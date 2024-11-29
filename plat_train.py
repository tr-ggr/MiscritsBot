import pyautogui as pg
import time
import keyboard
import pyscreeze as ps
import random
import pywinauto
from enum import Enum

app = pywinauto.Application().connect(path='Miscrits_Client.exe')

sleep_time = 1

class state(Enum):
    SEARCHING = 1
    BATTLE = 2
    TRAINING = 3

def humanizer():
    return time.sleep(random.uniform(1, 3))

# Attributes
state = state.SEARCHING
ready_to_train = True
    
def locate_object(target):
    try:
        pos = ps.locateOnScreen(f"./targets/{target}.png", confidence=0.9)
        print(f"Located {target} on Screen!")
        pg.moveTo(pos[0]+20, pos[1]+20)
        pg.leftClick()
        humanizer()

        return True
    except:
        print(f"Not Found {target} on Screen!")
        humanizer()
        return False
    
def plat_train():
    # Check if ready to train
    if locate_object("ready_train_button") == True:
        print("Ready to Train!")
        humanizer()

    if locate_object("ready_xp") == True:
        print("Ready to XP!")
        humanizer()

    if locate_object("train_now_button") == True:
        print("Available to Train!")
        humanizer()

    if locate_object("train_plat_button") == True:
        print("Available to Train!")
        humanizer()

    if locate_object("continue_button") == True:
        print("Training Now!")
        humanizer()

    if locate_object("continue_learned") == True:
        print("Learned new move!")
        humanizer()

    if locate_object("continue_evolved") == True:
        print("Learned new move!")
        humanizer()

    if locate_object("skip_button_level_up") == True:
        print("Level Up!")
        humanizer()
            

    if locate_object("continue_learned") == True:
        print("Learned new move!")
        humanizer()

    if locate_object("continue_evolved") == True:
        print("Learned new move!")
        humanizer()

    if locate_object("skip_button_level_up") == True:
        print("Level Up!")
        humanizer()

    if locate_object("x_button") == True:
        print("Exiting Training!")
        
        humanizer()
    
    print("Done Training!")

while True:
    if ready_to_train == True:
        plat_train()
        ready_to_train = False

    
