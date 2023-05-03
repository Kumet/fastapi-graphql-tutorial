import strawberry


@strawberry.type(description="Item Schema")
class Item:
    id: int
    name: str
    description: str


@strawberry.input(description="Item Mutation Schema")
class ItemMutation:
    name: str
    description: str
