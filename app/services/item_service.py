from fastapi import HTTPException

from app.schemas.item import Item, ItemCreate, ItemUpdate


class ItemService:
    def __init__(self) -> None:
        self._db: dict[int, Item] = {}
        self._next_id = 1

    def create(self, payload: ItemCreate) -> Item:
        item = Item(id=self._next_id, **payload.model_dump())
        self._db[self._next_id] = item
        self._next_id += 1
        return item

    def list_all(self) -> list[Item]:
        return list(self._db.values())

    def get(self, item_id: int) -> Item:
        item = self._db.get(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item no encontrado")
        return item

    def update(self, item_id: int, payload: ItemUpdate) -> Item:
        item = self.get(item_id)
        changes = payload.model_dump(exclude_unset=True)
        updated_item = item.model_copy(update=changes)
        self._db[item_id] = updated_item
        return updated_item

    def delete(self, item_id: int) -> None:
        if item_id not in self._db:
            raise HTTPException(status_code=404, detail="Item no encontrado")
        del self._db[item_id]


item_service = ItemService()
