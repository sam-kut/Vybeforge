import uuid
from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import String, DateTime, ForeignKey, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class TrackType(str, PyEnum):
    vocals = "vocals"
    drums = "drums"
    bass = "bass"
    instruments = "instruments"
    generated = "generated"
    upload = "upload"


class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    track_type: Mapped[TrackType] = mapped_column(Enum(TrackType), default=TrackType.generated)
    order_index: Mapped[int] = mapped_column(Integer, default=0)
    volume: Mapped[float] = mapped_column(default=1.0)
    pan: Mapped[float] = mapped_column(default=0.0)
    is_muted: Mapped[bool] = mapped_column(default=False)
    is_solo: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="tracks")
    stems = relationship("Stem", back_populates="track", cascade="all, delete-orphan")
