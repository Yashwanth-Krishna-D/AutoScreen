import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from autoscreen import nlp  # Assuming this is your custom module
from autoscreen import img  # Assuming this is your custom module

def screenshot(browser, name):
    folder_name="screenshots"
    try:
        # Ensure the folder exists
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        safe_name=name

        # Take screenshot of the chat page and save it in the 'screenshots' folder
        screenshot_filename = os.path.join(folder_name, f"{safe_name}.png")
        browser.save_screenshot(screenshot_filename)

        print(f"Screenshot saved as {screenshot_filename}")
    except Exception as e:
        print(f"Error taking screenshot for {name}: {e}")

# Example usage
# browser = webdriver.Chrome()
# browser.get("https://www.instagram.com/")
# screenshot(browser, "screenshots", "example_user")
