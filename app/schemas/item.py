from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: str = Field(default="", max_length=255)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=1, max_length=100)
    descripcion: str | None = Field(default=None, max_length=255)


class Item(ItemBase):
    id: int
