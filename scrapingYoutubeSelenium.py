from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from dotenv import load_dotenv
from pathlib import Path
import os
import wget
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

downloadPath = os.getcwd()
downloadPath = os.path.join(downloadPath, "outputFolder")
os.mkdir(downloadPath)

print(downloadPath)

for subscriber in subscribers:

    subscriberName = subscriber.replace(" ", "")

    subscriberVideoDownloadPath = os.path.join(
        downloadPath, subscriberName.replace("\n", ""))
    os.mkdir(subscriberVideoDownloadPath)

    searchBar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
    searchBar.clear()
    searchBar.send_keys(subscriber)

    time.sleep(2)

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

    videosOnPage = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[@id='thumbnail']")))

    numberOfDownloads = 5
    linksOfVideos = []
    try:
        for videoNumber in range(numberOfDownloads):
            linksOfVideos.append(
                videosOnPage[videoNumber].get_attribute('href'))
            # ActionChains(driver).click(videosOnPage[videoNumber]).perform()
        print(linksOfVideos)

        videoCounter = 1
        for videoLink in linksOfVideos:
            if videoLink == None:
                print('There was None here')
                continue
            else:
                subscriberName = subscriberName.replace("\n", "")
                print(subscriberName)
                saveVideo = os.path.join(
                    subscriberVideoDownloadPath, subscriberName + '_video_' + str(videoCounter))
                wget.download(videoLink, saveVideo)
                videoCounter += 1

    except:
        print('yea there is error')

    time.sleep(5)
