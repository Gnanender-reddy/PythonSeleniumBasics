"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has drop downs concept.
"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/profile/user-registration")
#time.sleep(1)
element=driver.find_element_by_xpath("/html[1]/body[1]/app-root[1]/app-home[1]/div[2]/div[1]/app-user-registration[1]/div[2]/div[1]/div[2]/div[4]/form[1]/div[5]/div[2]/p-dropdown[1]/div[1]/div[3]")
drop=Select(element)
drop.select_by_visible_text("What is your pet name")
