from typing import List, Optional

import strawberry
from strawberry.types import Info

from core.graph_ql import get_author_crud, get_book_crud, get_item_crud

from . import Author, Book, Item


@strawberry.type(description="Query all Entities")
class Query:
    @strawberry.field(description="List all Items")
    def items(self, info: Info) -> List[Item]:
        item_crud = get_item_crud(info)
        return item_crud.list()

    @strawberry.field(description="Get an Item")
    def item(self, item_id: int, info: Info) -> Optional[Item]:
        item_crud = get_item_crud(info)
        return item_crud.get(item_id)

    @strawberry.field(description="List all Authors")
    def authors(self, info: Info) -> List[Author]:
        author_crud = get_author_crud(info)
        return author_crud.list()

    @strawberry.field(description="Get an Author")
    def author(self, id: int, info: Info) -> Optional[Author]:
        author_crud = get_author_crud(info)
        return author_crud.get(id)

    @strawberry.field(description="List all Books")
    def books(self, info: Info) -> List[Book]:
        book_crud = get_book_crud(info)
        return book_crud.list()

    @strawberry.field(description="Get an Book")
    def book(self, id: int, info: Info) -> Optional[Book]:
        book_crud = get_book_crud(info)
        return book_crud.get(id)
