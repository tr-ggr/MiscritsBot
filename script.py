import pyautogui as pg
import time
import random
from enum import Enum
from enemy_search import check_enemy_miscrit

# Class
class state(Enum):
    SEARCHING = 1
    BATTLE = 2
    TRAINING = 3

class train(Enum):
    PLAT = 1
    FARM = 2

# Attributes

search_targets = [
    "mountain_gem1",
    "mountain_gem2"
]

battle_targets = [
    "drilldent",
    "mumbah"
]

sleep_time = 1

current_state = state.SEARCHING

attack_to_use = "shooting_spawn_button"

is_training_ready = False

training_mode = train.FARM


# Functions
def humanizer():
    return time.sleep(random.uniform(1, 3))

def locate(target):
    try:
        pos = pg.locateOnScreen(f"./targets/{target}.png", confidence=0.7)
        print(f"Located {target} on Screen!")
        pg.moveTo(pos[0]+20, pos[1]+20)

        return True
    except:
        print(f"Not Found {target} on Screen!")
        humanizer()
        return False
    
def locate_and_click(target):
    if locate(target) == True:
        pg.leftClick()
        humanizer()
        return True
    else:
        return False

def check_state():
    global current_state
    if is_training_ready:
        current_state = state.TRAINING
    elif locate(attack_to_use) == True:
        current_state = state.BATTLE
    else:
        current_state = state.SEARCHING


# Main Loop
while True:
    # Check state first
    check_state()
    print(f"Current State: {current_state}")
    

    # Search state
    if current_state == state.SEARCHING:
        # Clean up first before checks
        while locate_and_click("gold_drop") == True:
            print("Gold Drop Found!")
            pass

        for target in search_targets:
            locate_and_click(target)
            humanizer()

            check_state()
            if current_state != state.SEARCHING:
                break
        

    # Battle state
    elif current_state == state.BATTLE:
        time.sleep(1)
        # Check the target before attacking
        target, is_target = check_enemy_miscrit(battle_targets)

        if target == False:
            print("No target found!")
        if is_target == False:
            print(f"{target} is not on your list!")
        else:
            print(f"{target} found!")

        # Attack the target
        while locate_and_click(attack_to_use) == True:
            print("Attacking!")
            humanizer()

            time.sleep(1)

        time.sleep(1)

        # Check if miscrits are ready to train
        if locate("victory_screen_ready_xp") == True:
            print("Miscrits are ready to train!")
            is_training_ready = True
            humanizer()

        if locate_and_click("close_button") == True:
            print("Victory!")
            humanizer()


    # Training state
    elif current_state == state.TRAINING:
        if locate_and_click("ready_train_button") == True:
            print("Ready to Train!")
            humanizer()

        while locate_and_click("ready_xp") == True:
            humanizer()

            if locate_and_click("train_now_button") == True:
                print("Trained Miscrit!")
                humanizer()

            if training_mode == train.PLAT and locate_and_click("train_plat_button") == True:
                print("Plat Trained!")
                humanizer()

            if locate_and_click("continue_button") == True:
                humanizer()

            if locate("continue_learned") == True:
                if locate_and_click("continue_learned") == True:
                    print("Learned new move!")
                    humanizer()

                if locate_and_click("continue_evolved") == True:
                    print("Evolved miscrits!")
                    humanizer()

                if locate_and_click("skip_button_level_up") == True:
                    humanizer()
                

        
        print("Last checks before exiting training!")
        if locate("continue_learned") == True:

            if locate_and_click("continue_learned") == True:
                humanizer()

            if locate_and_click("continue_evolved") == True:
                humanizer()

            if locate_and_click("skip_button_level_up") == True:
                humanizer()

        if locate_and_click("x_button") == True:
            print("Exiting Training!")
            humanizer()
        
        print("Done Training!")
        is_training_ready = False