import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProjectVersionCreate(BaseModel):
    version_number: int = 1
    label: Optional[str] = None
    notes: Optional[str] = None
    snapshot_json: Optional[str] = None


class ProjectVersionOut(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    version_number: int
    label: Optional[str] = None
    notes: Optional[str] = None
    snapshot_json: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
