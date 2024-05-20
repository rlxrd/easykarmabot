from app.database.models import User, async_session
from sqlalchemy import select, update


async def add_karma(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id, karma=1))
            new_karma = 1
        else:
            new_karma = user.karma + 1
            await session.execute(update(User).where(User.tg_id == tg_id).values(karma=new_karma))
        
        await session.commit()
        return new_karma
