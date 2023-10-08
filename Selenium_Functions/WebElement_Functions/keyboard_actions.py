# Basically Keys module functions can be used to perform/press keyboard buttons
# find_element().send_keys(Keys.) can be used to press any of the keyboard button and also to perform a chain of keyboard actions like CONTROL+a USING '+' operator.

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()

input_box1 = driver.find_element(By.XPATH,"//textarea[@name='text1']")
input_box2 = driver.find_element(By.XPATH,"//textarea[@name='text2']")
input_box1.send_keys("Hi there, hello!!")

# CTRL+a
# -----------------
input_box1.send_keys(Keys.CONTROL+'a')

# CTRL+c
# ----------------
input_box1.send_keys(Keys.CONTROL+'c')
time.sleep(2)

# CTRL+v
#-----------------
input_box2.send_keys(Keys.CONTROL+'v')
time.sleep(2)

# TAB
# ---------------
input_box2.send_keys(Keys.TAB)

input_box1.send_keys(Keys.CONTROL+'a')
time.sleep(2)


# DELETE
# -----------------
input_box1.send_keys(Keys.DELETE)
time.sleep(2)

driver.quit()





