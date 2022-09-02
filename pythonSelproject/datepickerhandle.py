import time

import requests
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
# Initializing the url with driver
driver.get(dummy_ticket_url)  # Hit the url specified.

driver.maximize_window()
time.sleep(1)
'''
# Date picker is in frame. 
# used datepicker_jquery_url
driver.switch_to.frame(0)

# mm/dd/yyyy , well this date picker allows to fill directly dates with send keys, and its working.
#driver.find_element(By.XPATH,'//*[@id="datepicker"]').send_keys("05/05/1966")

# We will use the forward button on the calendar to move on the future date.
year = "2024"
month = "October"
day = "08"

# First open the calendar
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()  # opens datepicker

while True:
    yr = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[2]').text
    mnth = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    if yr == year and month == mnth:
        break
    else:
        driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[2]/span').click() # Next arrow button on calendar
        #river.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[1]/span').click() # back arrow button on calendar

# select Date
dates = driver.find_elements(By.XPATH,'//div[@id="ui-datepicker-div"]//table/tbody/tr/td/a')
for ele in dates:
    if ele.text == day:
        ele.click()
        break


time.sleep(5)

'''
# Date of birth from dummyticket portal practice
driver.find_element(By.XPATH,"//input[@id='dob']").click()  # open date picker or calendar

# select month from dropdown using the Select class with visible text value.
date_picker_month = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
date_picker_month.select_by_visible_text("Dec")
# select year from dropdown using the Select class with visible text value.
date_picker_year = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
date_picker_year.select_by_visible_text("1991")

all_dates = driver.find_elements(By.XPATH,'//div[@id="ui-datepicker-div"]//table/tbody/tr/td/a')

for date in all_dates:
    if date.text == "05":
        date.click()
        break

time.sleep(5)






driver.quit()