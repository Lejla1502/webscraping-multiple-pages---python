from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from csv import writer

#to work with accordian
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#define Chrome driver -- first download Chrome webdriver based on the version of Chrome
#Link : https://chromedriver.chromium.org/downloads

#driver=webdriver.Chrome(executable_path='C:\\Users\\User\\Downloads\\webdrivers\\chromedriver.exe')
driver=webdriver.Chrome(executable_path='C:\\Users\\\Administrator\\Downloads\\webdrivers\\chromedriver.exe')


#define from which web page we're scraping
driver.get('https://www.pkzedo.ba/ba/registar.php')

driver.maximize_window()

#wait for one second
time.sleep(1)

#getting value from dropdown - here we've chosen value 20
djelatnost=driver.find_element('name','djelatnost')
radiusVal=Select(djelatnost)

radiusVal.select_by_value("20")
time.sleep(1)


submitBtn=driver.find_element('xpath','//input[@Value="Pretraga"]')
submitBtn.click()


#-------------------------------------------ACCORDION---------------------------------
item_to_be_clicked=driver.find_elements('xpath','//div[@class="rt-accordion-item"]')

#defining lists of the things we want to extract
listNamesCompanies=[]
listDjelatnosti=[]
listCities=[]
listPhoneNumbs=[]
listMobileNumbs=[]
listOfTextsSixthParagraphInAccordion=[]

company_list={}
company_index=0
processing_companies=True

while processing_companies:
    companies=driver.find_elements('xpath','//div[@class="rt-accordion-item"]')
    if(company_index<len(companies)):
        companies[company_index].click()
        time.sleep(5)
        listParagraphs=companies[company_index].find_elements(By.CSS_SELECTOR, ".content p")
        listNamesCompanies.append(listParagraphs[1].text)
        listDjelatnosti.append(listParagraphs[4].text)
        company_index+=1
    else:
        processing_companies=False

for nn in listNamesCompanies:
    print(nn)


