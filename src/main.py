# main gate for project 
from fastapi import FastAPI 
from routes import base , data
from helpers.config import Settings

app = FastAPI()

app.include_router(base.router) 
app.include_router(data.data_router)

async def startup_span():
  settings = Settings.get_settings()





