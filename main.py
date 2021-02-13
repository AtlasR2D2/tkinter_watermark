# Watermark Project

import tkinter as tk
from turtle import Turtle, Screen
from PIL import ImageTk, Image, ImageDraw, ImageFont


def add_suffix_to_filename(url_x, suffix):
    """takes a url and adds a suffix to the filename"""
    dot_char = len(url_x)-url_x[::-1].find(".")-1
    name = url_x[:dot_char]
    file_type = url_x[dot_char:]
    new_name = name + suffix
    new_url = new_name + file_type
    return new_url


class PhotoUploader:
    def __init__(self, img_url):
        self.img_url = img_url
        self.watermark_text = "Watermark Test"
        self.app = tk.Tk()
        self.photo = Image.open(self.img_url)

    def add_watermark(self):
        # Allow edit on image
        self.photo = Image.open(self.img_url)
        self.drawing = ImageDraw.Draw(self.photo)
        self.black = (3, 8, 12)
        self.font = ImageFont.truetype("Roboto-Black.ttf", 70)
        self.drawing.text((100, 100), self.watermark_text,fill=self.black, font=self.font)
        self.photo.save(add_suffix_to_filename(self.img_url, "_wtm"))

    def show_img(self):
        self.photo.show()


# Declare class object
# Make sure to reference to image you wish to show
photo_uploader = PhotoUploader(img_url="horse.jpg")
# Ask user if they want to add watermark to image
valid_answer = False
while not valid_answer:
    answer = input("Do you want to add a watermark? (Y/N): ").upper()
    valid_answer = (answer in ["Y", "N"])

add_watermark = (answer == "Y")
if add_watermark:
    photo_uploader.add_watermark()
# Show photo
photo_uploader.show_img()
