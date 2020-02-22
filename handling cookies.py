from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
#capture the cookies
cookies=driver.get_cookies()
print(cookies,len(cookies))
#adding new cookies
cookies={'name':'mycookie','value':'122'}
driver.add_cookie(cookies)
cokk=driver.get_cookies()
print(cokk,len(cokk))
#deleting cookies
driver.delete_cookie("mycookie")
cookiesss=driver.get_cookies()
print(len(cookiesss))
#for deleting all cookies use delete all cookies method.
