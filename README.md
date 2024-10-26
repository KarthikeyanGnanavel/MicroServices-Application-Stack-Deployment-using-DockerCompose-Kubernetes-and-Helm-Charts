# Microservices Application

## Overview
This is a microservices application built using Flask for the backend, React for the frontend, and MongoDB for the database. It supports user registration and login functionalities.

## Technologies Used
- **Frontend**: Flask
- **Backend**: Flask
- **Database**: MongoDB
- **Containerization**: Docker
- **Orchestration**: Docker Swarm

## Features
- User registration with unique email validation
- User login functionality
- Persistent storage for MongoDB
- Microservices architecture
- Deployable using Docker Swarm

## Prerequisites
- Docker installed on your machine
- Docker Compose installed
- Docker Swarm initialized (for swarm deployment)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Microservices_App
```

### 2. Build and Run with Docker Compose
You can run the application locally using Docker Compose:

```bash
docker-compose up -d --build
```

### 3. Access the Application
- Frontend: `http://localhost:5000`
- Backend: `http://localhost:5001`

### 4. Deploying with Docker Swarm
To deploy the application using Docker Swarm, follow these steps:

#### Step 1: Initialize Docker Swarm
If you haven't already initialized Docker Swarm, run:

```bash
docker swarm init
```

#### Step 2: Deploy the Stack
Use the following command to deploy the application stack using the `docker-swarm.yml` file:

```bash
docker stack deploy -c docker-swarm.yml myapp
```

#### Step 3: Accessing the Application
Once the services are deployed, you can access the application via the published ports on your node:

- Frontend: `http://<node-ip>:5000`
- Backend: `http://<node-ip>:5001`


### 5. Stopping Docker Swarm
To remove the stack and stop the services, run:

```bash
docker stack rm myapp
```

## Notes
- The application is designed for development purposes and may require additional security measures for production use.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

