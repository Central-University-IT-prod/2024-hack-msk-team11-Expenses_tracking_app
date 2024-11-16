from sqlalchemy import String, Integer, Column, ForeignKey, DateTime, Table, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


class Base(DeclarativeBase):
    def __repr__(self) -> str:
        class_ = self.__class__.__name__
        attrs = sorted((k, getattr(self, k)) for k in self.__mapper__.columns.keys())
        formatted_attrs = ", ".join("{}={!r}".format(*x) for x in attrs)

        return f"{class_}({formatted_attrs})"


association_table = Table(
    "association_table",
    Base.metadata,
    Column("events", ForeignKey("events.id")),
    Column("users", ForeignKey("users.id")),
)


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    link: Mapped[str] = mapped_column(String(128), nullable=False)
    owner = Column(BigInteger(), ForeignKey("users.id"))
    users: Mapped[list["User"]] = relationship(secondary=association_table, lazy="selectin")


class Cheque(Base):
    __tablename__ = "cheques"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    params: Mapped[str] = mapped_column(String(256), nullable=False)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    events: Mapped[list[Event]] = relationship(
        secondary=association_table, back_populates="users", lazy="selectin"
    )


class Obligations(Base):
    __tablename__ = "obligations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    lender: Mapped[int] = Column(BigInteger, ForeignKey("users.id"))
    borrower: Mapped[int] = Column(BigInteger, ForeignKey("users.id"))
    event: Mapped[int] = Column(Integer, ForeignKey("events.id"))
    amount: Mapped[int] = mapped_column(BigInteger)
