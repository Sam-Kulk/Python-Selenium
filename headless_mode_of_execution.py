# Headless of test execution
# =============================
# It is basically running our test execution in backend without opening the browser.
#
# Advantages
# ----------------
# 1. When running large number of test cases, I cannot perform any other operation in my laptop, because the browsers keep on opening, creating the disturbance for other activities, so headless mode will over come this issue.
# 2. Reduction in test execution time, since the browsers are not opened.

from selenium import webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--headless")

driver = webdriver.Chrome(ops)

driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.quit()