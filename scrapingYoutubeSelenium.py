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
from pytube import YouTube
import shutil


def scrapeYoutubeVideos():
    dotenv_path = Path("./config.env")

    load_dotenv(dotenv_path=dotenv_path)

    # Reads subscribers file where we assosicate search terms with the people who we subscribe
    readSubscriberFile = open("subscribers.txt", "r")
    subscribers = []
    for subscriber in readSubscriberFile:                                   # Loads subscribers into list
        subscribers.append(subscriber)

    print('The List of subscribers are ', subscribers)

    # Loads webdriver to connect to url thats given
    driver = webdriver.Firefox()
    driver.get("https://youtube.com/")

    # Gets current Path
    downloadPath = os.getcwd()
    # Adds new path outputFolder to it
    downloadPath = os.path.join(downloadPath, "outputFolder")

    # If the Path outputFolder exists in current directory it will delete and recreate it as we dont want have have the old videos as they were previously scrapped
    if os.path.exists(downloadPath):
        shutil.rmtree(downloadPath)     # shutil removes the directory
        os.mkdir(downloadPath)          # Creates the directory
    else:
        os.mkdir(downloadPath)          # Creates the directory

    for subscriber in subscribers:  # iterates through subscribers

        subscriberName = subscriber.replace(" ", "")

        subscriberVideoDownloadPath = os.path.join(
            downloadPath, subscriberName.replace("\n", ""))             # Creates directory for each subscriber
        os.mkdir(subscriberVideoDownloadPath)

        print(subscriberName)

        searchBar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))    # Select search bar element
        searchBar.clear()
        # Send the name of the subscriber
        searchBar.send_keys(subscriber)

        time.sleep(2)

        searchBarButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='search-icon-legacy']")))   # Finds button with search icon to search
        ActionChains(driver).click(
            searchBarButton).perform()

        time.sleep(2)

        filterButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Search filters']")))   # Clicks on filter button
        filterButton.click()

        searchForLastHour = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@title='Search for Last hour']")))      # Finds button with filter for last hour
        searchForLastHour.click()

        time.sleep(2)

        videosOnPage = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@id='video-title']")))               # Find all the videos with on the page that were posted in the last hour

        linksOfVideos = []

        try:
            # number of videos to download
            numberOfDownloads = 5
            videoNumber = 0
            for videoNumber in range(numberOfDownloads):
                linksOfVideos.append(
                    videosOnPage[videoNumber].get_attribute('href'))                # Iterates and gets link of each selenium object
                # ActionChains(driver).click(videosOnPage[videoNumber]).perform()
            print(linksOfVideos)

            videoCounter = 1
            for videoLink in linksOfVideos:
                if videoLink == None:
                    print('There was None here')
                    continue
                else:
                    video = YouTube(videoLink)
                    print(video.title)
                    saveVideo = os.path.join(
                        subscriberVideoDownloadPath)                                # Downloads with highest resolution
                    video = video.streams.get_highest_resolution()

                    # Downloads in certain path
                    video.download(saveVideo)
                    # subscriberName = subscriberName.replace("\n", "")
                    # print(subscriberName)
                    # saveVideo = os.path.join(
                    #     subscriberVideoDownloadPath, subscriberName + '_video_' + str(videoCounter))
                    # wget.download(videoLink, saveVideo)
                    # videoCounter += 1

        except:
            print('Error will downloading the video')

        videosOnPage = 0   # Clears video list
        time.sleep(5)
