from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base

from .book import book_author_association


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(16), nullable=False)
    books = relationship("Book", lazy="dynamic", secondary=book_author_association)

    def as_dict(self):
        return {"id": self.id, "name": self.name}
