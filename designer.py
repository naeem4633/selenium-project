import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from designerScript import design_file
import pdb
import sys
from dotenv import load_dotenv

os.environ['PATH'] += r"C:/SeleniumDrivers"
load_dotenv()

# Constants
FIGMA_URL = "https://www.figma.com/"
IMPLICIT_WAIT_TIME = 10
FIREFOX_DRIVER_PATH = "./geckodriver.exe"  # Update with your GeckoDriver path

COLLECTION = [
    {"BRAND_NAME": "BAYSHORE", 
     "FULL_NAME": "BAYSHORE ATHLETIC CLUB"}
    #  ,
    # {"BRAND_NAME": "MYBRAND", 
    #  "FULL_NAME": "SOME FULL NAME"}
]

def open_firefox(url):
    # Set up Firefox driver with implicit wait
    driver = webdriver.Firefox()
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)
    driver.get(url)
    driver.maximize_window()
    return driver

def login_user(driver):
    try:
        # Use browser developer tools to find the correct locator for login button
        login_button = driver.find_element(By.CSS_SELECTOR, "a.css-1mtp6jj")
        login_button.click()
        time.sleep(3)  # Short wait for login modal to appear (adjustable)

        driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,'iframe.css-18rrfez'))
        # Find and interact with the email and password fields
        email_field = driver.find_element(By.ID, 'email')
        password_field = driver.find_element(By.ID,'current-password')
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email = os.getenv("FIGMA_LOGIN_EMAIL")
        password = os.getenv("FIGMA_LOGIN_PASSWORD")
        # Input text into the fields
        email_field.send_keys(email)
        password_field.send_keys(password)
        submit_button.click()

        # Switch back to default content
        driver.switch_to.default_content()     
    except NoSuchElementException:
        print("Element not found.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit()

def find_and_open_design_template(driver):
    try:
        # Wait until the element with aria-label "Gym Template (Copy)" opens up
        gym_template_copy = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Gym Template (Copy)']"))
        )
        time.sleep(1)

        # Perform right-click action on the div
        # Example: (for demonstration purposes)
        actions = ActionChains(driver)
        actions.double_click(gym_template_copy).perform()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit()
    
def login_and_design_file(content, driver):
    try:
        login_user(driver)
        find_and_open_design_template(driver)
        # Wait for the deisgn to load
        time.sleep(15)
        design_file(content)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    for content in COLLECTION:
        login_and_design_file(content)

if __name__ == "__main__":
    main()
