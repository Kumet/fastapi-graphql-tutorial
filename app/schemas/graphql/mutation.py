import strawberry
from strawberry.types import Info

from core.graph_ql import get_author_crud, get_book_crud, get_item_crud

from . import Author, AuthorMutation, Book, BookMutation, Item, ItemMutation


@strawberry.type(description="Mutate all Entity")
class Mutation:
    @strawberry.mutation(description="Create an Item")
    def create_item(self, item: ItemMutation, info: Info) -> Item:
        item_crud = get_item_crud(info)
        return item_crud.create(item)

    @strawberry.mutation(description="Update an Item")
    def update_item(self, item_id: int, item: ItemMutation, info: Info) -> Item:
        item_crud = get_item_crud(info)
        return item_crud.update(item_id, item)

    @strawberry.mutation(description="Delete an Item")
    def delete_item(self, item: ItemMutation, info: Info) -> None:
        item_crud = get_item_crud(info)
        return item_crud.delete(item)

    @strawberry.mutation(description="Create an Author")
    def create_author(self, author: AuthorMutation, info: Info) -> Author:
        author_crud = get_author_crud(info)
        return author_crud.create(author)

    @strawberry.mutation(description="Update an Author")
    def update_author(self, author_id: int, author: AuthorMutation, info: Info) -> Author:
        author_crud = get_author_crud(info)
        return author_crud.update(author_id, author)

    @strawberry.mutation(description="Delete an Author")
    def delete_author(self, author: AuthorMutation, info: Info) -> None:
        author_crud = get_author_crud(info)
        return author_crud.delete(author)

    @strawberry.mutation(description="Create an Book")
    def create_book(self, book: BookMutation, info: Info) -> Book:
        book_crud = get_book_crud(info)
        return book_crud.create(book)

    @strawberry.mutation(description="Update an Book")
    def update_book(self, book_id: int, book: BookMutation, info: Info) -> Book:
        book_crud = get_book_crud(info)
        return book_crud.update(book_id, book)

    @strawberry.mutation(description="Delete an Book")
    def delete_book(self, book: BookMutation, info: Info) -> None:
        book_crud = get_book_crud(info)
        return book_crud.delete(book)
