from typing import List

import strawberry

from .book import Book


@strawberry.type(description="Author Schema")
class Author:
    id: int
    name: str
    books: List[Book]


@strawberry.input(description="Author Mutation Schema")
class AuthorMutation:
    name: str
