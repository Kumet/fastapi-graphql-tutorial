from core.database import Base
from sqlalchemy import Column, Integer, String


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)

    def as_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}
