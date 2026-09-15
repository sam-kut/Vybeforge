import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class StemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    audio_url: Optional[str] = None
    start_time: float = 0.0
    duration: Optional[float] = None
    order_index: int = 0


class StemUpdate(BaseModel):
    name: Optional[str] = None
    audio_url: Optional[str] = None
    start_time: Optional[float] = None
    duration: Optional[float] = None
    order_index: Optional[int] = None


class StemOut(BaseModel):
    id: uuid.UUID
    track_id: uuid.UUID
    name: str
    audio_url: Optional[str] = None
    start_time: float
    duration: Optional[float] = None
    order_index: int
    created_at: datetime

    class Config:
        from_attributes = True
