from pydantic import BaseModel

class Book(BaseModel):
    book_id:int
    title:str
    author:str
    published_year:int
    genre:str
    language:str
    pages:int