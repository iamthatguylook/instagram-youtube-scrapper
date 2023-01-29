from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.resize import resize
import os
from os.path import isfile, join
import random
import shutil


def makeCompilation(videoPath, outputFile):
    videosInPath = []

    for fileName in os.listdir(videoPath):

        filePath = join(videoPath, fileName)
        if isfile(filePath) and fileName.endswith('.mp4'):
            videoClip = VideoFileClip(filePath)
            videoClip = videoClip.resize(width=1920)
            videoClip = videoClip.resize(height=1080)
            videosInPath.append(videoClip)

    finalClip = concatenate_videoclips(videosInPath, method='compose')
    finalClip.write_videofile(outputFile, threads=8,
                              remove_temp=True, codec="libx264")


def makeCompilationOfEachFolder(mainFolder):
    downloadPath = os.getcwd()
    # Adds new path outputFolder to it
    downloadPath = os.path.join(downloadPath, mainFolder)
    for folder in os.listdir(downloadPath):
        print(folder)
        folderPath = os.path.join(downloadPath, folder)
        fileNameForOutput = folder + '.mp4'
        fileLocation = os.path.join(downloadPath, fileNameForOutput)
        makeCompilation(folderPath, fileLocation)
