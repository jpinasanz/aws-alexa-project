import re
import numpy as np
from moviepy.tools import cvsecs
from moviepy.video.VideoClip import TextClip, VideoClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip

def main():
    generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=24, color='white')
    sub = SubtitlesClip("Output.srt", generator)
    myvideo = VideoFileClip("transcribe-sample Movie.mov")
    final = CompositeVideoClip([myvideo, sub.set_pos(('center','bottom'))])
    final.write_videofile("transcribe-sample_MP4.mp4", fps=myvideo.fps, codec='libx264')


if __name__ == '__main__':
    main()