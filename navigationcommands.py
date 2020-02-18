import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://newtours.demoaut.com/")
time.sleep(2)
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(2)

print(driver.title)
driver.back()
time.sleep(2)

print(driver.title)
driver.forward()
time.sleep(2)

print(driver.title)
