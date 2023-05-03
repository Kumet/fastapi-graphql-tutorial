from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from core.database import Base

# many-to-many relationship between Books and Authors
book_author_association = Table(
    "book_author_association",
    Base.metadata,
    Column("book_id", ForeignKey("books.id")),
    Column("author_id", ForeignKey("authors.id")),
)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(40), nullable=False)
    authors = relationship(
        "Author",
        lazy="dynamic",
        secondary=book_author_association,
    )

    def as_dict(self):
        return {"id": self.id, "name": self.name}
