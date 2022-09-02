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

# select specific checkbox
# driver.find_element(By.XPATH,"//input[@id='monday']").click()
# time.sleep(5)

# Select all of weekdays checkbox in the webpage
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")

# #Apprach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
# #Apprach 2
# for checkbox in checkboxes:
#     checkbox.click()
# Select any of two days or values from weekdays
# for checkbox in checkboxes:
#     dayname = checkbox.get_attribute("id")
#     if dayname == 'monday' or dayname =='sunday':
#         checkbox.click()



# Select last two checkbox from weekdays
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click

# Select first two check box from weekdays
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()

# Clearig all the check boxes or
# check if checkbox is selected, then unselect it.


time.sleep(5)
driver.quit()