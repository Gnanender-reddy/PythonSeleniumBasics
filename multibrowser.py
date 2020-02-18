from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
print(driver.title)
print(driver.current_url)#it returns the url
print(driver.page_source) #it returns the html code of that page
driver.close()