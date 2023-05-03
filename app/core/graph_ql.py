from crud import ItemCRUD
from fastapi import Depends
from strawberry.types import Info


async def get_graphql_context(item_crud: ItemCRUD = Depends()):
    return {"item_crud": item_crud}


def get_item_crud(info: Info) -> ItemCRUD:
    return info.context["item_crud"]
