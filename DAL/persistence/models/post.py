from sqlalchemy.orm import Mapped, mapped_column
from DAL.persistence.engine import Base


class user(Base):
    _tablename = "users"
    FirstName : Mapped[str] = mapped_column()
    UserName : Mapped[str] = mapped_column()