import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pdb

os.environ['PATH'] += r"C:/SeleniumDrivers"

# Constants
FIGMA_URL = "https://www.figma.com/"
IMPLICIT_WAIT_TIME = 10
FIREFOX_DRIVER_PATH = "./geckodriver.exe"  # Update with your GeckoDriver path

def open_firefox(url):
    # Set up Firefox driver with implicit wait
    driver = webdriver.Firefox()
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)
    driver.get(url)
    driver.maximize_window()
    return driver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# def user_login(driver):
#     try:
#         login_button = driver.find_element(By.CSS_SELECTOR, "a.css-1mtp6jj")
#         login_button.click()
#         time.sleep(5)  # Wait for the login modal to appear

#         # Wait for email input field to be present
#         email_input = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "email"))
#         )

#         # Enter email
#         email_input.send_keys("rockypaul377@gmail.com")

#         # Enter password
#         password_input = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "current-password"))
#         )
#         password_input.send_keys("aaabbbcc")

#         # Click submit button
#         submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#         submit_button.click()
#     except NoSuchElementException:
#         print("Element not found.")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# def login_user(driver):
#     try:
#         # Click login button
#         login_button = driver.find_element(By.CSS_SELECTOR, "a.css-1mtp6jj")
#         login_button.click()
#         time.sleep(5)

#         # Wait for auth form to appear
#         auth_form = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "form.auth_iframe_app_view--authViewCenter--ZC-Y9"))
#         )

#         # Enter email
#         email_input = auth_form.find_element(By.ID, "email")
#         email_input.send_keys("rockypaul377@gmail.com")

#         # Enter password
#         password_input = auth_form.find_element(By.ID, "current-password")
#         password_input.send_keys("aaabbbcc")

#         # Click submit button
#         submit_button = auth_form.find_element(By.CSS_SELECTOR, "button[type='submit']")
#         submit_button.click()
#     except NoSuchElementException:
#         print("Element not found.")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

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

        # Input text into the fields
        email_field.send_keys('rockypaul377@gmail.com')
        password_field.send_keys('aaabbbcc')
        submit_button.click()

        # Switch back to default content
        driver.switch_to.default_content()

        # Wait until the element with aria-label "Gym Template" opens up
        gym_template = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Gym Template']"))
        )
        time.sleep(1)

        # Perform right-click action on the div
        # Example: (for demonstration purposes)
        actions = ActionChains(driver)
        actions.context_click(gym_template).perform()
        pdb.set_trace()
        copy_option = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "duplicate"))
        )
        actions.move_to_element(copy_option).click().perform()


    except NoSuchElementException:
        print("Element not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    try:
        driver = open_firefox(FIGMA_URL)
        login_user(driver)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
