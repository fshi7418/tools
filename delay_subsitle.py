import os
import re
from datetime import datetime, timedelta


def delay_subtitles(input_file, output_file, delay_seconds):
    """
    Delays all timestamps in a subtitle file by a specified amount of seconds.

    Args:
        input_file: Path to the input subtitle file
        output_file: Path to the output subtitle file
        delay_seconds: Number of seconds to delay (can be float for milliseconds)
    """
    # Convert delay to timedelta
    delay = timedelta(seconds=delay_seconds)

    # Regular expression to match timestamp lines
    timestamp_pattern = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})')

    with open(input_file, 'r', encoding='utf-8') as infile, \
            open(output_file, 'w', encoding='utf-8') as outfile:

        for line in infile:
            # Check if this line contains timestamps
            match = timestamp_pattern.search(line)
            if match:
                # Parse start and end times
                start_str, end_str = match.groups()

                # Convert strings to datetime objects
                start_time = datetime.strptime(start_str, '%H:%M:%S,%f')
                end_time = datetime.strptime(end_str, '%H:%M:%S,%f')

                # Add delay
                new_start = start_time + delay
                new_end = end_time + delay

                # Format back to string
                new_start_str = new_start.strftime('%H:%M:%S,%f')[
                                :-3]  # Remove last 3 digits to keep milliseconds as 3 digits
                new_end_str = new_end.strftime('%H:%M:%S,%f')[:-3]

                # Replace the timestamps in the line
                new_line = f"{new_start_str} --> {new_end_str}\n"
                outfile.write(new_line)
            else:
                # Write the line unchanged
                outfile.write(line)


if __name__ == "__main__":
    os.chdir(r'/home/franks/Videos/阮玲玉（1991）')
    # Example usage
    input_file_ = "阮玲玉（1991）.srt"  # Change to your input file
    output_file_ = "output.srt"  # Change to your desired output file
    delay_seconds_ = 15

    delay_subtitles(input_file_, output_file_, delay_seconds_)
    print(f"Subtitles delayed by {delay_seconds_} seconds and saved to {output_file_}")