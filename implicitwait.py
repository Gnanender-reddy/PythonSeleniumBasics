import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/profile/user-registration")
driver.implicitly_wait(10)
element=driver.find_element_by_name("userName")
print(element.is_displayed())
print(element.is_enabled())

element1=driver.find_element_by_name("usrPwd")
print(element1.is_displayed())
print(element1.is_enabled())
Male_radio=driver.find_element_by_css_selector("input[value=M]")
print(Male_radio.is_selected(),"------------>")#it checks the status of radio button
driver.close()