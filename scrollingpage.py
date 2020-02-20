"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has scrolling pages concept.
"""

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
#scrolling the page by pixel
driver.execute_script("window.scrollBy(0,1000)","")
#scrolling the page till the element found
flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[41]/td[2]")
driver.execute_script("arguments[0].scrollIntoView();",flag)
#scroll down till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
