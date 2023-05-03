from typing import List, Optional

from fastapi import APIRouter, Depends, status

from core.logger import setup_logger
from crud import AuthorCRUD
from schemas.pydantic import AuthorCreateSchema, AuthorSchema, AuthorUpdateSchema, BookSchema

setup_logger(__name__)
author_router = APIRouter(prefix="/authors")


@author_router.get("/", response_model=List[AuthorSchema])
def index(name: Optional[str] = None, author_crud: AuthorCRUD = Depends()):
    return [author.as_dict() for author in author_crud.list(name=name)]


@author_router.get("/{id}", response_model=AuthorSchema)
def get(id: int, author_crud: AuthorCRUD = Depends()):
    return author_crud.get(id)


@author_router.post("/", response_model=AuthorSchema, status_code=status.HTTP_201_CREATED)
def create(author: AuthorCreateSchema, author_crud: AuthorCRUD = Depends()):
    return author_crud.create(author).as_dict()


@author_router.patch("/{id}", response_model=AuthorSchema)
def update(id: int, author: AuthorUpdateSchema, author_crud: AuthorCRUD = Depends()):
    return author_crud.update(id, author).as_dict()


@author_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, author_crud: AuthorCRUD = Depends()):
    return author_crud.delete(id)


@author_router.get("/{id}/books/", response_model=List[BookSchema])
def get_books(id: int, author_crud: AuthorCRUD = Depends()):
    return [book.as_dict() for book in author_crud.get_books(id)]
