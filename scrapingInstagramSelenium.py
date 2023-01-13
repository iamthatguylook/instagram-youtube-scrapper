from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path("./config.env")

load_dotenv(dotenv_path=dotenv_path)
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

driver=webdriver.Firefox()
driver.get("https://instagram.com")

try:
    usernameElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    usernameElement.send_keys(INSTAGRAM_USERNAME)
    
    passwordElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    passwordElement.send_keys(INSTAGRAM_PASSWORD)
    passwordElement.send_keys(Keys.RETURN)

    notNowElement =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Not Now')]"))) 
    notNowElement.click()
    
    notNowNotificationsButton =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Not Now')]"))) 
    notNowNotificationsButton.click()

    profileButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"_aaav"))) 
    profileButton.click()

    profileButton2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Profile')]"))) 
    profileButton2.click()

    followingButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'following')]"))) 
    followingButton.click()
    followingProfiles =[]
    followingProfiles = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"_aano")))
    
    for element in followingProfiles:
        for divs in element:
            print(divs)

except:
    print(followingProfiles)
