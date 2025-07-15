from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

social_media="https://www.instagram.com/"
username="@sxnjxnxx.1405"
password="KSR@2005"

driver.get(social_media)

username_field=driver.find_element(By.CSS_SELECTOR,"input[name='username']")
password_field=driver.find_element(By.CSS_SELECTOR,"input[name='password']")
login=driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > main:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3)")

username_field.send_keys(username)
password_field.send_keys(password)
login.click()

