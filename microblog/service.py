from asyncio import sleep

from sqlalchemy.orm import Session
from .models import Post
from .schemas import PostCreate


async def get_post_list(db: Session):
    return db.query(Post).all()


async def create_post(db: Session, item: PostCreate):
    post = Post(**item.dict())
    await sleep(10)  # здесь эмулируется работа нагрузки на процессор
    db.add(post)
    db.commit()
    db.refresh(post)

    return post
