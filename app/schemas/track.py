import uuid
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from app.models.track import TrackType
from app.schemas.stem import StemOut


class TrackCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    track_type: TrackType = TrackType.generated
    order_index: int = 0


class TrackUpdate(BaseModel):
    name: Optional[str] = None
    track_type: Optional[TrackType] = None
    order_index: Optional[int] = None
    volume: Optional[float] = None
    pan: Optional[float] = None
    is_muted: Optional[bool] = None
    is_solo: Optional[bool] = None


class TrackOut(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    track_type: TrackType
    order_index: int
    volume: float
    pan: float
    is_muted: bool
    is_solo: bool
    created_at: datetime
    stems: List[StemOut] = []

    class Config:
        from_attributes = True
