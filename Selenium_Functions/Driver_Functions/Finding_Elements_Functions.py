from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# to return a first matching element
ele = driver.find_element(By.XPATH,"//input[@id='autosuggest']")
print(ele)

# to return all matching elements
eles = driver.find_elements(By.XPATH,"//input")
print(eles)

driver.quit()

# Note : The locator should be given in double quotes