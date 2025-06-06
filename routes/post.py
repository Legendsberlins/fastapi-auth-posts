from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.post import PostCreate, PostDelete
from ..services.auth import validate_token
from ..services.post import add_post, get_posts, delete_post
from ..database import get_db

router = APIRouter()

@router.post("/addpost")
def add_post_endpoint(post: PostCreate, token: str, db: Session = Depends(get_db)):
    user = validate_token(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    post_id = add_post(db, user.id, post.text)
    return {"postID": post_id}

@router.get("/getposts")
def get_posts_endpoint(token: str, db: Session = Depends(get_db)):
    user = validate_token(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    posts = get_posts(db, user.id)
    return posts

@router.delete("/deletepost")
def delete_post_endpoint(post: PostDelete, token: str, db: Session = Depends(get_db)):
    user = validate_token(db, token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    success = delete_post(db, user.id, post.postID)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}