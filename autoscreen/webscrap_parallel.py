import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from concurrent.futures import ThreadPoolExecutor

# Initialize the WebDriver
driver = webdriver.Chrome()

def login_to_facebook(username_face, pass_face):
    driver.get("https://www.facebook.com/")

    username_field_xpath = "//input[@class='inputtext _55r1 _6luy']"
    pass_field_xpath = "//input[@class='inputtext _55r1 _6luy _9npi']"

    user_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, username_field_xpath)))
    pass_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pass_field_xpath)))

    user_field.send_keys(username_face)
    pass_field.send_keys(pass_face)

    login_button_xpath = "//button[@name='login']"
    login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
    login.click()

    time.sleep(10)

def login_to_twitter(user_twitter, pass_twitter):
    driver.get("https://x.com/i/flow/login")
    time.sleep(10)

    username_xpath = "//input[contains(@autocomplete,'username')]"
    user = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, username_xpath)))
    user.send_keys(user_twitter)

    next_xpath = "//button[contains(@class,'css-175oi2r')]"
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_xpath)))
    next_button.click()

    pass_xpath = "//input[contains(@name,'password')]"
    pass_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, pass_xpath)))
    pass_field.send_keys(pass_twitter)

    login_xpath = "//button[contains(@class,'css-175oi2r')]"
    login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
    login_button.click()

    time.sleep(10)

async def login_to_social_media(username_facebook, pass_facebook, user_twitter, pass_twitter):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        # Run Facebook and Twitter login in parallel using ThreadPoolExecutor
        await asyncio.gather(
            loop.run_in_executor(executor, login_to_facebook, username_facebook, pass_facebook),
            loop.run_in_executor(executor, login_to_twitter, user_twitter, pass_twitter)
        )

# Main function to trigger the async login process
async def main():
    await login_to_social_media("webscrape2005@gmail.com", "webscrape@123", "@webscrape2005", "webscrape@123")

# Run the async main function
asyncio.run(main())

# Close the driver after use
driver.quit()
