from fastapi import APIRouter
from api.square_root import router as square_root_router
from api.users import router as users_router
from api.posts import router as posts_router

def include_routers(app):
    app.include_router(square_root_router, prefix="/square-root", tags=["square-root"])
    app.include_router(users_router, prefix="/users", tags=["users"])
    app.include_router(posts_router, prefix="/posts", tags=["posts"])
 