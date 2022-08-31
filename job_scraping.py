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
with open('job_scraping.csv','w', encoding='utf-8-sig') as file:
    file.write("Job_title; Location; Salary; Company_name; Job_description \n")

#driver=webdriver.Chrome( executable_path='C:\\Users\\User\\Downloads\\webdrivers\\chromedriver.exe')
driver=webdriver.Chrome(executable_path='C:\\Users\\\Administrator\\Downloads\\webdrivers\\chromedriver.exe')


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

locations=driver.find_elements("xpath", "//li[@class='sc-fznXWL hSqkJy']")

published=driver.find_elements("xpath","//li[@class='sc-fznXWL jwFgqb']")

salaries=driver.find_elements("xpath","//dl[@class='sc-fzoJMP jpodhy']")

companies=driver.find_elements("xpath", "//div[@class='sc-fzoiQi kuzZTz']")

job_details=driver.find_elements("xpath", "//a[@data-offer-meta-text-snippet-link='true']")


print(len(locations))
print(len(published))
print(len(salaries))
print(len(job_details))
    
#specifying number of pages we're scraping from (from pagination)
for i in range(3):
    titles=driver.find_elements("xpath",'//div[@class="sc-fzooss kBgtGS"]/a/h2') 

    locations=driver.find_elements("xpath", "//li[@class='sc-fznXWL hSqkJy']")

    published=driver.find_elements("xpath","//li[@class='sc-fznXWL jwFgqb']")

    salaries=driver.find_elements("xpath","//dl[@class='sc-fzoJMP jpodhy']")

    companies=driver.find_elements("xpath", "//div[@class='sc-fzoiQi kuzZTz']")

    job_details=driver.find_elements("xpath", "//a[@data-offer-meta-text-snippet-link='true']")
    #mode is append, because we are appending list elements to the file
    with open('job_scraping.csv','a', encoding='utf-8-sig') as file:
        for i in range(len(titles)):
            file.write(titles[i].text+ ";" + locations[i].text + ";" + salaries[i].text + ";" + companies[i].text + ";" + job_details[i].text + '\n')
        next=driver.find_element("xpath", "//a[@data-at='pagination-next']")
        next.click()
    file.close()