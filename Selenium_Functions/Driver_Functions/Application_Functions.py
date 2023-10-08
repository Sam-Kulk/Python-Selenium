from selenium import webdriver

driver = webdriver.Chrome()

# get() - To open a specific url on browser
driver.get("https://www.letskodeit.com/practice")

# To get the title of the current tab
print(driver.title)

# To get the url of the web page opened in the current tab
print(driver.current_url)
