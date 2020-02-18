"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics.
"""


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://github.com/login")
# print(driver.title) #it returns the title of the page
# print(driver.current_url) #it returns the current url of the page
driver.find_element_by_xpath("//*[@id='login']/form/div[3]/input[9]").click()
time.sleep(2)
driver.quit()