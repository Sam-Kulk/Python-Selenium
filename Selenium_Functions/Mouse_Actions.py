# ActionChains class has methods to perform the mouse actions
# Mouse actions : Mouse-Hover, Click, Right-Click, Double-Click, and Drag & Drop etc..
# Note : perform() function should be mandatory used to perform the created action/actions chain

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

mouse = ActionChains(driver) # This constructor requires driver as argument

# Mouse-Hover and Click
# ---------------------------
mouse.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).move_to_element(driver.find_element(By.XPATH,"//a[.='Top']")).click().perform()
time.sleep(2)


# Right-click
# -----------------
mouse.context_click(driver.find_element(By.XPATH,"//input[@id='bmwcheck']")).perform()
time.sleep(3)

# Double-Click
# -----------------------
mouse.double_click(driver.find_element(By.XPATH,"//legend[.='Radio Button Example']")).perform()
time.sleep(3)

# Drag and Drop
# ---------------------
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source = driver.find_element(By.XPATH,"//div[@id='box6']")
distination = driver.find_element(By.XPATH,"//div[@id='box106']")
mouse.drag_and_drop(source,distination).perform()
time.sleep(3)

# Slider movement
# -----------------------
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slider = driver.find_element(By.XPATH,"//div[@class = 'price-range-block']//span[1]")
min_slider_loc = min_slider.location
print(min_slider_loc)

max_slider = driver.find_element(By.XPATH,"//div[@class = 'price-range-block']//span[2]")

mouse.drag_and_drop_by_offset(min_slider,min_slider_loc['x']+100,0).perform()
mouse.drag_and_drop_by_offset(max_slider,-100,0).perform()  # for opp direction -ve values should be used
time.sleep(2)

# scrolling
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
mouse.scroll_to_element(driver.find_element(By.XPATH,"//img[@alt='Flag of India']")).perform()
time.sleep(3)
mouse.scroll_by_amount(0,1000).perform()
time.sleep(3)

driver.quit()
