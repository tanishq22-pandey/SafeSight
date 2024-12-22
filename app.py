from flask import Flask, render_template, request, redirect, url_for, flash
import re
import os
import google.generativeai as genai
from PIL import Image
from twilio.rest import Client as TwilioClient

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'your_secret_key'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Twilio setup
account_sid = ''
auth_token = ''
twilio_client = TwilioClient(account_sid, auth_token)

from_phone_number =  ''
to_phone_number = ''

# AI model setup
api_key = ""
model_name = "gemini-1.5-flash-latest"

genai.configure(api_key=api_key)

s1= (
    "You are an advanced AI system specialized in generating detailed, context-rich descriptions of images. "
    "Your task is to analyze the provided image and create a comprehensive narrative that clearly communicates what’s happening in it. "
    "Focus on identifying objects, their relationships, and any significant interactions or activities. Pay attention to the environment, "
    "mood, and the context in which the image is set. The description should include the following:\n"
    "1. tObjects and People: Identify key elements in the image, including any people, animals, objects, or landmarks. "
    "Mention their appearance, placement, and any noteworthy characteristics.\n"
    "2. Actions and Interactions: If applicable, describe what people or objects are doing. Highlight any interactions between individuals "
    "or objects, including movements, gestures, and emotional expressions.\n"
    "3. Context and Environment: Provide context about the scene, including the location (e.g., indoors, outdoors), time of day, "
    "weather conditions, and the setting (e.g., home, park, street).\n"
    "4. Overall Narrative: Create a clear, coherent story or description that ties all these elements together in a logical flow, "
    "focusing on clarity and precision.\n"
    "do not give me any sort of priority here"
    "Your goal is to provide a description that not only identifies what is in the image but also captures its essence, giving the reader "
    "a vivid understanding of the scene. Ensure the description is informative, engaging, and useful, especially for individuals relying on it "
    "to gain insights into the content."
)

s2 = (
    "You are an advanced AI surveillance analyst. Your task is to analyze images from security cameras and "
    "generate detailed yet concise incident reports. Focus on identifying movements, anomalies, suspicious activities, "
    "and any notable events. Reports should be actionable and prioritize critical observations. Limit your responses "
    "Additionally, based on the urgency and significance of the detected event, assign any one priority level from the following options:\n"
     "- high_priority: Critical incidents, such as potential security breaches, unauthorized access, or immediate threats.\n"
    "- mid_priority: Notable events that may require attention but are not immediately threatening.\n"
    "- low_priority: Minor or inconsequential events that are unlikely to cause harm.\n"
    "to 150 words while ensuring clarity and precision."
    "You do not make descriptions."
)

system_content = s2

c1 = (
    "You are an AI-powered system tasked with analyzing images and generating detailed, context-rich descriptions. "
    "For each provided image, you should identify the objects, people, and elements present, along with their interactions and relationships. "
    "Focus on the following aspects:\n"
    "1. Objects and People: Describe the key elements in the image, including any individuals, animals, objects, or landmarks. "
    "Note their appearance, positions, and any significant details.\n"
    "2. Actions and Interactions: If applicable, explain what actions are taking place in the image. Describe any interactions, "
    "movements, or emotional expressions among people or objects.\n"
    "3. Context and Environment: Offer insight into the surroundings, including the time of day, location (indoor/outdoor), "
    "weather conditions, and the environment (e.g., a park, street, home).\n"
    "4. Narrative Summary: Craft a clear and coherent description that ties all elements together, providing a concise and "
    "engaging overview of the scene.\n"
    "Your goal is to generate a description that is informative, clear, and visually engaging, giving the reader a thorough understanding "
    "of what is happening in the image. Keep the description actionable and insightful."
)

c2 = (
    "You are an AI-powered system tasked with analyzing images and generating detailed, context-rich descriptions. "
    "For each provided image, you should identify the objects, people, and elements present, along with their interactions and relationships. "
    "Focus on the following aspects:\n"
    "1. Objects and People: Describe the key elements in the image, including any individuals, animals, objects, or landmarks. "
    "Note their appearance, positions, and any significant details. If the image quality is low, mention the reduced visibility or clarity but still provide as much detail as possible.\n"
    "2. Actions and Interactions: If applicable, explain what actions are taking place in the image. Describe any interactions, "
    "movements, or emotional expressions among people or objects. If the image is blurry or unclear, note that the lack of clarity may hinder interpretation, but identify any visible elements.\n"
    "3. Context and Environment: Offer insight into the surroundings, including the time of day, location (indoor/outdoor), "
    "weather conditions, and the environment (e.g., a park, street, home). If the image quality hinders recognition of the context, mention this limitation and focus on any identifiable features.\n"
    "4. Priority: Based on the importance of the image content, assign a priority level from the following options:\n"
    "   - high_priority: For critical, urgent events or suspicious activities that require immediate attention.\n"
    "   - mid_priority: For notable activities or events that may require further review.\n"
    "   - low_priority: For less significant, routine activities that do not need immediate attention. If the image is of low quality but involves potential concerns, err on the side of caution and assign the appropriate priority.\n"
    "5. Brief Summary: Provide a brief summary (about 10 words) of the key events taking place in the image. This summary should "
    "highlight the most important action or event in a concise manner, even if the image quality is low.\n"
    "Your goal is to generate a description that is informative, clear, and visually engaging, giving the reader a thorough understanding without pointing out what could be done to improve the image"
    "of what is happening in the image. Even for low-quality images, focus on extracting useful details while acknowledging any limitations due to poor image clarity."
)

user_content = c2


client_kwargs = {
    "model_name": model_name,
    "generation_config": {
        "temperature": 0.6,
        "top_p": 0.4
    },
    "system_instruction": system_content,
}
client = genai.GenerativeModel(**client_kwargs)

def send_message(body):
    try:
        message = twilio_client.messages.create(
            body=body,
            from_=from_phone_number,
            to=to_phone_number
        )
        print(f"Message sent: {body}")
    except Exception as e:
        print(f"Failed to send message: {e}")

def make_call():
    try:
        call = twilio_client.calls.create(
            to=to_phone_number,
            from_=from_phone_number,
            url='http://demo.twilio.com/docs/voice.xml'
        )
        print("Call initiated.")
    except Exception as e:
        print(f"Failed to make call: {e}")


# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# Upload Page Route
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        priority = request.form.get('priority', 'low')  # Default to 'low' if not set
        
        if file:
            filename = file.filename.replace(' ', '_')
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            flash('File successfully uploaded')
            
            return redirect(url_for('description', filename=filename, priority=priority))

    
    return render_template('index.html')



@app.route('/description/<filename>')
def description(filename):
    # Get priority from query parameters
    security_level = request.args.get('priority', 'low')  # Default to 'low' if not provided
    
    # Generate description using AI model
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img = Image.open(image_path)

    # Use your AI model to analyze the image
    response = client.generate_content([user_content, img], stream=True)
    response.resolve()  
    description = response.text if response.text else "No description generated."

    if user_content == c2:
                priority_tag = "low_priority"  # Default tag
                if "high_priority" in description:
                    priority_tag = "high_priority"
                elif "mid_priority" in description:
                    priority_tag = "mid_priority"
                elif "low_priority" in description:
                    priority_tag = "low_priority"

    if user_content == c2:
            if priority_tag == "high_priority":
                    if security_level == "high":
                        send_message("High priority incident detected!")
                        make_call()
                    elif security_level == "mid":
                        send_message("High priority incident detected!")
                    elif security_level == "low":
                        send_message("High priority incident detected!")
                    elif priority_tag == "mid_priority":
                        if security_level == "high":
                            send_message("Mid priority incident detected!")
                    elif security_level == "mid":
                            send_message("Mid priority incident detected!")
                    elif priority_tag == "low_priority":
                        if security_level == "high":
                            send_message("Low priority incident detected!")


    return render_template(
        'description.html',
        filename=filename,
        description=description,
        priority=priority_tag
    )


# Send Message function


if __name__ == '__main__':
    app.run(debug=True)