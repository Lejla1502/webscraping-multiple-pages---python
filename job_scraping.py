from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

#define Chrome driver -- first download Chrome webdriver based on the version of Chrome
#Link : https://chromedriver.chromium.org/downloads

driver=webdriver.Chrome(executable_path='C:\\Users\\Administrator\\Downloads\\webdrivers\\chromedriver.exe')

#define from which web page we're scraping
driver.get('https://www.jobsite.co.uk/')

driver.maximize_window()

#wait for one second
time.sleep(1)

#build xpath expression for "accept all" cookies button
cookie= driver.find_element("xpath",'//div[@class="privacy-prompt-button primary-button ccmgt_accept_button "] ')

try:
    cookie.click()
except:
    pass



#we need to simulate the steps we would make on the page when doing the search
job_title=driver.find_element('id','keywords')

job_title.click()

job_title.send_keys('Software Engineer')  #searching by Software Engineer keyword 
time.sleep(1)


location=driver.find_element("id","location")
location.click()
location.send_keys('Manchester')
time.sleep(1)


dropdown=driver.find_element('id','Radius')
radius=Select(dropdown)
radius.select_by_visible_text("30 miles")
time.sleep(1)


submitBtn=driver.find_element("xpath",'//input[@Value="Search"]')
submitBtn.click()

