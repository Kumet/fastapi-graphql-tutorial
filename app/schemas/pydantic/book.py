from pydantic import BaseModel


class BookBaseSchema(BaseModel):
    name: str


class BookCreateSchema(BookBaseSchema):
    pass


class BookUpdateSchema(BookBaseSchema):
    pass


class BookSchema(BookBaseSchema):
    id: int


class BookAuthorPostRequestSchema(BaseModel):
    author_id: int
