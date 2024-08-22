# Synchronization
# ======================
# Synchronization is a technique to sync the selenium execution speed & web page loading speed i.e. managing the mismatch in speeds.
# These techniques deal with managing the selenium execution speed not the application speed to tackle the issue.
# The problem raises mainly while navigating from one page to another page, pop-us & alerts etc...
# The following are the synchronization techniques i.e. sleep(), implicitly_wait() & explicitly_wait()
# all time specified is by default in seconds
# find_element() & implicitly_wait() are wrt dom & explicitly_wait() can check of visibility on the element on webpage

from selenium import webdriver
import time

from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# 1. sleep() - Basically it pauses the execution for the specified time
time.sleep(2)

# disadvantages :
# It pauses the execution for the specified time, even though the web element is visible withing that time, so it increases execution time unnecessarily.

# 2. implicitly_wait()
driver.implicitly_wait(15) # This will work on all the elements coming after this statement & will be applicable till driver.quit() or driver.close() is used.
driver.find_element(By.XPATH,"//input[@id='bmwradio']")

# Note :
# This will wait until the element is present on webpage DOM for a specified maximum time, before throwing the exception.
# It is a good practice to use this right after the get() or maximize_window()

# disadvantages :
# If our expected result aims to validate a particular element should not be present on the webpage, then at that time it will wait for max specified time trying to find the element, eventhough the expectation is met in 1st second
# It will only check for the presence of the element on DOM not it's visibility & clickability on the webpage.

# 3. Explicit wait
# It works based on condition i.e. waiting until certain condition such as presence, visibility, clickability etc. is satisfied/true.
mywait = WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException]) # explicit wait declaration i.e. (driver instance, timeout)
# this should be created after window max
# mywait is WebDriverWait class object
# ignore_exceptions parameter is used to ignore the specified exceptions & continue the further execution.

element = mywait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@id='bmwradio']")))

print(element)
# after chekcing the condition I can perform any action on the element.
element.click()

time.sleep(5)

driver.quit()

# try, expect & finally concepts can be used with explicit wait.