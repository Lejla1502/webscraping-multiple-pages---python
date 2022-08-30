from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

#define Chrome driver -- first download Chrome webdriver based on the version of Chrome
#Link : https://chromedriver.chromium.org/downloads

driver=webdriver.Chrome(executable_path='C:\\Users\\Administrator\\Downloads\\webdrivers\\chromedriver.exe')

#define from which web page we're scraping
driver.get('https://www.pkzedo.ba/ba/registar.php')

driver.maximize_window()

#wait for one second
time.sleep(3)


djelatnost=driver.find_element('name','djelatnost')
radiusVal=Select(djelatnost)

radiusVal.select_by_value("20")
time.sleep(3)


submitBtn=driver.find_element('xpath','//input[@Value="Pretraga"]')
submitBtn.click()