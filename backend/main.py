import io
from typing import List

import cv2
import numpy as np
import mediapipe as mp
from fastapi import FastAPI, Request, File, UploadFile

import hand

app = FastAPI()


recognizer = hand.GestureRecognizer(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
)


@app.get("/api")
async def root(request: Request):
    print(request.headers)
    return {"message": "Hello World"}


def read_image(bin_data, size=(1280, 720)):
    file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # img = cv2.resize(img, size)
    return img


@app.post("/api/hand-gesture")
async def hand_gesture(file: UploadFile = File(...)):
    bin_data = io.BytesIO(file.file.read())
    img = read_image(bin_data)
    np_array = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np_array)
    recognizer.model.recognize_async(mp_image, recognizer.timestamp)
    recognizer.timestamp += 1
    print("gestures:", recognizer.get_gestures())
    return {"gestures": recognizer.get_gestures()}
