from fastapi import APIRouter, Depends, UploadFile
from asyncio import create_task
import cv2
import numpy as np

from .schemas.schemas import DetectionRequest, DetectionResponse
from .utils.utils import decode_frames
from .utils.recognition_model import model


router = APIRouter(prefix="/inference-service",
                   tags=["Inference Operations"])

@router.post("/detect/", response_model=DetectionResponse)
async def detect(request: DetectionRequest = Depends()):
    img = await(create_task(decode_frames(encoded_img=request.Image)))
    boxes = model(img)[0].cpu().detach().numpy().tolist()
    response = DetectionResponse(BoundingBoxes=boxes)
    return response