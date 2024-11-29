import pyautogui as pg
import time
import keyboard
import pyscreeze as ps
import random
import cv2
import numpy as np
from enum import Enum
import re
import easyocr

reader = easyocr.Reader(['en']) # specify the language 

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

def check_if_target(miscrit, targets):
    for i in targets:
        if strcmp(i, miscrit):
            return True
    return False

targets = ["cubsprout", "sparkspeck"]

def locate(target):
    try:
        pos = ps.locateOnScreen(f"./targets/{target}.png", confidence=0.7)
        print(f"Located {target} on Screen!")

        return pos
    except:
        print(f"Not Found {target} on Screen!")
        time.sleep(1)
        return False


def check_enemy_miscrit(targets):
    try:
        if locate("easy_text") == False:
            if locate("hard_text") == False:
                pos = locate("normal_text")
            else:
                pos = locate("hard_text")
        else:
            pos = locate("easy_text")

        image = pg.screenshot(region=(int(pos[0]), int(pos[1]+20), 87, 24))
    
        image.save("otin.png")
        result = reader.readtext("otin.png")

        # for (bbox, text, prob) in result:
        #     print(f'Text: {text}, Probability: {prob}')

        
        bbox, text, prob = result[0]

        time.sleep(1)
        return (text, check_if_target(text, targets))

    except Exception as e:
        print(e)
        print("No image found")
        time.sleep(1)
        return (False, False)
    
# while True:
#     check_enemy_miscrit(targets)
    
