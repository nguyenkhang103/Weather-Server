from fastapi import Request, FastAPI
import requests
app = FastAPI()

API_KEY = "a5d089453468a09613ea162ff8d4403f"
@app.post("/api/weather")
async def getWeather(request: Request):
  state = await request.json()
  rq = 'https://api.openweathermap.org/data/2.5/weather?q=' + state['query'] + '&units=' + state['units'] +'&APPID=' + API_KEY
  return requests.get(rq).json()
