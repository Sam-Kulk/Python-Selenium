import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# 1. SELECTING
# ======================
# selecting specific checkbox
# ----------------------------------
# driver.find_element(By.XPATH,"//input[@id='benzcheck']").click()
# time.sleep(2)

# selecting all the checkboxes
# ---------------------------------
# checkboxes = driver.find_elements(By.XPATH,"//input[@name='cars' and @type='checkbox']")
# for checkbox in checkboxes:
#     checkbox.click()
# time.sleep(2)

# selecting multiple checkboxes by choice
# ------------------------------------------
# checkboxes = driver.find_elements(By.XPATH,"//input[@name='cars' and @type='checkbox']")
# for checkbox in checkboxes:
#     value = checkbox.get_attribute('value')
#     if value == 'benz' or value == 'honda':
#         checkbox.click()
# time.sleep(2)
# # I can write even a appropriate XPATH for doing the same task.

# selecting last few checkboxes
# ------------------------------------
# checkboxes = driver.find_elements(By.XPATH,"//input[@name='cars' and @type='checkbox']")
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()
# time.sleep(2)

# selecting first few checkboxes
# ------------------------------------
# checkboxes = driver.find_elements(By.XPATH,"//input[@name='cars' and @type='checkbox']")
# for i in range(0,len(checkboxes)-1):
#     checkboxes[i].click()
# time.sleep(2)

# 2. IS_SELECTED
# =======================
# driver.find_element(By.XPATH,"//input[@id='benzcheck']").click()
#
# if driver.find_element(By.XPATH,"//input[@id='benzcheck']").is_selected():
#     print("Is selected")

# 3. UNSELECTING
# ==================
# again click() function itself will unselect the checkbox

driver.find_element(By.XPATH,"//input[@id='benzcheck']").click()
driver.find_element(By.XPATH,"//input[@id='benzcheck']").click()
time.sleep(2)


driver.quit()