from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, DateTime, Integer, ForeignKey

from datetime import datetime, date, timezone
from typing import List

from app.models.option import Option
from app.models.game_question import GameQuestion
from app.models.submission import Submission

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000), nullable=True)
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topics.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

    option_ids: Mapped[List["Option"]] = relationship(back_populates="question")
    games: Mapped[List["GameQuestion"]] = relationship(back_populates="question")
    submissions: Mapped[List["Submission"]] = relationship(back_populates="question")
