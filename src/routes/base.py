from fastapi import APIRouter , FastAPI
import os 
# APIRouter is a class that provides a way to group routes together
router = APIRouter(
  prefix = "/api/v1", 
  tags = ["api/v1"]
)

@router.get("/")
def root():
  app_name = os.getenv("APP_NAME")
  app_version = os.getenv("APP_VERSION")
  return (f"hello {app_name} {app_version}")

@router.get("/health")
def health():
  return ("ok")

@router.get("/version")
def version():
  app_version = os.getenv("APP_VERSION")
  return (f"1.0.0")