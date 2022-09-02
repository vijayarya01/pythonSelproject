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

practice_url = "http://automationpractice.com/index.php"
test_practice_blog_url = "https://practicetestautomation.com/practice-test-login/"
test_automationpractice_url_table = "https://testautomationpractice.blogspot.com/"
facebook_url = "https://www.facebook.com"
ecommerce_registerpage_url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
ecommerce_url = "https://demo.nopcommerce.com/"
checkBox_url = "https://itera-qa.azurewebsites.net/home/automation"
dummy_deadlinks_url = "http://www.deadlinkcity.com"
dropdown_url_opencart_registerpage = "https://www.opencart.com/index.php?route=account/register"
the_internet_url_for_alert = "https://the-internet.herokuapp.com/basic_auth/"  # https://the-internet.herokuapp.com/
popup_url = "https://mypage.rediff.com/"
selenium_dev_frames_url = "https://www.selenium.dev/selenium/docs/api/java/index.html?allpackages-index.html"
# https://www.selenium.dev/selenium/docs/api/java/allpackages-index.html
demo_automation_practice_url = "https://demo.automationtesting.in/Frames.html"
demo_hrm_orange_register_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
hrm_orange_url = "https://www.orangehrm.com/"
dummy_ticket_url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
datepicker_jquery_url = "https://www.jqueryui.com/datepicker/"
rightclick_url = "https://swisnl.github.io/jQuery-contextMenu/demo.html"
# Initializing the url with driver

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')  # Hit the url specified.
time.sleep(3)
driver.maximize_window()

# Scroll down by pixel
driver.execute_script("window.scrollBy(0,3000)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved " , value) # 3000 moved it is.

time.sleep(5)
# Scroll down the page till the element is found
flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")

driver.execute_script("arguments[0].scrollIntoView();", flag)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved " , value) #

time.sleep(5)

# Scroll down the page till the end of webpage

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved " , value) #

time.sleep(4)
# Scroll up the page from  the end of webpage till top of the page

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved " , value) #

time.sleep(5)

driver.quit()
