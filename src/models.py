from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class urls(Base):
    __tablename__ = 'urls'

    slug: Mapped[str] = mapped_column(primary_key=True)

    long_url: Mapped[str] = mapped_column()