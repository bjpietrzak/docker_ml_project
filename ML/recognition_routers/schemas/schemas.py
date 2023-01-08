from pydantic import BaseModel
from fastapi import UploadFile, File
from typing import List


class DetectionRequest(BaseModel):
    Image: UploadFile = File(...)

class DetectionResponse(BaseModel):
    BoundingBoxes: List
