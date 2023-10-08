# Links are used to connect different pages of same application.
# Broken/Bad link is a link that will not have any target page & it responds with error code 400 & 500 i.e. 404 page not found, 400 Bad Request, 401 authorized etc & there is a way to find total number of broken links on web page using requests module.
# all other links will open a new webpage on same or different tab after click.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# 1. find total number of links on webpage
# ------------------------------------------
links = driver.find_elements(By.XPATH,"//a")
print(len(links))

# 2. click link which remain on same tab
# --------------------------------------------
# driver.find_element(By.XPATH,"//a[@href='/interview']").click()
# # After this I need to wait until the page/element is loaded.

# 2. click link which opens web page on new tab
# --------------------------------------------
driver.find_element(By.XPATH,"//a[@id='opentab']").click()
# After this I need to switch to new window & wait until the page/element is loaded.


driver.quit()