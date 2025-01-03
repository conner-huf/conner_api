from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.services.red_ribbon_service import RedRibbonService
from app.models.red_ribbon import Present

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

# TODO: Implement route for adding an item to a user's wishlist

# TODO: Implement route for deleting an item from a user's wishlist

# TODO: Implement route for updating an item on a user's wishlist

# TODO: Implement a route for creating a new gift group

# TODO: Implement a route for fetching all members in a gift group

# TODO: Implement a route for adding an existing user to a gift group

# TODO: Implement a route for deleting an existing user from a gift group