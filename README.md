 AI-Based Crowd Density & Safety Alert System

📌 Overview

The AI-Based Crowd Density & Safety Alert System is a computer vision project designed to monitor real-time crowd levels using video input. The system detects people in a frame, counts them, and classifies the crowd density into different levels to identify potentially unsafe situations.

This project demonstrates the practical application of Computer Vision techniques for solving real-world safety problems in public spaces such as campuses, markets, and events.

🎯 Problem Statement

Overcrowding in public areas can lead to safety risks such as accidents, stampedes, and security issues. There is a need for an automated system that can monitor crowd density in real-time and generate alerts when the situation becomes critical.

🎯 Objectives

Detect people in real-time video streams
Count the number of individuals present
Classify crowd density into levels (Low, Medium, High)
Provide visual alerts for unsafe crowd conditions
🧠 Key Features

✅ Real-time human detection using OpenCV
✅ Crowd counting and density classification
✅ Visual alert system for high-density scenarios
✅ Lightweight and easy to deploy
✅ No need for custom model training
⚙️ Tech Stack

Programming Language: Python
Libraries: OpenCV, NumPy
Model Used: HOG + SVM (Pre-trained Human Detector)
Platform: Desktop / Laptop
🏗️ Project Structure

crowd-density-system/ │── app.py # Main application │── detector.py # People detection logic │── requirements.txt # Dependencies │── README.md # Project documentation │── report.pdf # Project report

🔍 Methodology

Capture video input using a webcam

Use HOG (Histogram of Oriented Gradients) with SVM for human detection

Draw bounding boxes around detected individuals

Count the number of detected people

Classify crowd density:

Low (0–2 people)
Medium (3–6 people)
High (7+ people)
Display results on screen with alerts

🧮 Algorithm

Start video capture
For each frame: a. Detect humans using HOG + SVM b. Count number of detections c. Classify density level d. Display count and alert
Repeat until exit
▶️ Installation & Setup

Step 1: Clone the Repository

bash git clone https://github.com/your-username/crowd-density-system.git cd crowd-density-system

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Run the Project

python app.py

📊 Output

Real-time video feed with:

Detected people highlighted using bounding boxes
Total people count displayed
Crowd density level shown (Low / Medium / High)
📸 Screenshots

image image
🚀 Applications

Smart city surveillance systems
Crowd monitoring in events and festivals
College campus safety
Public transport stations
Shopping malls and marketplaces
⚠️ Limitations

Accuracy may reduce in low lighting conditions
Occlusion (people overlapping) may affect detection
Works best with a clear camera view
🔮 Future Improvements
Use YOLOv8 for more accurate detection
Add sound/email alerts for high crowd density
Deploy as a web application using Flask
Integrate with CCTV systems
Add heatmaps for crowd visualization
📚 Learning Outcomes
Practical implementation of Computer Vision
Understanding object detection techniques
Real-time video processing using OpenCV
Problem-solving using AI in real-world scenarios
👨‍💻 Author
Utkarsh Pandey Third Year Student, VIT Bhopal

📜 License

This project is for academic purposes only.

⭐ Acknowledgements

OpenCV Library
Computer Vision Course Resources
Pre-trained HOG + SVM Detector
