#This file look for new floder inside user uploads and converts them to reel if they are m=not already converted

import os 

def text_to_audio(folder):
    print("TTA: ",folder)

def create_reel(folder):
    print("CR: ",folder)

if __name__ == "__main__":
    with open("done.txt","r") as f:
        done_folder = f.readlines()

    done_folder = [f.strip() for f in done_folder]
    folders = os.listdir("user_uploads")
    for folder in folders:
        if folder not in done_folder :
            text_to_audio(folder)
            create_reel(folder)
            with open("done.txt","a") as f:
                f.write(folder +"\n")