import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

serv_obj = Service('C:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

practice_url = "http://automationpractice.com/index.php"
facebook_url = "https://www.facebook.com"
ecommerce_url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(ecommerce_url)

driver.maximize_window() # For maximizing window

# checking is_enabled() and is_displayed()
search_bar_xpath = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("The displayed status is, ", search_bar_xpath.is_displayed())
print("The enabled status is ", search_bar_xpath.is_enabled())

# checking for is_selected() for radio button and check boxes
rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("The defaults radio button status is below: ")
print(rd_male.is_selected()) # This will return False
print(rd_female.is_selected()) # this will also return False

rd_male.click()

print("The radio button status after clicking Male button is below: ")
print(rd_male.is_selected()) # This will return False
print(rd_female.is_selected()) # this will also return False

rd_female.click()

print("The radio button status after clicking Female button is below: ")
print(rd_male.is_selected()) # This will return False
print(rd_female.is_selected()) # this will also return False

