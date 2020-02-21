"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has mouse hover actions concept.
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermanagement=driver.find_element_by_id("menu_admin_UserManagement")
user=driver.find_element_by_id("menu_admin_viewSystemUsers")
#to do mouse hover actions we have to use actions chains class
#create an object of actions chains class
Action=ActionChains(driver)
Action.move_to_element(admin).move_to_element(usermanagement).move_to_element(user).click().perform()