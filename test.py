import pyautogui as pg
import time
import keyboard
import pyscreeze as ps
import random
import pywinauto
import pytesseract as ts
import cv2
import numpy as np
from enum import Enum
import re

# print(ts.image_to_string(image="name_test.png"))
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def remove_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)

def strcmp(a, b):
    a = a.lower()
    b = b.lower()
    ctr = 0
    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        if a[i] != b[i]:
            ctr += 1

    if ctr > 2:
        return False
    return True

def check_if_target(miscrit):
    for i in targets:
        if strcmp(i, miscrit):
            return True
    return False

targets = ["cubsprout", "sparkspeck"]


while True:
    try:
        pos = pg.locateOnScreen("./targets/right_battle_miscrits.png", confidence=0.6)
        # print(pos)
        # if pos:
        image = pg.screenshot(region=(int(pos[0]+48), int(pos[1]+30), 87, 24))
    
        image = remove_noise(np.array(image))
        image = get_grayscale(image)
        image = thresholding(image)
        cv2.imwrite("otin.png", image)
        miscrit = ts.image_to_string(image=image)
        miscrit = miscrit.strip()

        # Use regex to extract only words
        words = re.findall(r'\b\w+\b', miscrit)
        words = ' '.join(words)

        print(f"{words} is {check_if_target(words)}")

    except:
        print("No image found")
        time.sleep(1)
#     # time.sleep(1)  # Add a delay to avoid excessive CPU usage
