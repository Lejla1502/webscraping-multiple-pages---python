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

# company_list={}
# company_index=0
# processing_companies=True

# while processing_companies:
#     companies=driver.find_elements('xpath','//div[@class="rt-accordion-item"]')
#     if(company_index<len(companies)):
#         companies[company_index].click()
#         time.sleep(5)
#         listParagraphs=companies[company_index].find_elements(By.CSS_SELECTOR, ".content p")
#         listNamesCompanies.append(listParagraphs[1].text)
#         listDjelatnosti.append(listParagraphs[4].text)
#         company_index+=1
#     else:
#         processing_companies=False

# for nn in listNamesCompanies:
#     print(nn)

for item in item_to_be_clicked:
    item.click()
    time.sleep(2)
    #ttl=item.find_element(By.CSS_SELECTOR, "p")
    #listNamesCompanies.append(ttl)
    listParagraphs=item.find_elements(By.CSS_SELECTOR, ".content p")
    listNamesCompanies.append(listParagraphs[1].text)
    listDjelatnosti.append(listParagraphs[4].text)
    listOfTextsSixthParagraphInAccordion.append(listParagraphs[5].text)
    
    #.find_elements(By.CSS_SELECTOR, "p")
    #print(driver.execute_script('return arguments[0].lastChild.textContent;', WebDriverWait(driver, 20).until(EC.visibility_of_element_located(listParagraphs[5].find_elements(By.CSS_SELECTOR, "p strong")))))
    #print(driver.execute_script('return arguments[0].lastChild.textContent;', listParagraphs[5].find_element(By.CSS_SELECTOR, "p strong")))
    #print(listParagraphsAddress.text.splitlines()[1])
    #print(listParagraphsAddress.text.splitlines()[2])
    #print(listParagraphsAddress.text.splitlines()[4])
    #splitLastParagraph=listParagraphsAddress.text.splitlines()
    #listCities.append(city)
    #listPhoneNumbs.append(phone)
    #listMobileNumbs.append(mobile)
    #title=driver.find_element('xpath','//div[@class="content"]/p[2]')
    #print(ttls[2].text)
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="rt-accordion-item]'))).click()

for l in listOfTextsSixthParagraphInAccordion:
    newel=l.splitlines()
    if len(newel)>0:
        print(l.splitlines()[2])



    #listCities.append(l.splitlines()[2])
#for lc in listCities:
#    print(lc)

# accorddionLinks=driver.find_elements('xpath','//p[@class="title"]')
# for cl in accorddionLinks:
#     cl.click()

# #getting full company name
# listCompanies= driver.find_element('xpath','//div[@class="content"]/p[2]')
# print(listCompanies)

# #getting djelatnost
# listDjelatnost=driver.find_elements('xpath','//div[@class="content"]/p[5]')

# #getting city 
# ListCities= driver.find_elements('xpath', '//div[@class="content"]/p[6]/strong[2]')

# #getting phone
# listPhoneNums =driver.find_elements('xpath', '//div[@class="content"]/p[6]/strong[3]')

# #getting mobile num
# listMobileNums =driver.find_elements('xpath', '//div[@class="content"]/p[6]/strong[5]')

# with open('newfile.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     thewriter = writer(f)
#     header = ['Title']
#     thewriter.writerow(header)
#     for list in listCompanies:
#         thewriter.writerow(list.text)


