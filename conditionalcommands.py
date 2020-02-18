import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/profile/user-registration")
element=driver.find_element_by_name("email")
print(element.is_displayed())
print(element.is_enabled())

# element1=driver.find_element_by_name("pass")
# print(element1.is_displayed())
# print(element1.is_enabled())
# element.send_keys("0000")
# element1.send_keys("00000")
# driver.find_element_by_id('u_0_4').click()
# time.sleep(3)
