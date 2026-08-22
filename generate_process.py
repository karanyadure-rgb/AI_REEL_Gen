#This file looks for new folders inside user uploads and converts them to reels if they are not already converted

import os 
from text_to_audio import text_to_speech_file
import time

def text_to_audio(folder):
    print("TTA: ", folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    print(text, folder)
    text_to_speech_file(text, folder)

def create_reel(folder):
    print("CR: ", folder)


if __name__ == "__main__":
    while True:
        print("Processing the queue .....")
        with open("done.txt", "r") as f:
            done_folder = f.readlines()

        done_folder = [f.strip() for f in done_folder]
        folders = os.listdir("user_uploads")
        for folder in folders:
            if folder not in done_folder:
                try:
                    text_to_audio(folder)
                    create_reel(folder)
                    with open("done.txt", "a") as f:
                        f.write(folder + "\n")
                except Exception as e:
                    print(f"FAILED on {folder}: {e}")

        time.sleep(4)

