import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service('C:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

#driver.save_screenshot("C:\\Victory\\screenshotselenium")
driver.save_screenshot(os.getcwd()+"\\homepage.png")

driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_png()
driver.get_screenshot_as_base64() # saves in binary format.


