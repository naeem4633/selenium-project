import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess

os.environ['PATH'] += r"C:/Seleniumrivers"

# Constants[]
WEBSITE_URLS = [
    "https://www.figma.com/file/2Gu4rDpUogRxb1SG8yUzcI/STRONG-INC.?type=design&mode=design&t=AuaebCPYdd4yHuLu-0",
    "https://www.figma.com/file/nxOzlZOMd8scMs2zTnC7Al/Guruz-Fitness-Studio?type=design&t=LhsuJq8dWJlr8n9b-6",
    "https://www.figma.com/file/2GwPX0GDscubAait4VnfWQ/Gluckstadt-Fitness?type=design&t=LhsuJq8dWJlr8n9b-699"
]

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

# def run_recording_script(driver):
#     # try:
#     #     # Wait for canvas element to appear in the current tab or switch to the new tab
#     #     WebDriverWait(driver, 15).until(
#     #         EC.presence_of_element_located((By.CLASS_NAME, "prototype--viewer--uYMkg"))
#     #     )
#     # except:
#     #     try:
#     #         print("Preview not found, retrying...")
#     #         # Switch to the new tab
#     #         driver.switch_to.window(driver.window_handles[-1])
#     #         # Refresh the new tab
#     #         driver.refresh()
#     #         # Wait for canvas element to appear in the new tab
#     #         WebDriverWait(driver, 20).until(
#     #             EC.presence_of_element_located((By.CLASS_NAME, "prototype--viewer--uYMkg"))
#     #         )
#     #     except:
#     #         # If canvas element still doesn't appear after second attempt, display error and exit
#     #         print("Error: Canvas element did not appear after two attempts. Recording script cannot be run. Exiting...")
#     #         sys.exit(1)

#     try:
#         # Wait for canvas element to appear in the current tab or switch to the new tab9
#         WebDriverWait(driver, 15).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "prototype--viewer--uYMkg"))
#         )
#     except:
#         print("Preview not found, waiting 15 seconds then starting the recording...")
#         #wait some more time
#         time.sleep(15)

#     # Run recordingScript.py
#     process = subprocess.Popen(["python", "recordingScript.py"])
#     # Wait for the process to finish
#     process.wait()

def run_recording_script(driver):
    try:
        # Wait for canvas element to appear in the current tab or switch to the new tab9
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "prototype--viewer--uYMkg"))
        )
    except:
        print("Preview not found, waiting 15 seconds then starting the recording...")
        #wait some more time
        time.sleep(15)

        if not EC.presence_of_element_located((By.CLASS_NAME, "header--titleWithCaret--iNOEc")):
            driver.switch_to.window(driver.window_handles[-1])
            driver.refresh()
            time.sleep(20)
            if not EC.presence_of_element_located((By.CLASS_NAME, "header--titleWithCaret--iNOEc")):
                print("Black screen, exiting the process")
                sys.exit(1)

    # Run recordingScript.py
    process = subprocess.Popen(["python", "recordingScript.py"])
    # Wait for the process to finish
    process.wait()


def close_window(driver):
    # Close the entire browser window
    driver.quit()

def main():
    for url in WEBSITE_URLS:
        driver = open_firefox(url)
        click_toolbar_button(driver)
        run_recording_script(driver)
        close_window(driver)

if __name__ == "__main__":
    main()
