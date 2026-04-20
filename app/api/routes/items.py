from fastapi import APIRouter

from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.services.item_service import item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.post("", response_model=Item, status_code=201)
def create_item(payload: ItemCreate) -> Item:
    return item_service.create(payload)


@router.get("", response_model=list[Item])
def list_items() -> list[Item]:
    return item_service.list_all()


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    return item_service.get(item_id)


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemUpdate) -> Item:
    return item_service.update(item_id, payload)


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    item_service.delete(item_id)
