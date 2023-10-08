# Note : Window/tab handles/ids/name cannot be found on HTML and are dynamic, i.e. everytime window gets new handel

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# fetching window handles
print(driver.current_window_handle)

driver.find_element(By.XPATH,"//a[@id='opentab']").click()

window_handles = driver.window_handles # returns the list of windows handles
print(window_handles)

# switching windows
driver.switch_to.window(window_handles[1])
print(driver.title)

driver.switch_to.window(window_handles[0])
print(driver.title)

driver.quit()
