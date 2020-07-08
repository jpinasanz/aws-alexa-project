import re
import sys
import numpy as np
from moviepy.tools import cvsecs
from moviepy.video.VideoClip import TextClip, VideoClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip
#FiletobeCaptioned is a .mov or .mp4 I believe


def makesubtitle(SRTFile,FiletobeCaptioned):

    #Check to see whihc type of file. MP3,Mp4 ect
    generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=24, color='white')
    sub = SubtitlesClip(SRTFile, generator)
    myvideo = VideoFileClip(FiletobeCaptioned)
    final = CompositeVideoClip([myvideo, sub.set_pos(('center','bottom'))])
    final.write_videofile(FiletobeCaptioned + "_MP4.mp4", fps=myvideo.fps, codec='libx264')


if __name__ == '__main__':
    makesubtitle(*sys.argv[1:])