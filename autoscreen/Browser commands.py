from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()

browser.get("https://leetcode.com/")
browser.find_element(By.CSS_SELECTOR,".btn.sign-up-btn.hover-panel.round").click()
time.sleep(5)
browser.back()
time.sleep(5)
browser.refresh()
time.sleep(5)
browser.forward()