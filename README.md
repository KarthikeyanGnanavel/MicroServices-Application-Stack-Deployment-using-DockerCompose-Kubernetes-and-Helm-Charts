
# Microservices Application Stack

This project is a microservices application that consists of a frontend service, a backend service, and a MongoDB database. It is designed to allow user registration and login functionality.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker Compose Deployment](#docker-compose-deployment)
- [Docker Swarm Deployment](#docker-swarm-deployment)
- [License](#license)

## Technologies Used
- Flask (Python)
- MongoDB
- Docker
- Docker Compose
- Docker Swarm

## Features
- User registration
- User login
- User authentication
- Data storage in MongoDB

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Ensure you have Docker and Docker Compose installed on your machine.
3. Build and start the services using Docker Compose:
   ```bash
   docker-compose up -d --build
   ```

## Usage
- Access the frontend application at `http://localhost:5000`.
- The backend API can be accessed at `http://localhost:5001`.

## API Endpoints
### User Registration
- **Endpoint:** `/register`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "username": "string",
      "email": "string",
      "password": "string",
      "gender": "string"
  }
  ```
- **Response:**
  - **201 Created:** User created successfully.
  - **409 Conflict:** User already exists. Please log in.

### User Login
- **Endpoint:** `/login`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "email": "string",
      "password": "string"
  }
  ```
- **Response:**
  - **200 OK:** Returns the username of the logged-in user.
  - **401 Unauthorized:** Invalid credentials.

## Docker Compose Deployment
To deploy the application using Docker Compose, run the following command:
```bash
docker-compose up -d --build
```

## Docker Swarm Deployment
To deploy the application using Docker Swarm, follow these steps:

1. Initialize Docker Swarm (if not already done):
   ```bash
   docker swarm init
   ```

2. Deploy the stack with your `docker-swarm.yml`:
   ```bash
   docker stack deploy -c docker-swarm.yml myapp
   ```

3. Access the frontend at `http://<node-ip>:5000`.

## License
This project is licensed under the MIT License.
