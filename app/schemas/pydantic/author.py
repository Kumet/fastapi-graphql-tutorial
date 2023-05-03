from pydantic import BaseModel


class AuthorBaseSchema(BaseModel):
    name: str


class AuthorCreateSchema(AuthorBaseSchema):
    pass


class AuthorUpdateSchema(AuthorBaseSchema):
    pass


class AuthorSchema(AuthorBaseSchema):
    id: int
