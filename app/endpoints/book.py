from typing import List, Optional

from fastapi import APIRouter, Depends, status

from core.logger import setup_logger
from crud import BookCRUD
from schemas.pydantic import AuthorSchema, BookAuthorPostRequestSchema, BookCreateSchema, BookSchema, BookUpdateSchema

logger = setup_logger(__name__)
book_router = APIRouter(prefix="/books")


@book_router.get("/", response_model=List[BookSchema])
def index(name: Optional[str] = None, book_crud: BookCRUD = Depends()):
    return [book.as_dict() for book in book_crud.list(name=name)]


@book_router.get("/{id}", response_model=BookSchema)
def get(id: int, book_crud: BookCRUD = Depends()):
    return book_crud.get(id).as_dict()


@book_router.post("/", response_model=BookSchema, status_code=status.HTTP_201_CREATED)
def create(book: BookCreateSchema, book_crud: BookCRUD = Depends()):
    return book_crud.create(book).as_dict()


@book_router.patch("/{id}", response_model=BookSchema)
def update(id: int, book: BookUpdateSchema, book_crud: BookCRUD = Depends()):
    return book_crud.update(id, book).as_dict()


@book_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, book_crud: BookCRUD = Depends()):
    return book_crud.delete(id)


@book_router.get("/{id}/auhors/", response_model=List[BookSchema])
def get_authors(id: int, book_crud: BookCRUD = Depends()):
    return [book.as_dict() for book in book_crud.get_authors(id)]


@book_router.post("/{id}/authors/", response_model=List[AuthorSchema])
def add_author(id: int, author: BookAuthorPostRequestSchema, book_crud: BookCRUD = Depends()):
    return [author.as_dict() for author in book_crud.add_author(id, author)]


@book_router.delete("/{id}/authors/{author_id}", response_model=List[AuthorSchema])
def remove_author(id: int, author_id: int, book_crud: BookCRUD = Depends()):
    return [author.as_dict() for author in book_crud.remove_author(id, author_id)]
