import os
import sys
import shutil
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
from screenColorCheck import detect_screen_color, black_screen_detected, white_screen_detected, black_screen_detected_small_area
import pyautogui

os.environ['PATH'] += r"C:/SeleniumDrivers"

# Constants[]
WEBSITE_URLS = [
"https://www.figma.com/file/p8fFwlKKzz40HiAvCJFsa9/Valhalla-Training-Grounds?type=design&node-id=34-976&mode=design&t=f7RRP1Jb7rk0YGhO-0"
]

OBS_VIDEOS_FOLDER = r"C:\Users\ahmed\OneDrive\Desktop\OBSVids"
AUTOSCROLL_EXE_PATH = "./AutoScroll.exe"

IMPLICIT_WAIT_TIME = 10  # Set implicit wait time to 10 seconds

def open_firefox(url):
    # Set up Firefox driver with implicit wait
    driver = webdriver.Firefox()
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)
    driver.get(url)
    driver.maximize_window()
    return driver

def click_toolbar_button(driver):
    try:
        # Explicitly wait for the toolbar button to appear
        toolbar_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "toolbar_styles--flyoutButton--lyOUg"))
        )
        # Once toolbar button is located, click it
        toolbar_button.click()
    except:
        print("Error: Toolbar button not found. Exiting...")
        sys.exit(1)

def run_recording_script(driver):
    # Delete previous screenshots if they exist
    if os.path.exists("screenshot.png"):
        os.remove("screenshot.png")
    if os.path.exists("screenshot2.png"):
        os.remove("screenshot2.png")
    if os.path.exists("screenshot3.png"):
        os.remove("screenshot3.png")

    driver.switch_to.window(driver.window_handles[-1])
    
    try:
        # Wait for canvas element to appear in the current tab or switch to the new tab
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "prototype--viewer--uYMkg"))
        )
    except:
        print("Preview not found, waiting 15 seconds then starting the recording...")
        #wait some more time
        time.sleep(15)
        driver.save_screenshot("screenshot.png")
        if black_screen_detected("screenshot.png"):
            print("black screen detected")
            driver.refresh()
            time.sleep(20)
            print("black screen possibly resolved, resuming recording")
        elif white_screen_detected("screenshot.png"):
            print("white screen detected, waiting 20 seconds")
            time.sleep(20)
            driver.save_screenshot("screenshot2.png")
            if black_screen_detected("screenshot2.png"):
                driver.refresh()
                time.sleep(20)

    time.sleep(5)
    
    # Go to the laptop preview section and start the recording
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width / 2, screen_height / 2)
    time.sleep(2)
    pyautogui.press('right')
    driver.save_screenshot("screenshot3.png")
    if black_screen_detected_small_area("screenshot3.png"):
        print('black screen detected')
        pyautogui.press('left')

    # Run recordingScript.py
    process = subprocess.Popen(["python", "recordingScript.py"])
    # Wait for the process to finish
    process.wait()


def close_window(driver):
    # Close the entire browser window
    driver.quit()

def rename_recent_file(url):
    try:
        # List all files in the OBS videos folder
        files = os.listdir(OBS_VIDEOS_FOLDER)
        
        # Filter out directories and get the most recent file
        files = [f for f in files if os.path.isfile(os.path.join(OBS_VIDEOS_FOLDER, f))]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(OBS_VIDEOS_FOLDER, x)), reverse=True)
        
        if files:
            most_recent_file = files[0]
            
            # Extract relevant words from the URL
            words = re.search(r'\/([^\/]+)\?', url).group(1)
            new_filename = os.path.join(OBS_VIDEOS_FOLDER, f"{words}.mp4")
            
            shutil.move(os.path.join(OBS_VIDEOS_FOLDER, most_recent_file), new_filename)
            print(f"Renamed {most_recent_file} to {new_filename}")
        else:
            print("No files found in OBS videos folder.")
    except FileNotFoundError:
        print("OBS videos folder not found.")


def main():
    subprocess.Popen([AUTOSCROLL_EXE_PATH])
    for url in WEBSITE_URLS:
        driver = open_firefox(url)
        click_toolbar_button(driver)
        run_recording_script(driver)
        close_window(driver)
        rename_recent_file(url)

if __name__ == "__main__":
    main()
