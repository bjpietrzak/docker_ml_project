import streamlit as st
import cv2
from PIL import Image
import requests

from dependencies.utils import (encode_img, split_detections,
                                draw_rectangle)
from dependencies.dependencies import servers


def main():
    st.title('Human Detection PAI')

    st.subheader("Image Input")
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
    if image_file is not None:
        st.text("")

        st.subheader("Result")
        img = Image.open(image_file)
        img.save("img.jpg")
        img_cv = cv2.imread("img.jpg")
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)


        bit_img = encode_img(img_cv)
        response = requests.post(servers["inference_server"],
                                files={"Image": bit_img})
        bounding_boxes = response.json()["BoundingBoxes"]

        head, body = split_detections(bounding_boxes)

        draw_img = draw_rectangle(img_cv.copy(), head, (237,222,164))
        draw_img = draw_rectangle(draw_img, body, (212,82,12))

        st.image(draw_img, width=600)
        st.subheader("Sending Result to Database:")
        correct = st.radio(
                "Are bounding boxes in correct places?",
                ('Yes', 'No'))
        if correct == 'Yes':
            image_file
        else:
            image_file = None

if __name__ == '__main__':
    main()