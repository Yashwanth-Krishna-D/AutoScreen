from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://leetcode.com/')

# Locate the element using the corrected CSS selector
text = browser.find_element(By.CSS_SELECTOR, "div[class='content text-center'] h1")
print(text.text)
