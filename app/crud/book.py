from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from core.logger import setup_logger
from models import Author, Book
from schemas.pydantic import BookAuthorPostRequestSchema, BookCreateSchema, BookUpdateSchema

logger = setup_logger(__name__)


class BookCRUD:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str] = None,
        limit: Optional[int] = 10,
        start: Optional[int] = 0,
    ) -> List[Book]:
        query = self.db.query(Book)
        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()

    def get(self, id: int) -> Optional[Book]:
        return self.db.get(Book, id)

    def create(self, book: BookCreateSchema) -> Book:
        book_model = Book(name=book.name)
        self.db.add(book_model)
        self.db.commit()
        self.db.refresh(book_model)
        return book_model

    def update(self, id: int, book: BookUpdateSchema) -> Book:
        book_model = Book(name=book.name)
        book_model.id = id
        self.db.merge(book_model)
        self.db.commit()
        return book_model

    def delete(self, id: int) -> None:
        book_model = self.db.get(Book, id)
        self.db.delete(book_model)
        self.db.commit()
        self.db.flush()

    def get_authors(self, id: int) -> List[Author]:
        return self.db.get(Book, id).authors

    def add_author(self, book_id: int, author_body: BookAuthorPostRequestSchema) -> List[Author]:
        author = self.db.get(Author, author_body.author_id)
        book = self.db.get(Book, book_id)
        book.authors.append(author)
        self.db.merge(book)
        self.db.commit()
        return book.authors

    def remove_author(self, book_id: int, author_id: int) -> List[Author]:
        book = self.db.get(Book, book_id)
        book.authors = list(filter(lambda author: author.id != author_id, book.authors))
        self.db.merge(book)
        self.db.commit()
        return book.authors
