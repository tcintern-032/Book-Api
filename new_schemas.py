from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class BookCreate(BaseModel):
    title: str
    author: str


class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True