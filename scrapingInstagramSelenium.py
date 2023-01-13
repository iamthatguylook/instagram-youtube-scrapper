from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path("./config.env")

load_dotenv(dotenv_path=dotenv_path)
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

driver=webdriver.Firefox()
driver.get("https://instagram.com")
doubleClickAction = ActionChains(driver)
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
    followingProfiles = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd']")))
    for followee in  followingProfiles:
        doubleClickAction.keyDown(Keys.LEFT_CONTROL).click(followee)
        #doubleClickAction.double_click(followee).perform() to perform double clicks
        print(followee)
        break
        
except:
    print('Hey there is an error')
