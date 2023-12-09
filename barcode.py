import cv2
print(cv2.__version__)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import json
# import random
from scipy import stats
def cv_imread(filePath):
    cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), cv2.IMREAD_COLOR)
    return cv_img
# import threading
# import keyboard
# import time
import pyzbar.pyzbar as pyzbar
import pyzbar.pyzbar as pyzbar
from flask import jsonify

def barcode(picture):
    tt = 0
    # img = cv_imread(r'barcode_folder\\test3.jpg')
    # img = cv_imread(picture)
    img = np.array(picture.split(",")).astype(int).reshape((480,640,4))[:,:,0:3]
    # img = np.array(picture.split(",")).astype(int).reshape((-1,4))
    img = np.float32(img)
    # cv2.imwrite('pic/test.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 80])  # 存成 jpg
    print(img.shape)
    # print(img)
    # img = cv2.resize(img, (0,0), fx = mag, fy = mag) #放大圖片
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #轉灰
    print(img)
    texts = pyzbar.decode(img)
    for text in texts:
        if text.data.decode("utf-8"):
            tt = text.data.decode("utf-8")
    print(tt)
    # return jsonify({"barcode":tt})

    return tt

    # tt = 0
    # img = cv_imread(r'barcode_folder\\test3.jpg')
    # # img = cv2.resize(img, (0,0), fx = mag, fy = mag) #放大圖片
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #轉灰
    # texts = pyzbar.decode(img)
    # for text in texts:
    #     if text.data.decode("utf-8"):
    #         tt = text.data.decode("utf-8")
    # print(tt)