# instagram-youtube-scrapper

# Step 1 Create virual enviornment

pip install virtualenv
python -m virtualenv <nameOfEnv>
Activate virtualenv with <nameOfEnv>\Scripts\activate

# Step 2 Install necessary packages for scrapping after activating env

beautifulSoup4 - https://beautiful-soup-4.readthedocs.io/en/latest/
pip install beautifulsoup4

# Step 3 - To install necessary packages that are in requirements

pip install -r requirements.txt

# Step 4 - Use documentation of InstaLoader and Instalooter to download vides of your following.

First you login then you iterate through your following take each following download the posts from each
following based on date. This did not work cause apparently the packages have been discontinued.
So are next solution will be use a webdriver and use selenium to create our scrapper.

# Step 5 - Use webdriver To go to instagram

LOGIC - manually use the webdriver to search Instagram url, go to login page, select each input field
and enter the details accordingly then either press enter using selenium or click on the login button.

Once thats done in the code we must go through following list and open each followee in different tab
in order to download the videos in a particular folder related to the following from each window.

# One small issue

The following number for now is hardcoded the way to tackle this would be take the follower number from the html -span or div whatever the html might using selenium inner html feature then we could store that as a variable but the problem with this lets say you are following 200 people you would open 200 tabs with your bot account which is poor feature.

The more efficient thing would be to have list of urls from where you would scrape from or list of followers then you would open only those tabs and scrape videos from that day. ---> I will make future script for this now ill just hardcode to get the basic functionality running

# second issue

Instagram keeps detecting seleniums behaviour and considers it a bot. This second issue that needs to fixed. Cannot make 100 accounts just to finish project that regardless will get banned. We must find other sources other than instagram we can use youtube channel that would post shorts and take those shorts and compile them that seems more feasible.

# Step 6 - Instead of Instagram we download from youtube from the people we will search

Since Instagram blocks all the selenium bots, Next I will see a way to evade all bot detection using proxy or another method. For now I first search on youtube without signing in and scrape videos based on recent uploads on the subject we search. We download with highest resolution possible and store in the outputFolder. We use two new imports one is pytube and the other is shutil(for major os operations)

# Step 7 - Once all the windows are downloaded we must close the driver

using driver.close()
