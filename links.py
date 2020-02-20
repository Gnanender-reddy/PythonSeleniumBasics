"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has drop downs concept.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("http://newtours.demoaut.com")
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    print(link.text)   #This text extracts the value of the link
#clicking on the links
driver.find_element(By.LINK_TEXT,"REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()