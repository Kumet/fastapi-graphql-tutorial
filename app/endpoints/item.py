from typing import List, Optional

from fastapi import APIRouter

from schemas.pydantic import Item

item_router = APIRouter(prefix="/items")


@item_router.get("/", response_model=List[Item])
def index(
    name: Optional[str],
    description: Optional[str],
):
    return
