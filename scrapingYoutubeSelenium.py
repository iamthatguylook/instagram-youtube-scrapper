from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from dotenv import load_dotenv
from pathlib import Path
import os
import time


dotenv_path = Path("./config.env")

load_dotenv(dotenv_path=dotenv_path)

readSubscriberFile = open("subscribers.txt", "r")
subscribers = []
for subscriber in readSubscriberFile:
    subscribers.append(subscriber)

print(subscribers)

driver = webdriver.Firefox()
driver.get("https://youtube.com/")


for subscriber in subscribers:

    searchBar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
    searchBar.clear()
    searchBar.send_keys(subscriber)

    searchBarButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='search-icon-legacy']")))
    ActionChains(driver).click(
        searchBarButton).perform()

    time.sleep(2)

    filterButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Search filters']")))
    filterButton.click()

    searchForLastHour = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@title='Search for Last hour']")))
    searchForLastHour.click()

    time.sleep(5)
