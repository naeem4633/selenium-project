import time
from pynput import keyboard, mouse
import pyautogui

stop_execution = False
screen_width, screen_height = pyautogui.size()

COVER_LINE="GET RIPPED AT"
ABOUT_TEXT="ABOUT"
collection = [
    {"BRAND_NAME": "BAYSHORE", 
     "FULL_NAME": "BAYSHORE ATHLETIC CLUB"}
     ,
    {"BRAND_NAME": "MYBRAND", 
     "FULL_NAME": "SOME FULL NAME"}
]

def get_initials(string):
    # Split the string into words
    words = string.split()
    
    # Get the first letter of each word
    initials = [word[0].upper() for word in words]
    
    # Join the initials into a single string
    initials_string = ''.join(initials)
    
    return initials_string

def on_press(key):
    global stop_execution
    if key == keyboard.Key.esc:
        # Stop listener
        stop_execution = True
        return False


def main():
    for item in collection:
        design_file(item)
    
def design_file(content):
    BRAND_NAME = content["BRAND_NAME"]
    FULL_NAME = content["FULL_NAME"]
    INITIALS = get_initials(FULL_NAME)

    #move to and change title
    pyautogui.moveTo(950, 110)
    pyautogui.doubleClick()
    pyautogui.typewrite(FULL_NAME)

    #change laptop vie content
    #move to and select cover line
    pyautogui.moveTo(800, 325)
    for _ in range(4):
        pyautogui.doubleClick()
    pyautogui.typewrite(COVER_LINE)
    pyautogui.press('enter')
    pyautogui.typewrite(FULL_NAME if len(FULL_NAME) <= 23 else BRAND_NAME)
    #move to and select the greyed out intitials
    pyautogui.moveTo(850, 550)
    pyautogui.doubleClick()
    pyautogui.typewrite(BRAND_NAME if len(BRAND_NAME) <= 5 else INITIALS)
    #move to and select about section content
    pyautogui.moveTo(762, 557)
    pyautogui.doubleClick()
    pyautogui.typewrite(ABOUT_TEXT)
    pyautogui.moveTo(762, 560)
    pyautogui.click(clicks=3)
    pyautogui.typewrite(FULL_NAME)
    #move to and select initials in membership section
    pyautogui.moveTo(820, 770)
    pyautogui.doubleClick()
    pyautogui.typewrite(BRAND_NAME if len(BRAND_NAME) <= 5 else INITIALS)
    #move to and select full name in footer
    pyautogui.moveTo(760, 967)
    pyautogui.click(clicks=3)
    pyautogui.typewrite(FULL_NAME)


    #click in the middle to disable any active selection
    pyautogui.moveTo(1050, 317)
    pyautogui.doubleClick()


    #change content in phone view
    #move to and select cover line
    pyautogui.moveTo(1140, 317)
    for _ in range(5):
        pyautogui.doubleClick()
    pyautogui.typewrite(COVER_LINE)
    pyautogui.press('enter')
    pyautogui.typewrite(BRAND_NAME)
    #move to and select the greyed out intitials
    pyautogui.moveTo(1140, 500)
    pyautogui.doubleClick()
    pyautogui.typewrite(BRAND_NAME if len(BRAND_NAME) <= 5 else INITIALS)
    #move to and select initials in membership section
    pyautogui.moveTo(1138, 720)
    pyautogui.doubleClick()
    pyautogui.typewrite(BRAND_NAME if len(BRAND_NAME) <= 5 else INITIALS)
    #move to and select full name in footer
    pyautogui.moveTo(1145, 897)
    pyautogui.click(clicks=3)
    pyautogui.typewrite(FULL_NAME)

    pyautogui.moveTo(1050, 317)
    pyautogui.doubleClick()


if __name__ == "__main__":
    main()






























    