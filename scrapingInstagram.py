from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import datetime
import dateutil.relativedelta
from instalooter.looters import InstaLooter, ProfileLooter
import instaloader
from instalooter.cli.login import login

url_to_scrape = "https://practice.geeksforgeeks.org/courses/"
dotenv_path = Path("./config.env")

load_dotenv(dotenv_path=dotenv_path)
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

print(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)


def getHtmlDocument(url_to_scrape):
    response = requests.get(url_to_scrape)
    return response.text


html_document = getHtmlDocument(url_to_scrape)
soup = BeautifulSoup(html_document, 'html.parser')

print(soup.title)

def scrapevideos(output_Folder='./outputFolder', days=1):
    loadInstaloader = instaloader.Instaloader()
    loadInstaloader.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    profile = instaloader.Profile.from_username(
        loadInstaloader.context, INSTAGRAM_USERNAME)
    following = profile.get_followees()

    for followee in following:  # print all followers
        print(followee)
        followeeLooter = ProfileLooter(
            followee.username, videos_only=True, template="{id}-{username}-{width}-{height}")
        if not followeeLooter.logged_in():
            followeeLooter.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
        print("Getting videos from " + followee.username)
        today = datetime.date.today()
        timeframe = (today, today -
                     dateutil.relativedelta.relativedelta(days=days))
        numDowloaded = followeeLooter.download(
            output_Folder, media_count=30, timeframe=timeframe)
        print("Downloaded " + str(numDowloaded) + " videos successfully")
        print("")


scrapevideos('./outputFolder',1)
