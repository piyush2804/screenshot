from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from PIL import ImageGrab

import time

#set chromodriver.exe path
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.maximize_window()

#launch URL
driver.get("https://www.w3schools.com/html/html_tables.asp")
#identify element
driver.execute_script("document.body.style.zoom='100%'")
time.sleep(5)
m = driver.find_element(By.CSS_SELECTOR, "div.w3-example")

driver.execute_script("arguments[0].scrollIntoView({block: 'center' , behavior: 'smooth', inline: 'nearest'})", m)


#capture screenshot and save it in .png extension
time.sleep(5)

m.screenshot("C:\\Users\\user\\Downloads\\screenshot_text.png")
#browser quit
driver.quit()
