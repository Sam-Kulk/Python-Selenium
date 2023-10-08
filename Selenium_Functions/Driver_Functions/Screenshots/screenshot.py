from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

driver.save_screenshot(os.getcwd()+"/screenshot_demo.png")

# file path can have '/' or '\\' not '\' for navigation.
# if screenshot image with same name exists, it will override previous one.
# screenshot should saved with .png format

driver.quit()