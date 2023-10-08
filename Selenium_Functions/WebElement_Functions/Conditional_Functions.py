from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
ele = driver.find_element(By.XPATH,"//input[@id='bmwradio']")

# is_displayed(): To check whether the element is displayed/visible on the webpage or not, it returns bool value
print(ele.is_displayed())

# is_enabled()
print(ele.is_enabled())

# is_selected()
print(ele.is_selected())

# Note: displayed & enabled functions can be used on any web element, whereas the selected can be used only on checkboxes & radio buttons.

driver.quit()


