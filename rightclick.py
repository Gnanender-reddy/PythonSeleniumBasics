"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has mouse right clicking actions concept.
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("http://swisn1.github.io/jquery-contextmenu/demo.html")
driver.maximize_window()
button=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
action=ActionChains(driver)
action.context_click().perform()