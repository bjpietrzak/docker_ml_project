import streamlit as st
import cv2
from PIL import Image
import requests
import os
import redis
import json

from dependencies.utils import (encode_img, split_detections,
                                draw_rectangle, get_name)
from dependencies.dependencies import servers, storage


storage_path = storage["local"]
address, port =  (servers["database_server"]["address"],
                  servers["database_server"]["port"])
rs = redis.Redis(address, port, db=0)

st.subheader("Image Input")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
if image_file is not None:
    st.text("")
    st.subheader("Result")
    img = Image.open(image_file)
    img.save("cache.jpg")
    img = cv2.imread("cache.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    bit_img = encode_img(img)
    response = requests.post(servers["inference_server"],
                             files={"Image": bit_img})

    bounding_boxes = response.json()["BoundingBoxes"]

    if bounding_boxes:
        head, body = split_detections(bounding_boxes)
        img_cv = draw_rectangle(img.copy(), head, (237,222,164))
        img_cv = draw_rectangle(img_cv, body, (212,82,12))
        st.image(img_cv, width=600)

        name = get_name()
        rs.set(name, json.dumps(bounding_boxes))
        save_path = os.path.join(storage_path,name)[1:]
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(save_path, img)
    else:
        st.text("Person was not found")
        st.image(img, width=600)


