"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has downloading files  in chrome concept.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#to change the chrome settings for downloading files
# chromeoptions=Options()
# chromeoptions.add_experimental_option("prefs",{"download.default_directory":"home/admin/Downloads"})
driver=webdriver.Chrome(chromeoptions=chromeoptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
#download text file
driver.find_element_by_id("textbox").send_keys("testng download fie")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
#download pdf file
driver.find_element_by_id("pdfbox").send_keys("testng download fie")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

