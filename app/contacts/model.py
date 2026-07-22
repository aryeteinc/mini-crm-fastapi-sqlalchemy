from datetime import datetime

from sqlalchemy import DateTime,String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.database import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    phone: Mapped[str | None] =  mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now() )

    notes: Mapped[list["Note"]] = relationship("Note", back_populates="contact")
