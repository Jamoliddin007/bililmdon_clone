from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.orm import String


from datetime import datetime, Date, DateTime

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str] = mapped_column(unique=True)
    hashed_password:Mapped[str]  = mapped_column(String(128))
    username:Mapped[str] = mapped_column(String(32), unique=True)
    first_name:Mapped[str] = mapped_column(String(32))
    birthdate:Mapped[datetime] =  mapped_column(Date)
    joined_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    is_staff:Mapped[bool] = mapped_column(default=False)
    is_superuser:Mapped[bool] = mapped_column(default=False)
    is_active:Mapped[bool] = mapped_column(default=True)
