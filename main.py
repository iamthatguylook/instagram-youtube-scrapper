from scrapingYoutubeSelenium import scrapeYoutubeVideos
from compilingVideo import makeCompilationOfEachFolder
import os
from os.path import isfile, join

scrapeYoutubeVideos()
makeCompilationOfEachFolder('outputFolder')
