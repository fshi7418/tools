import wave
import os


def partition_audio(input_file_, input_path_, max_file_size):
    file_base_name = os.path.basename(input_file_)
    file_name, file_extension = os.path.splitext(file_base_name)

    # Set the maximum size for each part in megabytes
    max_size_megabytes = max_file_size

    # Open the input audio file
    with wave.open(os.path.join(input_path_, input_file_), 'rb') as audio_file:
        sample_width = audio_file.getsampwidth()
        frame_rate = audio_file.getframerate()
        channels = audio_file.getnchannels()

        # Calculate the maximum size for each part in bytes
        max_size_bytes = max_size_megabytes * 1024 * 1024

        # Initialize variables
        part_number = 1
        current_size = 0
        part_frames = []

        # Process the audio file in chunks
        while True:
            frames = audio_file.readframes(1024)  # Adjust the chunk size as needed

            if not frames:
                break

            part_frames.append(frames)
            current_size += len(frames)

            # Check if the current part exceeds the maximum size
            if current_size >= max_size_bytes:
                # Export the current part to a file
                output_file = os.path.join(input_path_, f"{file_name}_part{part_number}.wav")
                with wave.open(output_file, 'wb') as output_audio:
                    output_audio.setnchannels(channels)
                    output_audio.setsampwidth(sample_width)
                    output_audio.setframerate(frame_rate)
                    output_audio.writeframes(b''.join(part_frames))

                print(f"Exported part {part_number}: {output_file}")

                # Reset variables for the next part
                part_number += 1
                current_size = 0
                part_frames = []


if __name__ == '__main__':
    input_path = os.path.join(r'/home/franks/Documents/Podcasts/日谈公园')
    input_file = r'440. 疫情打不垮环球航海心，两年之后他再度启航.wav'
    partition_audio(input_file, input_path, 24.4)
