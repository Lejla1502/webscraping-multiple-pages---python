from random import getrandbits
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


#download Python (this is interpreter) --> version 3.9 needed
#download chromedriver
#install Python extension in VS Code
#python -m ensurepip
#install packages with pip in terminal

#define Chrome driver -- first download Chrome webdriver based on the version of Chrome
#Link : https://chromedriver.chromium.org/downloads

#declaring in which csv file we're inputing data
#the second parameter is the mode we want to work with - here we chose writing and adding
with open('job_scraping_pager.csv','w', encoding='utf-8-sig') as file:
    file.write("Job_title; Location; Salary; Company_name; Job_description \n")

#pages can recognize selenium and deny access
#we use options to workaround that blockage and be able to still scrape data we need
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(options=options, executable_path='C:\\Users\\User\\Downloads\\webdrivers\\chromedriver.exe')
#driver=webdriver.Chrome(executable_path='C:\\Users\\\Administrator\\Downloads\\webdrivers\\chromedriver.exe')


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


dropdown=driver.find_element('id','Radius')
radius=Select(dropdown)
radius.select_by_visible_text("30 miles")


submitBtn=driver.find_element("xpath",'//input[@Value="Search"]')
submitBtn.click()

time.sleep(6)
#getting three layers deep to get that title list
titles=driver.find_elements("xpath",'//div[@class="sc-fzooss kBgtGS"]/a/h2') 


elThatContainsTotal=driver.find_element("xpath","//div[@class='ResultsContainer-sc-1rtv0xy-2 dmSilN']")
totalElNum=elThatContainsTotal.get_attribute("data-resultlist-offers-total")
totalPages=round(int(totalElNum)/len(titles))
#we need to round this to closest integer number so that we can loop through 
print(totalPages)
#specifying number of pages we're scraping from (from pagination)
for i in range(totalPages):
    titles=driver.find_elements("xpath",'//div[@class="sc-fzooss kBgtGS"]/a/h2') 

    locations=driver.find_elements("xpath", "//li[@class='sc-fznXWL hSqkJy']")

    published=driver.find_elements("xpath","//li[@class='sc-fznXWL jwFgqb']")

    salaries=driver.find_elements("xpath","//dl[@class='sc-fzoJMP jpodhy']")

    companies=driver.find_elements("xpath", "//div[@class='sc-fzoiQi kuzZTz']")

    job_details=driver.find_elements("xpath", "//a[@data-offer-meta-text-snippet-link='true']")
    needed_page=i+2
    #mode is append, because we are appending list elements to the file
    with open('job_scraping_pager.csv','a', encoding='utf-8-sig') as file:
        for i in range(len(titles)):
            file.write(titles[i].text+ ";" + locations[i].text + ";" + salaries[i].text + ";" + companies[i].text + ";" + job_details[i].text + '\n')
        str_i=str(needed_page)                   #"//a[@data-at='pagination-page-link pagination-page-link-2]"
        print(str_i)
        btn=driver.find_element("xpath","//a[@data-at='pagination-page-link pagination-page-link-"+str_i+"']")
        btn.click()
        time.sleep(2)
    file.close()
driver.close()