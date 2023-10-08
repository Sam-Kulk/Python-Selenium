import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # I need to remember this

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

dropdown = Select(driver.find_element(By.XPATH,"//select[@id='carselect']")) # it is a constructor

# 1. get all options from dropdown
all_options = dropdown.options # returns list of all options as web-elements
print(len(all_options))

print(all_options)

for x in all_options:
    print(x.text)  # I can even use get_attribute() to get value of the "value" attribute.

# 2. Single selection dropdown
dropdown.select_by_visible_text("BMW") # It is most preffered way
time.sleep(2)

dropdown.select_by_value("benz")
time.sleep(2)

dropdown.select_by_index(2)
time.sleep(2)

# Note :
# I cannot perform deselect action on the single selection dropdown, as a workaround i can select the other required option(none or other), to do the same.
# If the dropdown is not having select tag, then I can use click() on the option element
# I can explore the different methods avaliable for dropdown by the text "select".
# For multi select dropdown I can select multiple/all options & deselect as well.

driver.quit()

