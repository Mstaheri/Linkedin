from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from DAL.persistence.engine import Base


class User(Base):
    __tablename__ = "users"
    firstname : Mapped[str] = mapped_column(String(50),nullable=False)
    lastname : Mapped[str] = mapped_column(String(50),nullable=False)
    username : Mapped[str] = mapped_column(String(50),primary_key=True)
    phonenumber : Mapped[str] = mapped_column(String(11) , nullable=True)