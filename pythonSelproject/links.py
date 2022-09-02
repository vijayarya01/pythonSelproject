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

# Select all of the working links on a webpage
# all_links = driver.find_elements(By.TAG_NAME,'a')
# print(len(all_links))
# for link in all_links:
#     print(link.text)

# find the broken links on a webpage

broken_links = driver.find_elements(By.TAG_NAME, 'a')
count = 0  # initialize this to count the number of broken links in a webpage

for link in broken_links:
    url = link.get_attribute("href")  # this will give url inside href attribute under anchor(a) tag on html page
    try:  # in order to avoid client -server network error we need to place this in try and except block
        resp = requests.head(url)

    except:
        None

    if resp.status_code >= 400:
        print(url, " is a broken link")
        count += 1
    else:
        print(url, " is a valid link")

print("total number of broken links are  ", count)
