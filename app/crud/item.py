from typing import List, Optional, Type

from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from core.logger import setup_logger
from models import Item
from schemas.pydantic import ItemCreate, ItemUpdate

logger = setup_logger(__name__)


class ItemCRUD:
    db: Session

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        limit: Optional[int] = 10,
        start: Optional[int] = 0,
    ) -> List[Type[Item]]:
        query = self.db.query(Item)
        if name:
            query = query.filter_by(name=name)
        if description:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()

    def get(self, item_id: int) -> Optional[Type[Item]]:
        return self.db.get(Item, item_id)

    def create(self, item: ItemCreate) -> Item:
        item_model = Item(name=item.name, description=item.description)
        self.db.add(item_model)
        self.db.commit()
        self.db.refresh(item_model)
        return item_model

    def update(self, item_id: int, item: ItemUpdate) -> Item:
        item_model = Item(name=item.name, description=item.description)
        item_model.id = item_id
        self.db.merge(item_model)
        self.db.commit()
        return item_model

    def delete(self, item_id: int) -> None:
        item_model = self.db.get(Item, item_id)
        self.db.delete(item_model)
        self.db.commit()
        self.db.flush()
