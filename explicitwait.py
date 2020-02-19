"""
@Author : P.Gnanender Reddy
@Since : Feb'2020
@keywords: selenium.
@Description:This code is for python selenium basics which has explicit wait concept.
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.expedia.co.in/?AFFCID=IN.NETWORK.OMG.1868522.HOTEL-TEXTLINK&sskey=5974d8550c604078a4a2b06183c966eb")
    #driver.find_element_by_id("tab-flight-tab-hp") or below line also we can use
    driver.find_element(By.ID,"tab-flight-tab-hp").click() #it clicks on flights button

    driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")#origin
    time.sleep(4)
    driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYc")#destination
    driver.find_element(By.ID,"flight-departing-hp-flight").clear()

    driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("22/02/2020")
    driver.find_element(By.ID,"flight-returning-hp-flight").clear()
    driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("22/02/2020")
    driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()
    #explicit waits
    wait=WebDriverWait(driver,10)
    element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0]")))
    element.click()
    driver.close()
if __name__ == '__main__':
    main()