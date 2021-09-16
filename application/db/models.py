from sqlalchemy import Column, Integer, String, Sequence
from .engine import Base, metadata


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String, unique=True)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, Sequence('post_count'), primary_key=True)
    message = Column(String)
