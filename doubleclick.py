"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has mouse double clicking actions concept.
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
element=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
action=ActionChains(driver)
action.double_click(element).perform()