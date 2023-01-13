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

# Step 6 - Once all the windows are downloaded we must close the driver

using driver.close()
