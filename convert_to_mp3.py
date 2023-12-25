import sys
import os
import subprocess
from pydub import AudioSegment
from pydub.exceptions import PydubException


def convert_to_mp3(input_file_, output_file_):
    try:
        # Load the audio file
        subprocess.run(['ffmpeg', '-i', input_file_, output_file_])
        # audio = AudioSegment.from_file(input_file_)

        # Export as MP3
        # audio.export(output_file_, format="mp3")

        print(f"Conversion successful. MP3 file saved as {output_file_}")

    except PydubException as e:
        print(f"Error during conversion: {e}")


if __name__ == "__main__":
    # # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python convert_to_mp3.py input_file")
        sys.exit(1)

    # Get the input file from the command line argument
    input_file = sys.argv[1]
    # input_file = r'/home/franks/Downloads/Symphony No.6 (1st movement).m4a'
    # input_file = r'/home/franks/Documents/Podcasts/日谈公园/440. 疫情打不垮环球航海心，两年之后他再度启航.m4a'
    file_base_name = os.path.basename(input_file)
    file_name, file_extension = os.path.splitext(file_base_name)
    pwd = os.getcwd()

    # Output file will have the same name with a .mp3 extension
    output_file = os.path.join(pwd, f'{file_name}.mp3')

    convert_to_mp3(input_file, output_file)
