from fastapi import FastAPI , APIRouter ,UploadFile , Depends
from helpers.config import Settings , get_settings
data_router = APIRouter(
  prefix = "/api/v1/data" , 
  tags = ["api/v1","data"]
)


@data_router.post(f"/upload/{project_id}")
async def upload_file(file: UploadFile , project_id: int , app_settings: Settings = Depends(get_settings) ):
  pass


