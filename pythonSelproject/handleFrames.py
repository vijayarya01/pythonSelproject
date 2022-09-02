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


'''
# switch to first frame and exit
driver.switch_to.frame("packageListFrame") # by name
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click() # it had issue here with xpath, not sure why
driver.switch_to.default_content()

time.sleep(5)
# switch to second frame and exit
driver.switch_to.frame("packageFrame") # by name
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()

time.sleep(5)
# switch to third frame and do final operation
driver.switch_to.frame("classFrame") # by name
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()

time.sleep(5)

'''
#*************** Frame within a frame or Inner Frame ************* #

bttn_to_open_frame = driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
outframe = driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outframe)

innerframe = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)
txt_box_innerframe = driver.find_element(By.XPATH,"/html/body/section/div/div/div/input")
txt_box_innerframe.send_keys("Thanks for entering txt in here GOoD, Job")

# This feature is in selenium 4 only to switch to parent frame except to default_content i.e Main screen of webpage
driver.switch_to.parent_frame()

time.sleep(4)
driver.quit()