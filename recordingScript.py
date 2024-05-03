import time
from pynput import keyboard, mouse
import pyautogui

stop_execution = False
screen_width, screen_height = pyautogui.size()

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

    # Press the ] key to start recording
    # pyautogui.keyDown(']')
    # time.sleep(0.1)
    # pyautogui.keyUp(']')

    #skip the intial screen
    time.sleep(2)
    pyautogui.keyDown('right')
    time.sleep(5)

    # scroll laptop, num9 is scroll down, num8 is scroll up hotkey
    scroll_laptop_view('num9', 'num8')

    # pyautogui.keyDown('right')

    # time.sleep(1)

    # scroll phone, num9 is scroll down, num8 is scroll up hotkey
    # scroll_phone_view('num9', 'num8')

    # Press the [ key to stop recording
    # pyautogui.keyDown('[')
    # time.sleep(0.1)
    # pyautogui.keyUp('[')

    if stop_execution:
        print("Execution stopped.")
        return
    

def scroll_laptop_view(scroll_down_key, scroll_up_key):
    time.sleep(1)

    #start recording
    pyautogui.keyDown(']')
    pyautogui.keyUp(']')

    time.sleep(2)

    # Move mouse cursor inside the phone view in figma
    pyautogui.moveTo(screen_width / 2, screen_height / 2)

    # cover - our programs
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.2)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # our programs - our partners
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.2)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # our partners - our schedule
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.17)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # our schedule - our trainers
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.1)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # our trainers - membership
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.1)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # membership - blog
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.1)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # blog - footer
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.1)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # back to top
    pyautogui.keyDown(scroll_up_key)
    pyautogui.keyUp(scroll_up_key)
    time.sleep(2.5)
    pyautogui.keyDown(scroll_up_key)
    pyautogui.keyUp(scroll_up_key)

    #stop recording
    pyautogui.keyDown('[')
    pyautogui.keyUp('[')


# def scroll_laptop_view_36ms(scroll_down_key, scroll_up_key):
#     time.sleep(1)

#     #start recording99
#     pyautogui.keyDown(']')
#     pyautogui.keyUp(']')

#     time.sleep(2)

#     # Move mouse cursor inside the phone view in figma
#     pyautogui.moveTo(screen_width / 2, screen_height / 2)

#     # cover - our programs
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)
#     time.sleep(0.2)
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)

#     time.sleep(2)

#     # our programs - our partners
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)
#     time.sleep(0.2)
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)

#     time.sleep(2)

#     # our partners - our schedule
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)
#     time.sleep(0.2)
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)

#     time.sleep(2)

#     # our schedule - our trainers
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)
#     time.sleep(0.2)
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)

#     time.sleep(2)

#     # our trainers - membership
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)
#     time.sleep(0.2)
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)

#     time.sleep(2)

#     # membership - blog
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)
#     time.sleep(0.12)
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)

#     time.sleep(2)

#     # blog - footer
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)
#     time.sleep(0.05)
#     pyautogui.keyDown(scroll_down_key)
#     pyautogui.keyUp(scroll_down_key)

#     time.sleep(2)

#     # back to top
#     pyautogui.keyDown(scroll_up_key)
#     pyautogui.keyUp(scroll_up_key)
#     time.sleep(2.5)
#     pyautogui.keyDown(scroll_up_key)
#     pyautogui.keyUp(scroll_up_key)

#     #stop recording
#     pyautogui.keyDown('[')
#     pyautogui.keyUp('[')



def scroll_phone_view(scroll_down_key, scroll_up_key):
    time.sleep(1)

    #start recording
    pyautogui.keyDown(']')
    pyautogui.keyUp(']')

    time.sleep(2)

    # Move mouse cursor inside the laptop view in figma
    pyautogui.moveTo(screen_width / 3, screen_height / 2)

    # cover - our programs
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.05)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # our programs - our partners
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.05)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # our partners - our schedule
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.1)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # our schedule - our trainers
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.1)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # our trainers - membership
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.08)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # membership - blog
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.08)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # blog - footer
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)
    time.sleep(0.1)
    pyautogui.keyDown(scroll_down_key)
    pyautogui.keyUp(scroll_down_key)

    time.sleep(2)

    # back to top
    pyautogui.keyDown(scroll_up_key)
    pyautogui.keyUp(scroll_up_key)
    time.sleep(2)
    pyautogui.keyDown(scroll_up_key)
    pyautogui.keyUp(scroll_up_key)

    #stop recording
    pyautogui.keyDown('[')
    pyautogui.keyUp('[')


if __name__ == "__main__":
    main()






























    