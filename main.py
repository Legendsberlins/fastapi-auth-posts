from fastapi import FastAPI
from .routes.user import router as user_router
from .routes.post import router as post_router

app = FastAPI()

# Include routes
app.include_router(user_router, prefix="/user")
app.include_router(post_router, prefix="/post")

# Run using uvicorn app.main:app --reload