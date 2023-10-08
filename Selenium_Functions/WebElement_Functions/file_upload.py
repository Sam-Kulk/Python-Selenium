# The file upload component will be having 'input' tag with 'type' attribute as 'file'.
# find_element().send_keys("file_location") is used to upload the file.
# The file location should be having forward slash i.e. '/' not windows style i.e. '\'

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.foundit.in/")
driver.maximize_window()


driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:/Users/samarth.kulkarni/Downloads/certificate.pdf")
time.sleep(5)

driver.quit()