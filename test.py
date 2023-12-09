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

cap = cv2.VideoCapture(0)
play = 1
print(1)
while cap.isOpened():
    if play:
        ret, frame = cap.read()  #回傳取得是否成功(boolin), 下一張圖片
        if ret:
            cv2.imshow('video', frame)
            bar = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #轉灰
            barcode = pyzbar.decode(bar)
            for text in barcode:
                if text.data.decode("utf-8"):
                    tt = text.data.decode("utf-8")
                    play = play ^ 1
                    print(frame)
                    print(tt)
        else: break
        
    #影片操作
    key = cv2.waitKey(1)
    if key == -1:
        continue
    elif key == ord('q') or key == 27: # Esc
        print('break')
        break
    elif key == 13: # Enter
        print('play / pause')
        play = play ^ 1
cap.release()
cv2.destroyWindow('video')