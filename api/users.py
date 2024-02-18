from fastapi import APIRouter, HTTPException, status
from models.user import User
from schemas.user import UserSchemaOut,UserSchemaIn

router = APIRouter()
# Retrive User Details By User Id
#================================================================================================
@router.get("/users/{user_id}", response_model=UserSchemaOut, status_code=status.HTTP_200_OK)
async def get_user(user_id: int):
    user = await User.filter(id=user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

# Create User 
#================================================================================================
@router.post("/users", response_model=UserSchemaOut, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserSchemaIn):
    user = User(username=user_data.username)
    await user.save()
    return user