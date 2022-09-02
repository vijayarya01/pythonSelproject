import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

serv_obj = Service('C:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

practice_url = "http://automationpractice.com/index.php"
test_practice_blog_url = "https://practicetestautomation.com/practice-test-login/"
facebook_url = "https://www.facebook.com"
ecommerce_registerpage_url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
ecommerce_url = "https://demo.nopcommerce.com/"
checkBox_url = "https://itera-qa.azurewebsites.net/home/automation"
dummy_deadlinks_url = "http://www.deadlinkcity.com"
dropdown_url_opencart_registerpage  = "https://www.opencart.com/index.php?route=account/register"
the_internet_url_for_alert = "https://the-internet.herokuapp.com/basic_auth/" # https://the-internet.herokuapp.com/
popup_url = "https://mypage.rediff.com/"
selenium_dev_frames_url = "https://www.selenium.dev/selenium/docs/api/java/index.html?allpackages-index.html"
#https://www.selenium.dev/selenium/docs/api/java/allpackages-index.html
demo_automation_practice_url = "https://demo.automationtesting.in/Frames.html"
demo_hrm_orange_register_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
hrm_orange_url = "https://www.orangehrm.com/"
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
#driver.find_element(By.NAME, 'username').clear()
driver.find_element(By.NAME, 'username').send_keys("Admin")

#driver.find_element(By.NAME, 'password').clear()
driver.find_element(By.NAME, 'password').send_keys("admin123")
time.sleep(2)
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]').click()
time.sleep(5)

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Test Case is passed.")
else:
    print("Test Case is failed.")

driver.close()