# Book API with JWT Authentication

A RESTful Book Management API built with FastAPI,SQLite, and SQLAlchemy that includes JWT (JSON Web Token) Authentication. Users can register, log in, receive a secure access token, and manage their own books through protected API endpoints.
This project demonstrates the implementation of authentication, password hashing, database integration, and secure API development using FastAPI.
# Features
* User Registration (Signup)
* User Login
* JWT Authentication
* Password Hashing using Passlib (bcrypt)
* SQLite Database Integration
* SQLAlchemy ORM
* Protected API Endpoints
* CRUD Operations for Books
* Books Associated with Logged-in Users
* Token Expiration
* Proper HTTP Status Codes
* Error Handling
* Interactive Swagger API Documentation
# Technologies Used
* Python 3.10+
* FastAPI
* SQLite
* SQLAlchemy
* Passlib (bcrypt)
* Python-JOSE (JWT)
* Uvicorn
# Project Structure
```text
book-api-auth/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── crud.py
│   └── dependencies.py
│
├── requirements.txt
├── README.md
└── .gitignore
```
# Run the Application
Start the FastAPI development server:
```bash
uvicorn app.main:app --reload
```
The API will be available at:
```
http://127.0.0.1:8000
```
# API Documentation
FastAPI automatically provides interactive API documentation.
Swagger UI
```
http://127.0.0.1:8000/docs
```
ReDoc
```
http://127.0.0.1:8000/redoc
```
# Authentication Flow

### Step 1: Register a User

**POST** `/signup`
Example Request

```json
{
  "username": "zeeshan",
  "password": "123456"
}
```
Example Response

```json
{
  "message": "User registered successfully"
}
```
### Step 2: Login

**POST** `/login`
Example Request

```json
{
  "username": "zeeshan",
  "password": "123456"
}
```
Example Response

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```
### Step 3: Authorize
1. Open Swagger UI.
2. Click the **Authorize** button.
3. Enter:
```
Bearer YOUR_ACCESS_TOKEN
```
4. Click **Authorize**.
Now you can access protected endpoints.
# Book Endpoints
## Home

| Method | Endpoint | Description     |
| ------ | -------- | --------------- |
| GET    | /        | Welcome message |

---
## Authentication
| Method | Endpoint | Description                 |
| ------ | -------- | --------------------------- |
| POST   | /signup  | Register a new user         |
| POST   | /login   | Login and receive JWT token |
## Books (Protected)

| Method | Endpoint | Description                     |
| ------ | -------- | ------------------------------- |
| POST   | /books   | Add a new book                  |
| GET    | /books   | Get all books of logged-in user |
# Example Book Request
```json
{
  "title": "Python Basics",
  "author": "John Doe"
}
```
Example Response

```json
{
  "id": 1,
  "title": "Python Basics",
  "author": "John Doe",
  "owner_id": 1
}
```
# Protected Routes
The following endpoints require authentication:

* POST `/books`
* GET `/books`
Requests without a valid JWT token will receive a **401 Unauthorized** response.
# Dependencies
```
fastapi
uvicorn
sqlalchemy
passlib[bcrypt]
python-jose
python-multipart
```
Install manually:
```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose python-multipart
```
# Learning Objectives
This project demonstrates:
* Building REST APIs with FastAPI
* Working with SQLite databases
* Using SQLAlchemy ORM
* Password hashing with Passlib
* JWT Authentication
* Authentication Dependencies
* Protected Routes
* User Registration and Login
* Secure API Development
* Error Handling with HTTPException
# Bonus Features
* Books linked to authenticated users
* JWT Token Expiration
* Authentication logic separated into its own module
* Organized project structure
* Secure password storage
* Reusable dependency injection
# Testing
You can test the API using:
* Swagger UI
* Postman
* Insomnia
# Author
**Developed By Muhammad Zeeshan Haider*    AI Engineering Track Learner
