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

# driver.get(rightclick_url)  # Hit the url specified.
# time.sleep(3)
# driver.maximize_window()

'''
driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.XPATH, '//button[@type="submit"]').click()

time.sleep(2)


# driver.switch_to.alert.accept() # accepting ok to change password window pop up

admin = driver.find_element(By.XPATH, "//@[@id='menu_admin_viewAdminModule']/b")
usrmngt = driver.find_element(By.XPATH, "//@[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//@[@id='menu_admin_viewSystemUsers']")

# MouseHover


act = ActionChains(driver) # create a object of ActionChains class and pass the driver object
act.move_to_element(admin).move_to_element(usrmngt).move_to_element(users).click().perform()
'''
'''

# Right Click action
rightclick_button = driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')

act = ActionChains(driver)

act.context_click(rightclick_button).perform()

time.sleep(2)
# right click on button will pop up few options and then we choosing to click on copy
driver.find_element(By.XPATH,'/html/body/ul/li[3]/span').click()
time.sleep(3)
# this create a alert window and then we click OK on that window
driver.switch_to.alert.accept()
'''

'''

# Double Click using mouse operation on a website.

driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3')
driver.maximize_window()

# switching to frame on the page where element is to be found.
driver.switch_to.frame('iframeResult')


field1_text = driver.find_element(By.XPATH,'//*[@id="field1"]')
field1_text.clear()
time.sleep(1)
field1_text.send_keys("This double click ")

# clicking on the button to perform double click mouse operation below

btton = driver.find_element(By.XPATH,'/html/body/button')
act = ActionChains(driver)

act.double_click(btton).perform()

'''
'''
# we will perform here drag and drop operations with mouse on below website
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()
time.sleep(3)

# locating source and target elements
source_drag_washington = driver.find_element(By.XPATH,'//*[@id="box3"]')
target_drop_united_States= driver.find_element(By.XPATH,'//*[@id="box103"]')

act = ActionChains(driver)
act.drag_and_drop(source_drag_washington,target_drop_united_States).perform()
# for performing it to multiple times, then we need to write more actions , we can not do it at once for all.

source_drag_rome = driver.find_element(By.ID,"box6")
target_drop_italy= driver.find_element(By.ID,'box106')
act.drag_and_drop(source_drag_rome,target_drop_italy).perform()

'''

# We will perform here slider operation as we do in ecommerce project with mouse action class
driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')
driver.maximize_window()
time.sleep(2)

min_slider = driver.find_element(By.XPATH,'//body//div//span[1]')
max_slider = driver.find_element(By.XPATH,'//body//div//span[2]')

# finding the location of sliders is necessary.
print("************** Location of slider before moving")

print(min_slider.location) #{'x': 59, 'y': 251}
print(max_slider.location) #{'x': 613, 'y': 251}

act  = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform() # moved x axis by 100, y kept 0 bcz no moving.
act.drag_and_drop_by_offset(max_slider,-50,0).perform() # decreased max slider by 50 , y kept 0

print("************** Location of slider after moving")

print(min_slider.location) #{'x': 159, 'y': 251}
print(max_slider.location) #{'x': 563, 'y': 251