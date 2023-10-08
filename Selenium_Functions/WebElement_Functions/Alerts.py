# I cannot directly inspect & find the Xpath for alert/popup & it's elements.
# I need to switch to alert first & then use special functions to handel alerts/popups.
# When Alerts/Popups are present on web page, then I can perform action only on that, not on any other element.
# Usually alerts/popups will be developed by JavaScripts

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
my_wait = WebDriverWait(driver,10)


driver.find_element(By.XPATH,"//button[.='Click for JS Prompt']").click()
if  my_wait.until(expected_conditions.alert_is_present()):
    alert_win = driver.switch_to.alert
else:
    driver.quit()

# actions on alert window
print(alert_win.text)

alert_win.send_keys("Hi there, hello")  # alert will usually have only one text field & I can only pass text in only first field on alert

alert_win.accept()
time.sleep(2)

# alert_win.dismiss() # To cancel

driver.quit()

# Authentication alert/popup
# ==========================
# I can handel the authentication alert/popup, by bypassing it by providing the credentials in the URL, in the format: protocol://UserName:Password@path
# I need to follow the above approach because I cannot pass text in more than one fields on alert window
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

# Notification popups
# ======================
# I cannot handle notification popups(ex locations asking ones) as alert, authentication or any other normal application popups as it a browser generated.
# I need to use the below approach to disable the notification, that is the only way.

# I need to use this before launching the browser:
    # co = webdriver.ChromeOptions()
    # co.add_argument("--disable-notifications")