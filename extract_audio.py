import os
import sys
import re
from moviepy.editor import VideoFileClip


def extract_audio(input_video, output_audio):
    video_clip = VideoFileClip(input_video)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio, codec='mp3')


if __name__ == "__main__":
    pwd = os.getcwd()
    cmd_args = sys.argv

    file_root = re.sub(re.compile('.mp4$'), '', cmd_args[1])
    input_video_file = os.path.join(pwd, cmd_args[1])
    output_audio_file = os.path.join(pwd, f'{file_root}.mp3')
    extract_audio(input_video_file, output_audio_file)
