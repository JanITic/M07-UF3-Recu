from typing import List, Dict, Any

# dades individuals a un diccionari
def book_schema(book) -> dict:
    return {
        "book_id": str(book[0]),
        "title": book[1],
        # "author": book[2],
        # "published_year": book[3],
        # "genre": book[4],
        # "language": book[5],
        # "pages": book[6],
        # "created_at": book[7],
        # "updated_at": book[8]
    }

 
# aplicar
def books_schema(books) -> List[Dict[str, Any]]:
    return [book_schema(book) for book in books]