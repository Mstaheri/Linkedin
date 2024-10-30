from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from DAL.persistence.engine import Base


class User(Base):
    __tablename__ = "users"
    firstname : Mapped[str] = mapped_column(String(50),nullable=False)
    lastname : Mapped[str] = mapped_column(String(50),nullable=False)
    username : Mapped[str] = mapped_column(String(50),primary_key=True)
    password : Mapped[str] = mapped_column(String(200),nullable=False)
    phonenumber : Mapped[str] = mapped_column(String(11) , nullable=True)
    email : Mapped[str] = mapped_column(unique=True , nullable=False)
    image : Mapped[str] = mapped_column(unique=True , nullable=True) 