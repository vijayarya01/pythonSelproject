import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")

serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj, options=opt)

driver.get("https://whatmylocation.com")

driver.maximize_window()
time.sleep(5)