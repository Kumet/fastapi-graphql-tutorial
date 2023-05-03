from typing import List, Optional

import strawberry
from strawberry.types import Info

from core.graph_ql import get_item_crud

from . import Item


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
