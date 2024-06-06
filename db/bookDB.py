import psycopg  
from db import clientPS 


def consulta():
    # Recupera tots els llibres
    try:
        conn = clientPS.client()  
        cur = conn.cursor()  
        cur.execute("SELECT * FROM book")  
        data = cur.fetchall() 
    except Exception as e:
        print(f"Failed to connect: {e}")  
        return None
    finally:
        conn.close()  
    return data  

# Obté tots els llibres de la bd
def get_all_books():
    try:
        conn = clientPS.client()  
        cur = conn.cursor()  
        cur.execute("SELECT * FROM book")  
        data = cur.fetchall()  
    except Exception as e:
        print(f"Failed to connect: {e}")  
        return None
    finally:
        conn.close()  
    return data  

# Insertar un nou llibre a la base de dades
def insert(book):
    try:
        conn = clientPS.client()  
        cur = conn.cursor() 
        cur.execute("""
            INSERT INTO public.book(book_id, title, author, published_year, genre, language, pages, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            RETURNING book_id
            """, 
            (book.book_id, book.title, book.author, book.published_year, book.genre, book.language, book.pages)
        )
        inserted_id = cur.fetchone()[0]  # Recupera el ID 
        conn.commit()  
    except Exception as e:
        print(f"Failed to connect: {e}")  
        return None
    finally:
        conn.close()  
    return inserted_id 

# Esborra un llibre amb id
def delete_book(book_id):
    try:
        conn = clientPS.client() 
        cur = conn.cursor()  
        cur.execute("DELETE FROM book WHERE book_id = %s", (book_id,))
        conn.commit()  
        return True  
    except Exception as e:
        print(f"Failed to connect: {e}") 
        return False 
    finally:
        conn.close() 