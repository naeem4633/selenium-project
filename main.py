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
from designer import login_user, find_and_open_design_template
from designerScript import design_file

os.environ['PATH'] += r"C:/SeleniumDrivers"

# Constants[]
WEBSITE_URLS = [
"https://www.figma.com/file/7bPoQKRpi9DjjTjk7CdRo4/Disciples-of-Strength?type=design&node-id=0-1&mode=design&t=grFPj7E9GsnrAVXI-0",
]
CONTENT_COLLECTION = [
    {"BRAND_NAME": "BAYSHORE", 
     "FULL_NAME": "BAYSHORE ATHLETIC CLUB"}
    #  ,
    # {"BRAND_NAME": "MYBRAND", 
    #  "FULL_NAME": "SOME FULL NAME"}
]

OBS_VIDEOS_FOLDER = r"C:\Users\ahmed\OneDrive\Desktop\OBSVids"
AUTOSCROLL_EXE_PATH = "./AutoScroll.exe"
FIGMA_URL = "https://www.figma.com/"

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
        # Explicitly wait for the play button to appear
        toolbar_button = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "toolbar_styles--flyoutButton--lyOUg"))
        )
        # Once toolbar button is located, click it
        toolbar_button.click()
    except:
        print("Error: Toolbar button not found. Exiting...")
        sys.exit(1)

def manually_click_toolbar_button():
    pyautogui.moveTo(1825, 100)
    pyautogui.doubleClick()

def run_recording_script(driver):
    # Delete previous screenshots if they exist
    if os.path.exists("screenshot.png"):
        os.remove("screenshot.png")
    if os.path.exists("screenshot2.png"):
        os.remove("screenshot2.png")
    if os.path.exists("screenshot3.png"):
        os.remove("screenshot3.png")
    
    #switch to the new window (preview window)
    driver.switch_to.window(driver.window_handles[-1])
    
    try:
        # Wait for canvas element to appear in the current tab or switch to the new tab
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "prototype--viewer--uYMkg"))
        )
    except:
        print("Canvas which contains the preview not found, waiting 15 seconds then starting the recording...")
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

    time.sleep(7)
    
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

def get_and_print_current_url(driver):
    current_url = driver.current_url
    return current_url

def open_new_tab_and_close_previous(driver, url):
    # Open a new tab using JavaScript
    driver.execute_script("window.open('{}', '_blank');".format(url))

    driver.close()
    
    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[-1])

def rename_recent_file_from_url(url):
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

def rename_recent_file(name):
    try:
        # List all files in the OBS videos folder
        files = os.listdir(OBS_VIDEOS_FOLDER)
        
        # Filter out directories and get the most recent file
        files = [f for f in files if os.path.isfile(os.path.join(OBS_VIDEOS_FOLDER, f))]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(OBS_VIDEOS_FOLDER, x)), reverse=True)
        
        if files:
            most_recent_file = files[0]
            
            new_filename = os.path.join(OBS_VIDEOS_FOLDER, f"{name}.mp4")
            
            shutil.move(os.path.join(OBS_VIDEOS_FOLDER, most_recent_file), new_filename)
            print(f"Renamed {most_recent_file} to {new_filename}")
        else:
            print("No files found in OBS videos folder.")
    except FileNotFoundError:
        print("OBS videos folder not found.")


def record_from_figma_links(design_urls):
    for url in design_urls:
        driver = open_firefox(url)
        click_toolbar_button(driver)
        run_recording_script(driver)
        close_window(driver)
        rename_recent_file_from_url(url)

def design_and_record(content_collection):
    print("Ensure that Caps Lock is off")
    print("Ensure that recorder is running")
    driver = open_firefox(FIGMA_URL)
    login_user(driver)
    time.sleep(5)
    for content in content_collection:
        open_new_tab_and_close_previous(driver, FIGMA_URL)
        find_and_open_design_template(driver)
        time.sleep(15)
        design_file(content)
        print(f"URL for {content["FULL_NAME"]} : {get_and_print_current_url(driver)}")
        manually_click_toolbar_button()
        time.sleep(10)
        run_recording_script(driver)
        rename_recent_file(content["FULL_NAME"])
    # close_window(driver)

def main():
    try:
        subprocess.Popen([AUTOSCROLL_EXE_PATH])
        # record_from_figma_links(WEBSITE_URLS)
        design_and_record(CONTENT_COLLECTION)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
