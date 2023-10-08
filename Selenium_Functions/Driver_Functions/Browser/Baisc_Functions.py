from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")

# to maximize the tab/window
driver.maximize_window()
time.sleep(2)

# I can also minimize

driver.get("https://github.com/")
time.sleep(2)

# back()
driver.back()
time.sleep(2)

# forward()
driver.forward()
time.sleep(2)

# refresh()
driver.refresh()

# to close browser/all it's opened tabs
driver.quit()

# Note
 # driver.close() to close the current opened tab of the browser, if I want to close a specific window, first I need to switch to that particular window
 # tab = window

