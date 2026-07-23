from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
import models
import crud
from database import engine
from dependencies import get_db
from dependencies import get_current_user
from new_schemas import UserCreate
from new_schemas import UserLogin
from new_schemas import BookCreate
from auth import hash_password
from auth import verify_password
from auth import create_access_token
models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Book API with JWT Authentication"
)
@app.get("/")
def home():
    return {"message": "Book API Authentication"}
@app.post("/signup")
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing = crud.get_user(db, user.username)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    hashed = hash_password(user.password)

    crud.create_user(
        db,
        user.username,
        hashed
    )

    return {"message": "User registered successfully"}
@app.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = crud.get_user(
        db,
        user.username
    )
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(
        {
            "sub": db_user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@app.post("/books")
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
  return crud.create_book(
        db,
        book.title,
        book.author,
        current_user.id
    )
@app.get("/books")
def get_books(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
 return current_user.books