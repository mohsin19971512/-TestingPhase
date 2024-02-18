from fastapi import APIRouter, HTTPException
import math

router = APIRouter()


#-Retreive The Square root Of The Number By Query Param
#================================================================================================
@router.get("/square-root")
async def calculate_square_root(number: int):
    if number < 10 or number > 100:
        raise HTTPException(status_code=400, detail="Number must be within the range 10 to 100")
    return {"square_root": math.sqrt(number)}
