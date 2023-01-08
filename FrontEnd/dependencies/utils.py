import cv2
import numpy as np

def test_device() -> bool:
    cap = cv2.VideoCapture(0)
    cam_avalible = cap.isOpened()
    cap.release()
    return cam_avalible

def encode_img(img):
    _, encoded = cv2.imencode('.jpg', img)
    bit_img = encoded.tobytes()
    return bit_img

def split_detections(detections):
    head, body = [], []
    for i in range(len(detections)):
        if detections[i][-1] == 1:
            head.append(detections[i])
        else:
            body.append(detections[i])
    return head, body

def draw_rectangle(img, detections, color) -> np.ndarray:
    for i in range(len(detections)):
        x1,y1,x2,y2 = detections[i][:4]
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
    return img
