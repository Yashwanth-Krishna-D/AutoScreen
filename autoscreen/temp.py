from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from autoscreen import frontend
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autoscreen import insta_chats1
from autoscreen import insta_posts

browser=webdriver.Chrome()
browser.get(frontend.url)

#To get the css values  of the username and password sections
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))

username_field=browser.find_element(By.XPATH,"//input[@name='username']")
password_field=browser.find_element(By.XPATH,"//input[@name='password']")

#To fill the username and password values
username_field.send_keys(frontend.username)
password_field.send_keys(frontend.password)

#To click the login button
login_xpath="//div[contains(@class,'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1')]"
#login_xpath="body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > main:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3)"
browser.find_element(By.XPATH, login_xpath).click()
#To wait until saved info page comes
WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//section[@class='xyamay9 x1o0k56v x1l90r2v x4ge4z1 x2b8uid']")))
not_now_button_xpath ="//div[@role='button']"
WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, not_now_button_xpath))).click()

# Wait till the notifications page appears and click the "Not Now" button
notifications_not_now_button_xpath = "//*[contains(@class, '_a9--') and contains(@class, '_ap36') and contains(@class, '_a9_1')]"
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, notifications_not_now_button_xpath))).click()

if frontend.Segment=="chats":
    messages_icon_selector = "//a[@href='/direct/inbox/']"
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, messages_icon_selector))).click()

    #Call the function chats to extract all the chats
    insta_chats1.chats(browser,frontend.keyword)

if frontend.Segment=="posts":
    post_icon_xpath = "//div[@class='x1n2onr6']"

    try:
        # Optional: Wait for a bit to ensure the page has loaded
        time.sleep(5)

        # Wait for the post icon to be clickable and then click it
        post_icon = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, post_icon_xpath))
        )
        post_icon.click()
        time.sleep(10)
        # Call the function to extract all posts
        insta_posts.extract_posts(browser)

    except Exception as e:
        print(f"Error encountered: {e}")


