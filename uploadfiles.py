"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has uploading files concept.
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("/home/admin1/Pictures/Screenshot from 2019-05-21 14-50-32.png")
