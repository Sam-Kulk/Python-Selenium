from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# 1. print number of rows & column in the table
# --------------------------------------------
rows = len(driver.find_elements(By.XPATH,"//table//tr")) - 1
print("No of rows",rows)
columns = len(driver.find_elements(By.XPATH,"//table//tr[1]/th"))
print("No of columns",columns)

# 2. print data from a specific row & column
print(driver.find_element(By.XPATH,"//table//tr[2]/td[2]").text)

# get data based on certain condition

# Note :
# I can select all elements from a particular row i.e. //table//tr[index]/td
# I can select all elements from a particular column i.e. //table//tr/td[index]

eligible_courses = []
for i in range(2,rows+1):
    price = driver.find_element(By.XPATH,"//table//tr["+str(i)+"]/td[3]").text # find_element() wil expect XPATH in str, so i need to do like this in order to concatenate index in int with rest of the XPATH in str.
    if price=='30':
        course = driver.find_element(By.XPATH, "//table//tr["+str(i)+"]/td[2]").text
        eligible_courses.append(course)
print(eligible_courses)

driver.quit()