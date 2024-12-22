# Project Name: **SafeSight**  

####      Bringing Security to Life: AI-powered real-time surveillance with customizable notifications for enhanced accessibility.
![Screenshot (140)](https://github.com/user-attachments/assets/31e0af88-9d54-4bbb-9e60-453a33fe972a)

## 🚀 Inspiration  
- This project addresses the need for enhanced surveillance systems that can not only detect activities but also provide detailed, context-rich descriptions of those events. It helps users, especially those with visual impairments, understand what's happening in their environment through AI-generated descriptions and notifications. By integrating real-time image recognition and notifications, this project improves accessibility and security.

- The inspiration for this project came from the desire to create a more inclusive and intelligent surveillance system. With the growing demand for smart security, I wanted to develop a solution that would make security camera footage more accessible to visually impaired users. By combining AI-driven image descriptions with customizable notifications via Twilio, I aimed to create a system that not only detects activities but also provides meaningful, human-like descriptions that could help users monitor their surroundings effectively.   

## 🧠 What it does  
- The surveillance camera AI assistant utilizes the Gemini API to generate detailed image descriptions of the activities detected by the camera. These descriptions are then sent to the user through customized notifications using the Twilio API. The system is built with Flask, HTML, CSS, and Bootstrap for an intuitive web interface. Users can adjust notification preferences based on the security level they choose (high, mid, or low), ensuring they are alerted appropriately for different incident priorities.
  
  - Activity Detection & Image Description: The AI system identifies events in the camera feed and generates detailed, context-rich descriptions using the Gemini API.
  - Customizable Notifications: Users can set their preferred notification method (call, message, or none) for different priority levels of incidents.
  - Real-Time Alerts: Users are notified instantly when an activity of interest is detected, with the system adjusting notifications based on user-configured preferences.
  - Enhanced Accessibility: Helps visually impaired users by providing audio or text-based descriptions of the scene, making it easier to monitor and understand their environment.
  - Security Monitoring: With adjustable security levels, the system ensures that only critical incidents trigger notifications, making it efficient and user-friendly. 

## ⚙️ How we built it

🛠️ Technologies, Frameworks, and Tools Used  

- **Flask**: A lightweight Python web framework used for creating the backend server, handling routing, and managing server-side logic.
- **HTML**: Used to create the structure of the web pages, providing an intuitive and easy-to-navigate interface for users.
- **CSS**: Used for styling the web interface, ensuring the application is visually appealing and responsive across devices.
- **Python**: The core programming language for the backend, managing the integration of APIs and the business logic for the system.
- **Gemini API**: An API that provides detailed, context-rich descriptions of images detected by the surveillance camera.
- **Twilio API**: An API used to send notifications (calls or messages) to the user based on incident priority and user preferences.

🏗️ High-Level Architecture  

The architecture is designed with clear separation of concerns between the frontend, backend, and external APIs:

1. **Frontend (Client-Side)**  
   - **HTML**: Provides the layout and structure of the web interface. Users interact with the frontend to set notification preferences and receive updates.
   - **CSS**: Responsible for the visual styling and responsive design of the application, ensuring it adapts to different screen sizes.
   - **JavaScript** (if needed for interactivity): Handles dynamic interactions, such as selecting notification preferences and triggering actions on the UI.

2. **Backend (Server-Side)**  
   - **Flask**: Handles HTTP requests, serves the frontend content, processes user interactions, and manages communication between the frontend and the external APIs (Gemini and Twilio).
   - **Python**: The backend is written in Python, and Flask serves as the framework that organizes the app. Python handles the integration of the Gemini and Twilio APIs and the core logic for the system.

3. **APIs**  
   - **Gemini API**: This API is used for generating detailed descriptions of the images captured by the surveillance camera. The Flask backend sends the captured image to the Gemini API and receives the generated description.
   - **Twilio API**: The Flask backend uses Twilio to send customized notifications (either a phone call or a text message) to users based on the configured priority and notification preferences.

4. **Workflow**  
   - The camera captures an image or video feed.
   - The backend detects activities in the footage and sends the image to the **Gemini API** for description generation.
   - The description is received and processed, then sent to the user via **Twilio API** according to the configured notification settings (phone call or text message).
   - The user is notified based on their chosen security level and preferences (e.g., receiving a call for high-priority incidents).

![Screenshot from 2024-12-22 00-32-16](https://github.com/user-attachments/assets/e38e1cdd-90ea-4c8f-9529-e5f7dfcadb54)


![image](https://github.com/user-attachments/assets/4e1fe093-d848-48b2-abf2-cdcf7f5a3bec)

Vision models can look at pictures and then tell you what's in them using words. These are called vision-to-text models. They bring together the power of understanding images and language. Using fancy neural networks, these models can look at pictures and describe them in a way that makes sense. They're like a bridge between what you see and what you can read.

This is super useful for things like making captions for images, helping people who can't see well understand what's in a picture, and organizing information. As these models get even smarter, they're going to make computers even better at understanding and talking about what they "see" in pictures. It's like teaching computers to understand and describe the visual world around us.image Based on which model we are using like OPENAI,GEMINI(sub models),Anthropic we use respective API KEY and also we use endpoint if necessary

➡️Generative model (predefined function) may play a key role in the whole process of development.

Gemini compared to other Models - 

Evidence suggests Gemini represents the state-of-the-art in foundation models:

It achieves record-breaking results on over 56 benchmarks spanning text, code, math, visual, and audio understanding. This includes benchmarks like MMLU, GSM8K, MATH, Big-Bench Hard, HumanEval, Natural2Code, DROP, and WMT23.

➡️Notably, Gemini Ultra is the first to achieve human-expert performance on MMLU across 57 subjects with scores above 90%.

➡️On conceptual reasoning benchmarks like BIG-Bench, Gemini outperforms expert humans in areas like math, physics, and CS.

➡️Specialized versions create state-of-the-art applications like the code generator AlphaCode 2 which solves programming problems better than 85% of human coders in competitions.

➡️Qualitative examples show Gemini can manipulate complex math symbols, correct errors in derivations, generate relevant UIs based on conversational context, and more.

## 💡 Challenges We Ran Into  

### Technical Challenges
1. **Gemini API Integration**  
   Integrating the Gemini API for image description posed a challenge in ensuring the descriptions were timely and accurate for real-time camera footage.  
   **Solution**: We conducted thorough testing with different images and fine-tuned the data sent to the Gemini API to improve response accuracy and reliability.

2. **Real-Time Notification System**  
   Setting up the Twilio API to send notifications based on user preferences (high, mid, low priority) in real time was a challenge.  
   **Solution**: We implemented clear logic for priority levels and tested various notification triggers to ensure the system worked smoothly.

### Logistical Challenges
1. **Time Constraints**  
   With limited time during the hackathon, balancing the development of features like AI image description, notification handling, and the web interface was challenging.  
   **Solution**: We prioritized core features first and incrementally added others, ensuring we could deliver a functional and polished project within the time limits.


## 🏆 Accomplishments That We're Proud Of  

- **Successful Integration of Gemini API**: We managed to integrate the Gemini API to generate accurate and detailed image descriptions in real time, providing meaningful context for surveillance footage.  
- **Real-Time Notification System**: The Twilio API integration allowed us to create a dynamic notification system that customizes alerts based on user preferences, ensuring that notifications are sent for high, mid, and low priority incidents.  
- **Seamless User Experience**: We developed an intuitive web interface using Flask, HTML, CSS, and Bootstrap, making it easy for users to interact with the system, configure notification preferences, and receive real-time updates.  
- **Innovative Accessibility Feature**: The project’s ability to provide detailed descriptions of surveillance footage offers a unique solution for visually impaired users, improving accessibility in security systems.  
- **Efficient Time Management**: Despite the time constraints of the hackathon, we successfully prioritized the core features and delivered a functional, polished product on schedule, demonstrating effective teamwork and planning.


## 🧪 What We Learned  

- **API Integration**: We gained a deeper understanding of how to effectively integrate external APIs (Gemini and Twilio) into a web application, ensuring smooth communication between the backend and third-party services.  
- **Real-Time Systems**: We learned how to build a real-time notification system, managing user preferences and triggering notifications based on different incident priorities in a dynamic environment.  
- **Accessibility in Technology**: Through the development of AI-generated image descriptions, we learned how technology can enhance accessibility, particularly for visually impaired users, making security systems more inclusive.  
- **Flask and Frontend Skills**: We honed our skills in Flask for backend development and improved our HTML, CSS, and Bootstrap knowledge to create a responsive and user-friendly frontend.  
- **Time Management and Collaboration**: During the hackathon, we learned how to prioritize tasks effectively, manage limited time, and collaborate efficiently as a team to deliver a well-rounded project.


## 🔮 What's next for SafeSight  
- The current version of our project is limited due to hardware and monetary constraints
- With better hardware we can make the frames reading faster
- With a paid subscription to the api services we can make faster and even more calls 

## 💻 Tech Stack  

- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Flask, Python  
- **APIs/Services:** Gemini API (for image description), Twilio API (for notifications)


## 🛠️ Installation and Usage  
1. **Clone the repository:**  
   ```bash  
   git clone https://github.com/Metadome-emergingtechhackathon/hackathon-mighty.git
