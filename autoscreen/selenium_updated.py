from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()

def login_to_face(username_face, pass_face):
    driver.get("https://www.facebook.com/")

    username_field_xpath = "//input[@class='inputtext _55r1 _6luy']"
    pass_field_xpath = "//input[@class='inputtext _55r1 _6luy _9npi']"

    user_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, username_field_xpath)))
    pass_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pass_field_xpath)))

    user_field.send_keys(username_face)
    pass_field.send_keys(pass_face)

    login_button_xpath ="//button[@name='login']"
    login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
    login.click()

    time.sleep(10)


def login_to_twitter(user_twitter,pass_twitter):
    driver.get("https://x.com/i/flow/login")
    time.sleep(10)
    username_xpath="//input[contains(@autocomplete,'username')]"
    user=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,username_xpath)))
    user.send_keys(user_twitter)

    next_xpath="//button[contains(@class,'css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l')]"
    next=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,next_xpath)))
    next.click()

    pass_xpath="//input[contains(@name,'password')]"
    passw=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,pass_xpath)))
    passw.send_keys(pass_twitter)

    login_xpath="//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-o7ynqc r-6416eg r-icoktb r-1ny4l3l')"
    login=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,login_xpath)))
    login.click()
    time.sleep(10)

