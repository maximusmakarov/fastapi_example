from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
from user.models import User


class Post(Base):
    __tablename__ = 'microblog_posts'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(500))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship(User)