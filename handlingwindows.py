"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has handling browsers windows concept.
"""

from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
handles=driver.window_handles
print(handles,"---------->")
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
driver.quit()