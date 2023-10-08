from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

ele_loc = driver.find_element(By.XPATH,"//button[@id='openwindow']").location # result will be x and y values in dict
print(ele_loc)
print(ele_loc['x'])
print(ele_loc['y'])