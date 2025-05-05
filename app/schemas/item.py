from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: Optional[bool] = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    title: Optional[str] = None
    is_active: Optional[bool] = None


class ItemInDBBase(ItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)


class Item(ItemInDBBase):
    pass


class ItemInDB(ItemInDBBase):
    pass 