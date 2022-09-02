import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException,ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service('C:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

# explicit wait declaration

#mywait = webdriver(driver,10)
mywait = webdriver(driver,10,ignored_exceptions = [NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException,
                                                   Exception])

driver.get("https://www.google.com")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys("Selenium")
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XAPTH,"//h3[text()='Selenium'")))
# even if above statement throw some exception, it will handle and move to next line of code.
searchlink.click()
