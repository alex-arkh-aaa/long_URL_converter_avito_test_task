from sqlalchemy.orm import declarative_base, Mapped, mapped_column

class Base(declarative_base):
    pass

class urls(Base):
    __tablename__ = 'urls'

    slug: Mapped[str] = mapped_column(primary_key=True)

    long_url: Mapped[str] = mapped_column()