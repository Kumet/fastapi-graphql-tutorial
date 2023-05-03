from typing import List, Optional, Type

from fastapi import APIRouter, Depends, status

from crud import ItemCRUD
from schemas.pydantic import Item, ItemCreate, ItemUpdate

item_router = APIRouter(prefix="/items")


@item_router.get("/", response_model=List[Item])
def index(
    name: Optional[str] = None,
    description: Optional[str] = None,
    limit: Optional[int] = 10,
    start: Optional[int] = 0,
    item_crud: ItemCRUD = Depends(),
) -> List[Type[Item]]:
    return item_crud.list(name, description, limit, start)


@item_router.get("/{item_id}", response_model=Item)
def get(item_id: int, item_crud: ItemCRUD = Depends()):
    return item_crud.get(item_id)


@item_router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create(item: ItemCreate, item_crud: ItemCRUD = Depends()):
    return item_crud.create(item)


@item_router.patch("/{item_id}", response_model=Item)
def update(item_id: int, item: ItemUpdate, item_crud: ItemCRUD = Depends()):
    return item_crud.update(item_id, item)


@item_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, item_crud: ItemCRUD = Depends()):
    return item_crud.delete(item_id)
