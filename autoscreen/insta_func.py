import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def chats(browser, key):
    try:
        # Click the first user
        css_first_user = "//div[contains(@class,'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x168nmei x13lgxp2 x5pf9jr xo71vjh x1lliihq xdj266r x11i5rnm xat24cr x1mh8g0r xg6hnt2 x18wri0h x1l895ks x1y1aw1k xwib8y2 xbbxn1n xxbr6pl')]"
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, css_first_user))).click()

        # Extract chat messages
        chat_css_selector = "//div[contains(@class,'html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x6ikm8r x10wlt62')]"
        time.sleep(5)
        messages = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.XPATH, chat_css_selector)))
        chat_texts = [message.text for message in messages]
        print("Chat Extracted: ", chat_texts)

        # Create a folder named 'screenshots' if it doesn't exist
        folder_name = "screenshots"
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
            except Exception as e:
                print(f"Error creating directory: {e}")
                return []

        # Take a screenshot of the chat page and save it in the 'screenshots' folder
        screenshot_filename = os.path.join(folder_name, f"chat_screenshot_{key}.png")
        try:
            browser.save_screenshot(screenshot_filename)
            print(f"Screenshot saved as {screenshot_filename}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

        return chat_texts

    except Exception as e:
        print(f"An error occurred in the 'chats' function: {e}")
        return []

# Example usage
# browser = webdriver.Chrome()
# browser.get("https://www.instagram.com/")
# chats(browser, "example_chat")
