from fastapi import APIRouter, Query, HTTPException, status
from models.post import Post
from schemas.post import PostSchemaOut,PostSchemaIn
from typing import List
router = APIRouter()

#-Retreive List Of Filter Posts By Category and Auther
#===========================================================================================
@router.get("/posts", response_model=List[PostSchemaOut], status_code=status.HTTP_200_OK)
async def get_posts(author: str , category: str ):
    query_params = {}
    if author:
        query_params['author__username'] = author
    if category:
        query_params['category'] = category

    posts = await Post.filter(**query_params).prefetch_related('author').values('id', 'title', 'content', 'category','author__username')
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No posts found")

    return posts

#-Create Post
#===========================================================================================
@router.post("/posts", response_model=PostSchemaOut, status_code=status.HTTP_201_CREATED)
async def create_post(post_data: PostSchemaIn):
    try:
        
        post = await Post.create(**post_data.model_dump())
        return post
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
