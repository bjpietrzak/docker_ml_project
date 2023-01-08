from fastapi import FastAPI
from recognition_routers.inference_service import router


app = FastAPI()
app.include_router(router)