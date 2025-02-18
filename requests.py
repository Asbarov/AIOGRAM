from sqlalchemy import select
from models import t_shirts,Trousers,Jackets,shoes
from models import async_session

async def t_shirts_req():
    async with async_session() as session:
        result=await session.execute(select(t_shirts))
        return result.scalars().all()

async def trousers_req():
    async with async_session() as session:
        result=await session.execute(select(Trousers))
        return result.scalars().all()
    
async def jackets_req():
    async with async_session() as session:
        result=await session.execute(select(Jackets))
        return result.scalars().all()
    
async def shoes_req():
   async with async_session() as session:
        result=await session.execute(select(shoes))
        return result.scalars().all() 


    
