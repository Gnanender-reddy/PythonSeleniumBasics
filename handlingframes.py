"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has handling frames concept.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.switch_to.frame("packageListFrame")#first frame
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")#second frame
driver.find_element_by_xpath("/html/body/div/ul/li[1]/a").click()
driver.close()
