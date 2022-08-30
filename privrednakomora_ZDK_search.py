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

driver=webdriver.Chrome(executable_path='C:\\Users\\User\\Downloads\\webdrivers\\chromedriver.exe')

#define from which web page we're scraping
driver.get('https://www.pkzedo.ba/ba/registar.php')

driver.maximize_window()

#wait for one second
time.sleep(3)

#getting value from dropdown - here we've chosen value 20
djelatnost=driver.find_element('name','djelatnost')
radiusVal=Select(djelatnost)

radiusVal.select_by_value("20")
time.sleep(3)


submitBtn=driver.find_element('xpath','//input[@Value="Pretraga"]')
submitBtn.click()


#-------------------------------------------ACCORDION---------------------------------
item_to_be_clicked=driver.find_elements('xpath','//div[@class="rt-accordion-item"]')

listNamesCompanies=[]
for item in item_to_be_clicked:
    item.click()
    time.sleep(2)
    ttl=item.find_element(By.TAG_NAME, "p")
    listNamesCompanies.append(ttl)
    #title=driver.find_element('xpath','//div[@class="content"]/p[2]')
    print(ttl.text)
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="rt-accordion-item]'))).click()

for lc in listNamesCompanies:
    print(lc.text)

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

