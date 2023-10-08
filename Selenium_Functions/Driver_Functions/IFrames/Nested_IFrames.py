import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@href='#Multiple']").click()

first_iframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(first_iframe)

second_iframe = driver.find_element(By.XPATH,"//div[@class= 'iframe-container']/iframe[@src='SingleFrame.html']")
driver.switch_to.frame(second_iframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hi there, hello") #while inspecting this I amy get multiple matches of input field, but while execution since focus will be on innerframe, so only one match will be there.

# to switch to parent frame from inner frame
driver.switch_to.parent_frame()

# to switch to defualt frame i.e. main webpage
driver.switch_to.default_content()

driver.quit()
