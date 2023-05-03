from typing import List, Optional, Type

from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from core.logger import setup_logger
from models import Author, Book
from schemas.pydantic import AuthorCreateSchema, AuthorUpdateSchema

logger = setup_logger(__name__)


class AuthorCRUD:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str] = None,
        limit: Optional[int] = 10,
        start: Optional[int] = 0,
    ) -> List[Type[Author]]:
        query = self.db.query(Author)
        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()

    def get(self, id: int) -> Optional[Type[Author]]:
        return self.db.get(Author, id)

    def create(self, author: AuthorCreateSchema) -> Author:
        author_model = Author(name=author.name)
        self.db.add(author_model)
        self.db.commit()
        self.db.refresh(author_model)
        return author_model

    def update(self, id: int, author: AuthorUpdateSchema) -> Author:
        author_model = Author(name=author.name)
        author_model.id = id
        self.db.merge(author_model)
        self.db.commit()
        return author_model

    def delete(self, id: int) -> None:
        author_model = self.db.get(Author, id)
        self.db.delete(author_model)
        self.db.commit()
        self.db.flush()

    def get_books(self, id: int) -> List[Book]:
        return self.db.get(Author, id).books
