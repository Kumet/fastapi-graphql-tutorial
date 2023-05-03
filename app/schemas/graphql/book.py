import strawberry


@strawberry.type(description="Book Schema")
class Book:
    id: int
    name: str


@strawberry.input(description="Book Mutation Schema")
class BookMutation:
    name: str
