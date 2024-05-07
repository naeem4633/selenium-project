import time
from pynput import keyboard, mouse
import pyautogui

stop_execution = False
screen_width, screen_height = pyautogui.size()

LINE_1="GET BURNED WITH"
LINE_2 ="BAYSHORE"
LINE_3="BAC"
LINE_4="ABOUT"
LINE_5="BAYSHORE ATHLETIC CLUB"
LINE_6="BAC"
LINE_7="BAYSHORE ATHLETIC CLUB"

LINE_1_MOBILE="GET BURNED WITH"
LINE_2_MOBILE ="BAYSHORE"
LINE_3_MOBILE="BAC"
LINE_4_MOBILE="BAC"
LINE_5_MOBILE="BAYSHORE ATHLETIC CLUB"

def on_press(key):
    global stop_execution
    if key == keyboard.Key.esc:
        # Stop listener
        stop_execution = True
        return False


def main():
    # Setting up the listener for the Escape key
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    design_file()

    if stop_execution:
        print("Execution stopped.")
        return
    
def design_file():
    time.sleep(1)
    pyautogui.moveTo(800, 325)
    for _ in range(4):
        pyautogui.doubleClick()
    pyautogui.typewrite(LINE_1)
    pyautogui.press('enter')
    pyautogui.typewrite(LINE_2)
    pyautogui.moveTo(850, 550)
    pyautogui.doubleClick()
    pyautogui.typewrite(LINE_3)
    pyautogui.moveTo(762, 557)
    pyautogui.doubleClick()
    pyautogui.typewrite(LINE_4)
    pyautogui.moveTo(762, 560)
    pyautogui.click(clicks=3)
    pyautogui.typewrite(LINE_5)
    pyautogui.moveTo(820, 770)
    pyautogui.doubleClick()
    pyautogui.typewrite(LINE_6)
    pyautogui.moveTo(760, 967)
    pyautogui.click(clicks=3)
    pyautogui.typewrite(LINE_7)

    pyautogui.moveTo(1050, 317)
    pyautogui.doubleClick()

    pyautogui.moveTo(1140, 317)
    for _ in range(5):
        pyautogui.doubleClick()
    pyautogui.typewrite(LINE_1_MOBILE)
    pyautogui.press('enter')
    pyautogui.typewrite(LINE_2_MOBILE)
    pyautogui.moveTo(1140, 500)
    pyautogui.doubleClick()
    pyautogui.typewrite(LINE_3_MOBILE)
    pyautogui.moveTo(1138, 720)
    pyautogui.doubleClick()
    pyautogui.typewrite(LINE_4_MOBILE)
    pyautogui.moveTo(1145, 897)
    pyautogui.click(clicks=3)
    pyautogui.typewrite(LINE_5_MOBILE)

    pyautogui.moveTo(1050, 317)
    pyautogui.doubleClick()

if __name__ == "__main__":
    main()






























    