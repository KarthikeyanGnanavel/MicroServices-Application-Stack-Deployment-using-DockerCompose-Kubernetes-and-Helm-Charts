My Application
Overview
My Application is a web-based platform - three tier web application that allows users to register, log in, and manage their profiles. Built using Flask for the backend and Bootstrap for the frontend, this application demonstrates the use of microservices architecture, containerization with Docker, and database management using MongoDB.

Features
User registration and authentication
Responsive and user-friendly interface
Gender selection during registration
Login and logout functionality
Success and error messages displayed in dialog boxes
Well-structured code with separation of concerns
Tech Stack
Frontend: HTML, CSS, Bootstrap
Backend: Python, Flask
Database: MongoDB
Containerization: Docker
Orchestration: Docker Compose
Getting Started
Prerequisites
Docker and Docker Compose installed on your machine
Python 3.x
MongoDB
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Build and run the Docker containers:

bash
Copy code
docker-compose up --build
Access the application in your web browser at http://localhost:5000.

Usage
To register, navigate to /register.
To log in, navigate to /login.
After logging in, you'll be redirected to your homepage.
Directory Structure
csharp
Copy code
.
├── backend               # Backend application
│   └── app.py           # Main application file
├── frontend              # Frontend application
│   ├── templates         # HTML templates
│   └── static            # Static files (CSS, JS)
├── database              # MongoDB container
├── docker-compose.yml    # Docker Compose configuration
└── README.txt            # This README file
Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License.

Author
Karthikeyan Gnanavel
Email: karthikgnanavel88@gmail.com
