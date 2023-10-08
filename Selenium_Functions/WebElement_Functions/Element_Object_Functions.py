from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

ele = driver.find_element(By.XPATH,"//button[@id='openwindow']")

# print element text
print(ele.text)

# get attribute value
print(ele.get_attribute('class')) # attribute_name should be passed as str