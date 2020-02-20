"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has web tables concept.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("file:///c:/SeleniumPractice/sample.html")
rows=len(driver.find_element_by_xpath("/html/body/table/tbody/tr"))
columns=len(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th"))
print(rows)
print(columns)
for r in range(2,rows+1):
    for c in range(1,columns+1):
        value=driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end=' ')
    print()
