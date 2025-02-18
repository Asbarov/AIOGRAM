from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped
from sqlalchemy.ext.asyncio import AsyncAttrs,async_sessionmaker,create_async_engine

engine=create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session=async_sessionmaker(engine)

class Base(DeclarativeBase,AsyncAttrs):
    pass

class t_shirts(Base):
    __tablename__='tshirts'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column()

class Trousers(Base):
    __tablename__='trousers'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column()

class Jackets(Base):
    __tablename__='jackets'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column()

class shoes(Base):
    __tablename__='shoes'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column()

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
