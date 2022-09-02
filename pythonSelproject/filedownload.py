import time

import requests
from selenium.webdriver import ActionChains
from selenium import webdriver

from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# creating a location using os module and passing it to preference object
location = os.getcwd()


# Scenarios to download the files in various browsers.
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\drivers\chromedriver.exe")

    # setup to our own preference location to download limited to chrome browser
    preferences = {"download.default_directory": location,
                   "plugins.always_open_pdf_externally": True}  # created a dic. object, we can hardcode any location here.
    # Above,another key added plugings one, in order to avoid the pdf file in reader mode, this will directly download pdf file now.
    # The same plugins is a bug in edge, we can not do in edge browser.
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)  # prefs is predefined parameter , preference we are giving to it.

    # initiating our driver here
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


def firefox_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\drivers\geckodriver.exe")

    # setup to our own preference location to download limited to chrome browser
    ops = webdriver.FirefoxOptions()
    # ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword") # Mime type
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk",
                       "application/pdf")  # mime type changed for pdf download
    ops.set_preference("browser.download.manager.showWhenStarting", False)

    # above code is to avoid that download window manager which firefox trigger while downloading any file.
    ops.set_preference("browser.download.folderList", 2)  # 0-desktop,1-downloads folder,2 - desired location
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True)  # only in case of pdf
    # initiating our driver here
    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver


# my_driver = chrome_setup()
# my_driver = edge_setup() # this will be same as chrome, just replace the term chrome with edge.
my_driver = firefox_setup()
'''
my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/ ")
time.sleep(4)
my_driver.maximize_window()
time.sleep(3)
file_Btton = my_driver.find_element(By.XPATH,'//*[@id="table-files"]/tbody/tr[1]/td[5]/a')
file_Btton.click()
time.sleep(2)
'''
# my_driver.find_element(By.XPATH,'//*[@id="dismiss-button"]/div/span').click()
# my_driver.switch_to.alert.dismiss()
time.sleep(5)

# Scenario to upload the file.

my_driver.get("https://www.monsterindia.com")
my_driver.maximize_window()

my_driver.find_element(By.XPATH, '//*[@id="user-signup-actions"]/div[1]/div[1]/a[2]').click()
my_driver.find_element(By.XPATH, '//*[@id="file-upload"]').send_keys('C:\\Users\\VijayD\\Downloads\\519551.pdf')

time.sleep(5)
