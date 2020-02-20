"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has alert pop ups concept.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("http://testautomationpratice.blogspot.com")
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
#driver.switch_to_alert().accept()#closes the alert window by clicking the ok button
driver.switch_to_alert().dismiss()#closes the alert window  by clicking the cancel button

