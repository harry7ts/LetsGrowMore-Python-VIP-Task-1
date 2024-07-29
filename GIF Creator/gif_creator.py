## LetsGrowMore Python Developer Virtual Internship Program 

## TASK-I

## Creating a GIF using multiple images


import os
from moviepy.editor import *

class GIFCreator:
    def __init__(self):
        self.image_folder = input("Enter the folder containing the images: ")
        self.gif_name = input("Enter the name of the output GIF file: ")
        self.duration = self.get_duration()

    def get_duration(self):
        while True:
            try:
                return float(input("Enter the duration of each image in seconds: "))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def create_gif(self):

        valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        image_files = []
        for f in os.listdir(self.image_folder):
            if f.lower().endswith(valid_extensions):
                image_files.append(os.path.join(self.image_folder, f))
        
        image_files.sort()

        image_clips = [ImageClip(f).set_duration(self.duration) for f in image_files]
        clip = concatenate_videoclips(image_clips)
        clip.write_gif(self.gif_name, fps=1)
        print("GIF created successfully!")

    def run(self):
        self.create_gif()

if __name__ == "__main__":
    GIFCreator().run()