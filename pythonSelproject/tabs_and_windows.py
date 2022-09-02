import os
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service('C:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com") # currently , url is not working.
driver.maximize_window()

regiters_link = Keys.CONTROL + Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(regiters_link)

# Selenium 4 feature
driver.get("https://demo.nopcommerce.com")
driver.switch_to.new_window('tab') # to open in new tab of the browser
#driver.switch_to.new_window('window')# to open in a new window browser
driver.get("https://www.oragehrm.com")
time.sleep()
