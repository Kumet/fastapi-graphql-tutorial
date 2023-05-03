from fastapi import Depends
from strawberry.types import Info

from crud import ItemCRUD


async def get_graphql_context(item_crud: ItemCRUD = Depends()):
    return {"item_crud": item_crud}


def get_item_crud(info: Info) -> ItemCRUD:
    return info.context["item_crud"]
