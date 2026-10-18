
from typing import Optional

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field


app = FastAPI(
    title="Library API",
    description="A simple library management API built with FastAPI",
    version="1.0.0",
)


# Models
class BookIn(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: Optional[int] = Field(default=None, ge=0)
    available: bool = True


class BookUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1)
    author: Optional[str] = Field(default=None, min_length=1)
    year: Optional[int] = Field(default=None, ge=0)
    available: Optional[bool] = None


books = [
    {
        "id": 1,
        "title": "طراحی الگوریتم",
        "author": "سپیده",
        "year": None,
        "available": True,
    },
    {
        "id": 2,
        "title": "سووشون",
        "author": "سیمین دانشور",
        "year": 1969,
        "available": True,
    },
    {
        "id": 3,
        "title": "شازده کوچولو",
        "author": "آنتوان دو سنت‌اگزوپری",
        "year": 1943,
        "available": True,
    },
]

next_id = 4


def find_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found",
    )


@app.get("/books")
def get_books():
    return books


@app.post("/books", status_code=201)
def add_book(data: BookIn):
    global next_id

    new_book = data.model_dump()
    new_book["id"] = next_id

    books.append(new_book)
    next_id += 1

    return new_book


@app.get("/books/{id}")
def get_book(id: int):
    return find_book(id)


@app.patch("/books/{id}")
def update_book(id: int, data: BookUpdate):
    book = find_book(id)

    changes = data.model_dump(exclude_unset=True)

    for field, value in changes.items():
        if value is None:
            raise HTTPException(
                status_code=422,
                detail=f"{field} cannot be null",
            )

    book.update(changes)

    return book


@app.delete("/books/{id}", status_code=204)
def delete_book(id: int):
    book = find_book(id)
    books.remove(book)

    return Response(status_code=204)
