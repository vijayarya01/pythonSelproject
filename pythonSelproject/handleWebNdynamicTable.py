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

driver.get(demo_hrm_orange_register_url)  # Hit the url specified.
driver.maximize_window()
# Get the windowid of the current tab
# windowID = driver.current_window_handle
# print(windowID) # window ID will be changed after closing the browser and reopening it again.
# #print(driver.title)
time.sleep(1) # this was causing issue here without putting some time.
'''
# Count the number of rows and columns

numberofRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
numberofcolumns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")) # well, <th> tag represents header of
#current row selected, this will be used to known as columns

print("The number of rows in current webtable is:", numberofRows)
print("The number of columns in current webtable is: ",numberofcolumns)
time.sleep(2)

# Read specific row and column data from table

data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
print(data)

#read all rows and all columns data from table:
# for r in range(2, numberofRows+1): # skipping header row here
#     for c in range(1, numberofcolumns+1):
#         data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[" +str(r)+ "]/td[" +str(c)+ "]").text # parameterizing the data in x path
#         print(data, end="   ")
#
#     print()
# Read data based on a specific condition(List name of books whose auther is Mukesh)

for r in range(2, numberofRows+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName =="Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName,"   ",authorName, "    ", price)
'''

#*********** Working with dynamic table on a webpage *****************

driver.find_element(By.NAME,"username").clear()
driver.find_element(By.NAME,"password").clear()
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.XPATH,'//button[@type="submit"]').click()

time.sleep(2)
#driver.switch_to.alert.accept() # accepting ok to change password window pop up
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
time.sleep(2)



# driver.quit()