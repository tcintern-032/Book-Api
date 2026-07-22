from fastapi import FastAPI, HTTPException, status
from models import Book
app = FastAPI()
books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "Ali",
        "price": 500
    },
    {
        "id": 2,
        "title": "FastAPI Guide",
        "author": "Ahmed",
        "price": 800
    },
    {
        "id": 3,
        "title": "Html Basics",
        "author": "Noman",
        "price": 300
    },
    {
        "id": 4,
        "title": "Css Basics",
        "author": "Zubair",
        "price": 400
    },
    {
        "id": 5,
        "title": "Java Basics",
        "author": "Aslam",
        "price": 600
    }
]
@app.get("/")
def home():
    return {"message": "Welcome to Book API"}
@app.get("/books")
def get_books():
    return books
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    books.append(book.model_dump())
    return {
        "message": "Book Added Successfully",
        "book": book
    }
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books[index] = updated_book.model_dump()
            return {
                "message": "Book Updated Successfully",
                "book": updated_book
            }
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {
                "message": "Book Deleted Successfully"
            }
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
@app.get("/search")
def search_book(title: str):
    result = []
    for book in books:
        if title.lower() in book["title"].lower():
            result.append(book)
    return result                  