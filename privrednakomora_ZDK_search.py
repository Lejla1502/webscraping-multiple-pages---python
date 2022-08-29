from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

#define Chrome driver -- first download Chrome webdriver based on the version of Chrome
#Link : https://chromedriver.chromium.org/downloads

driver=webdriver.Chrome(executable_path='C:\Users\Administrator\Downloads\webdrivers\chromedriver.exe')

#define from which web page we're scraping
driver.get('https://www.jobsite.co.uk/')

driver.maximize_window()

#wait for one second
time.sleep(1)


djelatnost=driver.find_element_by_name('djelatnost')
radiusVal=Select(djelatnost)