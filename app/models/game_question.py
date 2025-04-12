from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, ForeignKey
from app.models.game import Game
from app.models.question import Question


from app.database import Base

class GameQuestion(Base):
    __tablename__ = "game_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"))
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("questions.id"))

    question: Mapped["Question"] = relationship(back_populates="games")
    game: Mapped["Game"] = relationship(back_populates="questions")