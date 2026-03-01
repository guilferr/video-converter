import os
import sys
from pathlib import Path
from moviepy import *
from dotenv import load_dotenv

def convert_ts_to_mp4(ts_file, output_file):
    try:
        video = VideoFileClip(ts_file)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def get_ts_files(ts_video_path):
    path_obj = Path(ts_video_path)
    ts_files = list(path_obj.rglob("*.ts"))
    return ts_files

def main():
    load_dotenv()

    output_dir = os.getenv("OUTPUT_FILE")
    ts_video_path = os.getenv("TS_VIDEO_PATH")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(ts_video_path):
        print(f"Failed to find TS video directory: {ts_video_path}")
        sys.exit(1)

    ts_files = get_ts_files(ts_video_path)
    
    for ts_file in ts_files:
        file_name = os.path.splitext(os.path.basename(ts_file))[0]
        output_file = os.path.join(output_dir, f"{file_name}.mp4")

        if os.path.exists(output_file):
            continue

        print(f"Converting {ts_file} to {output_file}")
        convert_ts_to_mp4(ts_file, output_file)

    print("Conversion complete.")


if __name__ == "__main__":
    main()