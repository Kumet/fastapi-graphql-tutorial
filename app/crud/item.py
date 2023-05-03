from typing import List, Optional, Type

from core.database import get_db
from fastapi import Depends
from models import Item
from sqlalchemy.orm import Session


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

    def create(self, item: Item) -> Item:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update(self, item_id: int, item: Item) -> Item:
        item.id = item_id
        self.db.merge(item)
        self.db.commit()
        return item

    def delete(self, item: Item) -> None:
        self.db.delete(item)
        self.db.commit()
        self.db.flush()
