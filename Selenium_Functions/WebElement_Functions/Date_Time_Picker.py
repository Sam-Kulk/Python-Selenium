# Date or Date-Time Picker field can be of different types.
# Date or Date-Time pickers will have 'input' tag with 'type' attribute as 'date' or 'datetime' or something like that.
# Date or Date-Time Picker have a input field & send_Keys() methods can be used generally to pass the data into date input field i.e. it is a kind of alternative for date selection. here i need to pass the date in the required format

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)

# date picker
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("09/17/2023")
time.sleep(2)

# date-time picker
driver.get("http://172.25.36.193/EIR/CheckImeiSimulator")
driver.find_element(By.XPATH,"(//input)[1]").send_keys("ADMIN")
driver.find_element(By.XPATH,"(//input)[2]").send_keys("ADMIN3")
driver.find_element(By.XPATH,"(//button)[2]").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//div[@class='MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button'])[2]").click()
time.sleep(5)
date_box = driver.find_element(By.XPATH,"//input[@type='datetime-local']")

date_box.send_keys("17-09-2023")
date_box.send_keys(Keys.TAB) # Here use of TAB is mandatory to switch between two sections.
date_box.send_keys("04:30PM")  # Here I can avoid using ': & -',as default switch will be done after filling each part of the section. PM should be attcahed to mins part.
time.sleep(2)


driver.quit()

