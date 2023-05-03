from fastapi import Depends
from strawberry.types import Info

from crud import AuthorCRUD, BookCRUD, ItemCRUD


async def get_graphql_context(
    item_crud: ItemCRUD = Depends(),
    author_crud: AuthorCRUD = Depends(),
    book_crud: BookCRUD = Depends(),
):
    return {
        "item_crud": item_crud,
        "author_crud": author_crud,
        "book_crud": book_crud,
    }


def get_item_crud(info: Info) -> ItemCRUD:
    return info.context["item_crud"]


def get_author_crud(info: Info) -> AuthorCRUD:
    return info.context["author_crud"]


def get_book_crud(info: Info) -> BookCRUD:
    return info.context["book_crud"]
