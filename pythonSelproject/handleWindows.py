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
dropdown_url_opencart_registerpage = "https://www.opencart.com/index.php?route=account/register"
the_internet_url_for_alert = "https://the-internet.herokuapp.com/basic_auth/"  # https://the-internet.herokuapp.com/
popup_url = "https://mypage.rediff.com/"
selenium_dev_frames_url = "https://www.selenium.dev/selenium/docs/api/java/index.html?allpackages-index.html"
# https://www.selenium.dev/selenium/docs/api/java/allpackages-index.html
demo_automation_practice_url = "https://demo.automationtesting.in/Frames.html"
demo_hrm_orange_register_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
hrm_orange_url = "https://www.orangehrm.com/"

driver.get(demo_hrm_orange_register_url)  # Hit the url specified.
driver.maximize_window()
# Get the windowid of the current tab
# windowID = driver.current_window_handle
# print(windowID) # window ID will be changed after closing the browser and reopening it again.
# #print(driver.title)
time.sleep(1) # this was causing issue here without putting some time.

driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()  # this will open in new tab of browser
# print(driver.title) # this failed because it could not get it , driver was focussed on parent window
# By default, the driver always focuses on the parent webpage even after clicking a new url and going to new webpage.

windowIDs = driver.window_handles
# print(windowIDs)

parentWindowID = windowIDs[0]
childWindowId = windowIDs[1]
# print(parentWindowID,childWindowId)

# Now we can switch to and fro among windows opened in current browser using these ids.
driver.switch_to.window(childWindowId)
print("The title of child window ", driver.title)
driver.switch_to.window(parentWindowID)
print("The title of parent window ", driver.title)


# In case of many windows handling, we can use below approach using for loop

for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)

# in order to close random tabs we can do as below
for winid in windowIDs:
    driver.switch_to.window(winid)
    if driver.title == 'OrangeHRM': # in order to close any specific tab out of 4 tabls, we need to have title of that.we can close.
        driver.close()