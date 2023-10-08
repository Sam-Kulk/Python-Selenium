# Boostrap dropdown will not have 'select' tag, instead it will be having 'span' tag.
# It has dropdown-list with 'ul' tag and it's options with 'li' tag & it can have a search box input field.
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
my_wait = WebDriverWait(driver,10)


mouse = ActionChains(driver)
mouse.scroll_to_element(driver.find_element(By.XPATH,"//span[@id='select2-billing_state-container']")).perform()
time.sleep(5)

driver.find_element(By.XPATH,"//span[@id='select2-billing_state-container']").click()

my_wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//ul[@id='select2-billing_state-results']")))

driver.find_element(By.XPATH,"//input[@aria-owns='select2-billing_state-results']").send_keys("Chandigarh")

driver.find_element(By.XPATH,"//ul[@id='select2-billing_state-results']/li[.='Chandigarh']").click()

time.sleep(5)

driver.quit()