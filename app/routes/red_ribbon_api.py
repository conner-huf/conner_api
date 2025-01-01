from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.services.red_ribbon_service import RedRibbonService

router = APIRouter()

@router.get("/", response_model=dict)
def welcome():
  return {
    "welcome": "Welcome to the Red Ribbon Backend API. This API is for fetching data from the ribbon backend. This backend accesses data on users and the gifts they want.",
    "valid routes": {
      "/test/{user_id}": "a test endpoint. pass in a user_id to get a message"
    }
  }
  
@router.get("/test/{user_id}")
async def test(user_id: int):
  data = await RedRibbonService.test(user_id)
  if "error" in data:
    raise HTTPException(status_code=404, detail=data["error"])
  return JSONResponse(content=data)