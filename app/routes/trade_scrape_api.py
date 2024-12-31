from fastapi import APIRouter, HTTPException
from app.services.trade_scrape_service import TradeScrapeService

router = APIRouter()

url = 'https://www.capitoltrades.com/politicians/P000197'

@router.get("/", response_model=dict)
def welcome():
  return {
    "welcome": "Welcome to my trades scrape API. This API is for scraping trade data for representatives in congress.",
    "valid routes": {
      "/get_trades_by_person": "Get trades by person"
    }
  }

@router.get("/get_trades_by_person", response_model=dict)
async def get_trades_by_person():
  try:
    trades = await TradeScrapeService.get_trades_by_person(url)
    return {"trades": trades}
  except RuntimeError as e:
    raise HTTPException(status_code=500, detail=f"Service error: {str(e)}")
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")