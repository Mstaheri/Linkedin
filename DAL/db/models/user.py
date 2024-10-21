from sqlalchemy.orm import Mapped, mapped_column
from DAL.db.engine import Base


class User(Base):
    __tablename__ = "users"
    firstname : Mapped[str] = mapped_column()
    lastname : Mapped[str] = mapped_column(primary_key=True)
    phonenumber : Mapped[str] = mapped_column()