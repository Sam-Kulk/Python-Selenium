from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# clicking
radio = driver.find_element(By.XPATH,"//input[@id='bmwradio']")
radio.click()
time.sleep(2)

# passing text
input = driver.find_element(By.XPATH,"//input[@id='autosuggest']")
input.send_keys(123) # can be str, int or any
time.sleep(2)

# clearing text in field

input.clear()
time.sleep(2)