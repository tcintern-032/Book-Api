## Book API (FastAPI + SQLite)
A Rest-ful Book Management API built with **FastAPI**, **SQLite**, and **SQLAlchemy**. This project demonstrates how to connect FastAPI with a real database and perform complete CRUD (Create, Read, Update, Delete) operations. It follows a modular project structure and uses Pydantic for data validation.
## Features
- Create a new book
- View all books
- View a single book by ID
- Update an existing book
- Delete a book
- Persistent data storage using SQLite
- SQLAlchemy ORM integration
- Request and response validation with Pydantic
- HTTP status codes and exception handling
- Automatic API documentation with Swagger UI
- Modular project structure
- `created_at` timestamp for each book
## Technologies Used
- Python 3.x
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn
## Project Structure
```
book-api-fastapi-sqlite/
│
├── app/
│   ├── main.py          # FastAPI application and routes
│   ├── database.py      # Database connection
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD operations
│   └── __init__.py
│
├── books.db             # SQLite database
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore
```
## Run the Application
```bash
uvicorn app.main:app --reload
```
The server will start at:
```
http://127.0.0.1:8000
```
## API Documentation
Swagger UI
```
http://127.0.0.1:8000/docs
```
ReDoc
```
http://127.0.0.1:8000/redoc
```
## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/books` | Retrieve all books |
| GET | `/books/{id}` | Retrieve a book by ID |
| POST | `/books` | Create a new book |
| PUT | `/books/{id}` | Update a book |
| DELETE | `/books/{id}` | Delete a book |
## Example Request
### Create a Book
**POST** `/books`
```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "pages": 320
}
```
### Example Response
```json
{
  "id": 1,
  "title": "Atomic Habits",
  "author": "James Clear",
  "pages": 320,
  "created_at": "2026-07-22T10:30:00"
}
```
## Database
This project uses **SQLite** as the database.
Database file:
```
books.db
```
SQLAlchemy is used as the ORM to interact with the database.
## Validation
- Required fields are validated using Pydantic.
- Invalid requests return appropriate HTTP error responses.
- Non-existent book IDs return `404 Not Found`.
- Duplicate book IDs are prevented (if IDs are manually provided).
## Requirements
```
fastapi
uvicorn
sqlalchemy
pydantic
```
Install them using:
```bash
pip install -r requirements.txt
```
## Learning Objectives
This project helps you understand:
- Building REST APIs with FastAPI
- Connecting FastAPI with SQLite
- Using SQLAlchemy ORM
- Creating database models
- Performing CRUD operations
- Request validation with Pydantic
- Exception handling
- Organizing FastAPI projects into modules
## Author
**Devoloped By Muhammad Zeeshan Haider**
