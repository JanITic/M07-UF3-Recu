from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import bookDB
from Model.Book import Book

from schema.book import book_schema, books_schema

app = FastAPI()

# ruta arrel
@app.get("/")  
def read_root():
    return {"Hello": "World"}

# ruta GET per llegir tot
@app.get("/book")  
def read_books():
    books_data = bookDB.consulta()
    print("Datos de los libros:", books_data)
    return book_schema(books_data)


# ruta POST per afegir llibre
@app.post("/book")  
def create_book(book: Book):
    try:
        success = bookDB.insert(book)
        if success:
            return {"message": "Book added successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to add Book to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ruta per eliminar book per id
@app.delete("/book/{book_id}")  
def delete_book(book_id: int):
    success = bookDB.delete_book(book_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="book not found")
    return {"message": "book deleted successfully"}