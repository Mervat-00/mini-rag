from fastapi import APIRouter , FastAPI , Depends 
import os 
from helpers.config import Settings 
# APIRouter is a class that provides a way to group routes together
router = APIRouter(
  prefix = "/api/v1", 
  tags = ["api/v1"]
)

@router.get("/")
def root( app_settings: Settings = Depends(Settings.get_settings)):

  app_name = app_settings.APP_NAME
  app_version = app_settings.APP_VERSION

  return (f"hello {app_name} {app_version}")


  