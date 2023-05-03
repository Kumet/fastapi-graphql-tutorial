import strawberry
from core.graph_ql import get_item_crud
from strawberry.types import Info

from . import Item, ItemMutation


@strawberry.type(description="Mutate all Entity")
class Mutation:
    @strawberry.field(description="Create an Item")
    def create_item(self, item: ItemMutation, info: Info) -> Item:
        item_crud = get_item_crud(info)
        return item_crud.create(item)

    @strawberry.field(description="Update an Item")
    def update_item(self, item_id: int, item: ItemMutation, info: Info) -> Item:
        item_crud = get_item_crud(info)
        return item_crud.update(item_id, item)

    @strawberry.field(description="Delete an Item")
    def delete_item(self, item: ItemMutation, info: Info) -> None:
        item_crud = get_item_crud(info)
        return item_crud.delete(item)
