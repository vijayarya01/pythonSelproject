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

# dropcountry_xpath_elements = driver.find_element(By.XPATH,"//select[@name='country_id']")
# # # In order to select the value of dropdown we have to use the Select class
# select_value_drodwn = Select(dropcountry_xpath_elements)
#select_value_drodwn_value = select_value_drodwn.select_by_value("10") # choose value of value from html in dropdowns
# you can also rewrite above lines of code like below
# select_value_drodwn_value_without_dropcountry_xpath_elements = Select(driver.find_element(By.XPATH,"//select[@name='country_id']")).select_by_value("12") # value shown in html
# time.sleep(3)
# select_value_drodwn_index = Select(select_value_drodwn_value_without_dropcountry_xpath_elements).select_by_index(13) # by index of options of dropdown
# time.sleep(3)
# select_value_drodwn_visibletxt = Select(select_value_drodwn_value_without_dropcountry_xpath_elements).select_by_visible_text("India") # inner text of options of dropdown
# time.sleep(3)

# Capture all the options from the dropdown list and print them all

# all_options = select_value_drodwn.options
# print("total number of options" , len(all_options))

# for opt in all_options:
#     print(opt.text)

# Without using the built in functions such as visibletxt, index or value , select any given value from dropdown list.
# Need to run a for loop and then match the given value came from loop and do the click operation on loop value.
# for opt in all_options:
#     if opt.text == "India":
#         opt.click()
#         break

# all_options_without_select_input = driver.find_elements(By.XPATH,"//*[@id='input-country']/option")
# print(len(all_options_without_select_input))


#####################################################################################################

#********************Practice of dropdown and checkboxes below**************************#

username = driver.find_element(By.NAME,'username').send_keys("student")
password = driver.find_element(By.NAME,'password').send_keys("Password123")

btn_submit = driver.find_element(By.CLASS_NAME,'btn').click()


time.sleep(5)
# get current url for verification
current_url = driver.current_url
print(current_url)
if current_url == "practicetestautomation.com/logged-in-successfully/":
    print("Test case is passed for logging.")

time.sleep(4)

text_on_page = driver.find_element(By.XPATH,'//*[@id="loop-container"]/div/article/div[2]/p[1]/strong')
print(text_on_page.text)

btn_logout = driver.find_element(By.LINK_TEXT,'Log out').click()

time.sleep(3)



