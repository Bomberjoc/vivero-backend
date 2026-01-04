from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class ActivityLogBase(BaseModel):
    user_name: str
    plant_name: str
    action: str  # 'Creó', 'Modificó', 'Eliminó'
    description: str

class ActivityLogCreate(ActivityLogBase):
    user_id: Optional[UUID] = None

class ActivityLog(ActivityLogBase):
    id: UUID
    user_id: Optional[UUID] = None
    created_at: datetime

    class Config:
        from_attributes = True
