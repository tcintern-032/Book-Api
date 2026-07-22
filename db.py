from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas
import database_model
from database import engine, get_db
app = FastAPI(title="Book API with SQLite")
database_model.Base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    return {"message": "Book API is running. Go to /docs to test"}
@app.post("/books", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(database_model.Book).filter(database_model.Book.id == book.id).first()
    if db_book:
        raise HTTPException(status_code=400, detail="Book ID already exists")
    new_book = database_model.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
@app.get("/books", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(database_model.Book).all()
@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(database_model.Book).filter(database_model.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(database_model.Book).filter(database_model.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(database_model.Book).filter(database_model.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}