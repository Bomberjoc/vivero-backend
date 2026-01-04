from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class PlantImageBase(BaseModel):
    image_url: str
    is_main: bool = False

class PlantImage(PlantImageBase):
    id: UUID
    plant_id: UUID

    class Config:
        from_attributes = True

class PlantCommonNameBase(BaseModel):
    common_name: str

class PlantCommonName(PlantCommonNameBase):
    id: UUID
    plant_id: UUID

    class Config:
        from_attributes = True

class PlantBase(BaseModel):
    name: str
    scientific_name: Optional[str] = None
    price: float
    description: Optional[str] = None

class PlantCreate(PlantBase):
    pass

class Plant(PlantBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    plant_images: List[PlantImage] = []
    plant_common_names: List[PlantCommonName] = []

    class Config:
        from_attributes = True
