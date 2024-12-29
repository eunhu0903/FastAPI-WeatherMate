import requests
from fastapi import APIRouter, HTTPException
import os

router = APIRouter()

API_KEY = os.getenv("WEATHER_API_KEY")  # .env 파일에서 API 키를 불러옴

@router.get("/weather")
def get_weather(city: str):
    lang = 'kr'  # 한국어로 결과를 요청
    units = 'metric'  # 섭씨 온도로 반환
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},kr&appid={API_KEY}&lang={lang}&units={units}"
    
    # API 요청
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # 필요한 날씨 데이터만 추출
        temperature = data['main']['temp']  # 현재 기온
        temp_min = data['main']['temp_min']  # 최저 기온
        temp_max = data['main']['temp_max']  # 최고 기온
        humidity = data['main']['humidity']  # 습도
        description = data['weather'][0]['description']  # 날씨 설명
        clouds = data['clouds']['all']  # 구름 비율
        
        # 필요한 정보만 포함하여 반환
        return {
            "city": city,
            "temperature": temperature,
            "temp_min": temp_min,
            "temp_max": temp_max,
            "humidity": humidity,
            "weather": description,
            "clouds": clouds
        }
    else:
        raise HTTPException(status_code=404, detail="Error fetching weather data.")
