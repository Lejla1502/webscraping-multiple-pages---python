from selenium import webdriver
import time

#define Chrome driver -- first download Chrome webdriver based on the version of Chrome
#Link : https://chromedriver.chromium.org/downloads

driver=webdriver.Chrome(executable_path='C:\Users\Administrator\Downloads\webdrivers\chromedriver.exe')

#define from which web page we're scraping
driver.get('https://www.jobsite.co.uk/')