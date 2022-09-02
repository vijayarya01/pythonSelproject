import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service('C:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# click on the dropdown first and we will try to get elements in that.
driver.find_element(By.XPATH, '//*[@id="select2-billing_country-container"]').click()

time.sleep(2)
countrieslist = driver.find_elements(By.XPATH, '//span[@class="select2-results"]//li')
time.sleep(2)
print(countrieslist)
print(len(countrieslist))

for c in countrieslist:
    if c.text == "Pakistan":
        c.click()
        break
time.sleep(2)
#driver.switch_to.alert.dismiss()
#driver.find_element(By.XPATH,'//jdiv[@class="closeIcon_a151"]').click()
driver.find_element(By.XPATH,'//*[@id="jvlabelWrap"]/jdiv[1]]').click()
driver.find_element(By.XPATH,'//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv[1]/jdiv[1]/textarea').send_keys("Hi")
time.sleep(5)
driver.quit()
