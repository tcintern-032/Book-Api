from pydantic import BaseModel, Field  
class Student(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=100)
    course: str = Field(..., min_length=2)
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=100)
    course: str = Field(..., min_length=2)
class Book(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=2, max_length=100)
    author: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0) 