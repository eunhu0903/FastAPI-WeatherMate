from fastapi import APIRouter, HTTPException
from core.weather import get_weather  # weather.py에서 날씨 API 로직 import

router = APIRouter()

# 사용자에게 도시 이름을 입력받아 날씨 정보 출력
@router.get("/weather/{city}", tags=["Weather"])
def get_city_weather(city: str):
    try:
        weather_data = get_weather(city)
        return {"message": weather_data}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
