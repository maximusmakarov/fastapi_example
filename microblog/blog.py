from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from .schemas import PostCreate, PostList
from .service import get_post_list, create_post

router = APIRouter()


@router.get('/', response_model=List[PostList])
async def post_list(db: Session = Depends(get_db)):
    return await get_post_list(db)


@router.post('/')
async def post_list(item: PostCreate, db: Session = Depends(get_db)):
    return await create_post(db, item)
