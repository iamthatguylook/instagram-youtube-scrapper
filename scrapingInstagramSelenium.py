from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://instagram.com")

usernameField = driver.find_element(By.NAME, "username")
print(usernameField)
print(driver.title)