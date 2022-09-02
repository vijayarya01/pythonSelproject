import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

serv_obj = Service('C:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

practice_url = "http://automationpractice.com/index.php"
facebook_url = "https://www.facebook.com"
ecommerce_url = "https://demo.nopcommerce.com/register?returnUrl=%2F"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(ecommerce_url)

driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

#links = driver.find_elements(By.TAG_NAME,'a')

# print(len(links))
# tag can be optional but value is mandatory.
txtUsername_css= driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")
time.sleep(4)
txtUsername_css= driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")

txtUsername_css= driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")

txtUsername_css= driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")