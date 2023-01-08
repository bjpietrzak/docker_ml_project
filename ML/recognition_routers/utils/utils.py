import cv2
from fastapi import UploadFile
import numpy as np


async def decode_frames(encoded_img):
    encoded_img = await encoded_img.read()
    bit_img = np.frombuffer(encoded_img, np.uint8)
    decoded = cv2.imdecode(bit_img, -1)
    return decoded