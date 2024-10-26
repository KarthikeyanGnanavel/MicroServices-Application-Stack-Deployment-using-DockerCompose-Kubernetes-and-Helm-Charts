# Microservices Application

This repository contains a Dockerized microservices application built with Flask for the backend and a web frontend. The application allows users to register and log in, utilizing MongoDB as the database for user management.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration with email validation.
- User login functionality.
- Containerized services using Docker and Docker Compose.
- MongoDB for user data storage.

## Technologies

- Flask - Web framework for building the backend service.
- MongoDB - NoSQL database for storing user data.
- Docker - Containerization platform.
- Docker Compose - Tool for defining and running multi-container Docker applications.

## Architecture

The application consists of three main services:

1. **Frontend**: A web interface for user registration and login.
2. **Backend**: A RESTful API for handling user-related operations.
3. **MongoDB**: A database service for storing user information.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Docker Compose

### Running the Application

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd Microservices_App
   ```

2. Build and run the application using Docker Compose:

   ```bash
   docker-compose up -d --build
   ```

3. Open your web browser and navigate to `http://localhost:5000` to access the frontend application.

4. To stop the application, run:

   ```bash
   docker-compose down
   ```

## API Endpoints

### User Registration

- **Endpoint**: `/register`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "user1",
    "email": "user1@example.com",
    "password": "password123",
    "gender": "male"
  }
  ```
- **Response**:
  - `201 Created`: User created successfully.
  - `409 Conflict`: User already exists. Please log in.

### User Login

- **Endpoint**: `/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user1@example.com",
    "password": "password123"
  }
  ```
- **Response**:
  - `200 OK`: Returns the username of the logged-in user.
  - `401 Unauthorized`: Invalid credentials.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes.

