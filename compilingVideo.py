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
                              remove_temp=True)
