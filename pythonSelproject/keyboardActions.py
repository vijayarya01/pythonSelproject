import time

import requests
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service('C:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.text-compare.com")
driver.maximize_window()
# first identify the source box and target box where text will be kept and compared.
input1 = driver.find_element(By.XPATH,'//*[@id="inputText1"]').send_keys(" Welcome to keyboard actions")
input2 = driver.find_element(By.XPATH,'//*[@id="inputText2"]')

time.sleep(3)

# input 1 . control + A  SELECT THE TEXT.
act = ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
# or We can write this in one line of code as well.
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(2)

# input 1 . control + C . Copy the text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()



# Press Tab key to navigate to input box 2
act.send_keys(Keys.TAB).perform()

# input 2, Paste the selected text in here. Control + V
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(4)