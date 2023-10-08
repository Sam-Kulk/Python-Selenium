# Frame/IFrame is basically a page within a page.
# Iframe can have the tag iframe.
# I can find XPATH for the element in iframe, but I cannot directly interact with its elements.
# If I want to interact with the elements within the iframe, first I need to switch to iframe & then I can interact with it's elements.
# I can switch to iframe by index, name,id or webelement i.e. driver.find_element()(not locator).
# If I try to interact without switching to iframe, then I will get 'NoSuchElementException'.
# I need to re-switch to main web page as focus will be on iframe, if i want to interact with it's elements.
# I can find out that an element is in iframe by look & feel, while finding XPATH, if I get "NoSuchElementException" even though the locator is correct & element is loaded.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

driver.switch_to.frame("iframe-name") # name/id is prefered
driver.find_element(By.XPATH,"//input[@id='search']").send_keys("Hi there, hello")
time.sleep(5)

driver.switch_to.default_content() # to go back to main frame i.e. web page.
driver.quit()

# Note:
# I cannot directly switch from one iframe to another iframe on the webpage, if they are independent, I can switch only from main web page to iframe.
# So if I want to switch from one iframe to another iframe on the webpage, I should first switch to default webpage & then I can switch to any another iframe.

