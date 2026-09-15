import uuid
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from app.models.project import ProjectStatus, ProjectType
from app.schemas.track import TrackOut


class ProjectCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = None
    project_type: ProjectType = ProjectType.ai_song
    prompt_text: Optional[str] = None
    genre: Optional[str] = None
    tempo: Optional[int] = None
    key_signature: Optional[str] = None
    is_public: bool = False


class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None
    prompt_text: Optional[str] = None
    genre: Optional[str] = None
    tempo: Optional[int] = None
    key_signature: Optional[str] = None
    is_public: Optional[bool] = None


class ProjectOut(BaseModel):
    id: uuid.UUID
    owner_id: uuid.UUID
    title: str
    description: Optional[str] = None
    project_type: ProjectType
    status: ProjectStatus
    prompt_text: Optional[str] = None
    genre: Optional[str] = None
    tempo: Optional[int] = None
    key_signature: Optional[str] = None
    is_public: bool
    created_at: datetime
    updated_at: datetime
    tracks: List[TrackOut] = []

    class Config:
        from_attributes = True
