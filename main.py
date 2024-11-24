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
ready_to_train = False
    
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

while True:
    if keyboard.is_pressed("q"):
        print("Pressed Q")
        break

    # Search Area Logic
    if locate_object("mansion_cabinet") == False:
        print("Searching for Leaves")
        screen_size = app['Miscrits (DEBUG)'].rectangle()
        # app['Miscrits (DEBUG)'].click_input(coords=(screen_size.width()//2 + random.randint(-150, 150), screen_size.height()//2 + random.randint(-150, 150)))
    else:
        time.sleep(sleep_time)

    # if locate_object("mansion_statue1") == False:
    #     print("Searching for Shrug")
    #     screen_size = app['Miscrits (DEBUG)'].rectangle()
    #     # app['Miscrits (DEBUG)'].click_input(coords=(screen_size.width()//2 + random.randint(-150, 150), screen_size.height()//2 + random.randint(-150, 150)))
    # else:
    #     time.sleep(sleep_time)

    if locate_object("mansion_box") == False:
        print("Searching for Shrug")
        screen_size = app['Miscrits (DEBUG)'].rectangle()
        # app['Miscrits (DEBUG)'].click_input(coords=(screen_size.width()//2 + random.randint(-150, 150), screen_size.height()//2 + random.randint(-150, 150)))
    else:
        time.sleep(sleep_time)

    # print("Found Area!")
    humanizer()
        
    # Battle Screen Logic
    if locate_object("shooting_spawn_button") == False:
        print("Not on Battle Screen!")
    else:
        while locate_object("shooting_spawn_button") == True:
            print("On Battle Screen!")
            humanizer()
            time.sleep(sleep_time)

            if locate_object("victory_screen_ready_xp") == True:
                ready_to_train = True
                humanizer()

    if locate_object("victory_screen_ready_xp") == True:
        ready_to_train = True
        humanizer()

    if locate_object("close_button") == True:
        print("Victory!")
        humanizer()

    if ready_to_train == True:
        # Check if ready to train
        if locate_object("ready_train_button") == True:
            print("Ready to Train!")
            humanizer()

        while locate_object("ready_xp") == True:
            print("Ready to XP!")
            humanizer()

            if locate_object("train_now_button") == True:
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
        ready_to_train = False

    
