from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.services.red_ribbon_service import RedRibbonService

router = APIRouter()

@router.get("/", response_model=dict)
def welcome():
  return {
    "welcome": "Welcome to the Red Ribbon Backend API. This API is for fetching data from the ribbon backend. This backend accesses data on users and the gifts they want.",
    "valid routes": {
      "/user/{user_id}": "Get info for a user by user_id (test user = 6776c071bb7f0ba5bd3732ff)",
      "/user/{user_id}/wishlist": "Get wishlist for a user by user_id (test user = 6776c071bb7f0ba5bd3732ff)"
    }
  }

@router.get("/user/{user_id}")
async def get_user_info(user_id: str):
  data = await RedRibbonService.get_user_info(user_id)
  if "error" in data:
    raise HTTPException(status_code=404, detail=data["error"])
  return JSONResponse(content=data)

@router.get("/user/{user_id}/wishlist")
async def get_wishlist(user_id: str):
  data = await RedRibbonService.get_user_wishlist(user_id)
  if "error" in data:
    raise HTTPException(status_code=404, detail=data["error"])
  return JSONResponse(content=data)