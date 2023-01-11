# instagram-youtube-scrapper

# Step 1 Create virual enviornment

pip install virtualenv
python -m virtualenv <nameOfEnv>
Activate virtualenv with <nameOfEnv>\Scripts\activate

# Step 2 Install necessary packages for scrapping after activating env

beautifulSoup4 - https://beautiful-soup-4.readthedocs.io/en/latest/
pip install beautifulsoup4

# Step 3 - To install necessary packages that are in requirements

# Step 4 - Use documentation of InstaLoader and Instalooter to download vides of your following.

First you login then you iterate through your following take each following download the posts from each
following based on date. This did not work cause apparently the packages have been discontinued.
So are next solution will be use a webdriver and use selenium to create our scrapper.
