from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books: List[Book] = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="A Wizard of Earthsea", author="Ursula K. Le Guin"),
]


@app.get("/books", response_model=List[Book])
def list_books() -> List[Book]:
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Find the book or raise HTTPException with status code 404.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate) -> Book:
    # TODO: Assign the next ID, create the book, store it, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate) -> Book:
    # TODO: Replace the book's title and author, or raise HTTPException with 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    # TODO: Remove the book, or raise HTTPException with status code 404.
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)