from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://courses.thetestingacademy.com/")
print(driver.title)
driver.close()