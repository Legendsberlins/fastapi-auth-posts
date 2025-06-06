# services/post.py
from cachetools import TTLCache
from ..models.post import Post
from sqlalchemy.orm import Session

cache = TTLCache(maxsize=100, ttl=300)  # Cache for 5 minutes

def add_post(db: Session, user_id: int, text: str):
    post = Post(user_id=user_id, text=text)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post.id

def get_posts(db: Session, user_id: int):
    if user_id in cache:
        return cache[user_id]
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    cache[user_id] = posts  # Cache response
    return posts

def delete_post(db: Session, user_id: int, post_id: int):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False