"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has screen shots concept.
"""
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://swisn1.github.io/jquery-contextmenu/demo.html")
driver.maximize_window()
driver.save_screenshot("/home/admin1/Pictures/screenshots/home.png")
#driver.get_screenshot_as_file("/home/admin1/Pictures/screenshots/home121.png")