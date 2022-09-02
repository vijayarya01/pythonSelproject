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
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get(the_internet_url_for_alert)

driver.maximize_window()  # For maximizing window
'''
driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()

alert_window = driver.switch_to.alert # this is a way to switching to pop up and saving that to a variable

print(alert_window.text)   # will get the text shown in pop up or alert window and we are printing that here

alert_window.send_keys("Welcome to popus demo") # this will enter text to available field in pop up

alert_window.accept() # this method will click OK button on the pop up

#alert_window.dismiss() # this will push the CANCEL button on pop up

'''

# ******************** Test on another portal for pop up window********************** #
'''
# direct clicking on Go button on webpage, appears a pop up window

btn_go_xpath = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/form/table/tbody/tr[1]/td[3]/input").click()
alert_pop = driver.switch_to.alert

print(alert_pop.text)
time.sleep(5)
alert_pop.accept()
'''

#***************** Handle the authentication pop up **********************

'''
Basically, we initiaze the url above as shown in the line 24 of this.
driver.get(url)

But in this case,

'''
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth/")


