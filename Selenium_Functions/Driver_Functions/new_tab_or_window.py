import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# new tab
driver.switch_to.new_window('tab') # opens a new tab and switches control to that new tab.
driver.get("https://www.letskodeit.com/practice")
time.sleep(3)

# new window
driver.switch_to.new_window('window') # opens a new browser window and switches the control to that new window.
driver.get("https://www.jqueryscript.net/")
time.sleep(5)


driver.quit()