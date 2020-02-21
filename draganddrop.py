"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has mouse drag and drop actions concept.
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
source_element=driver.find_element_by_xpath("//*[@id='box6']")
target_element=driver.find_element_by_xpath("//*[@id='box106']")
action=ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()