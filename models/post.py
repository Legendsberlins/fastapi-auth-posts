from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base

# Post model defines the structure of the 'posts' table in the database.
class Post(Base):
    _tablename_ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)