from tkinter import messagebox
from PIL import Image, ImageTk

"""
Method used for generating window wm icon, so no external file is needed
   TODO: Create better image in future
"""


def generate_new_icon():
    image = Image.new('RGB', (255, 255), "black")
    pixel = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel[i, j] = (i, j, 100)
    return ImageTk.PhotoImage(image)


def generate_exception_box(exception_message, title=u'An error has occurred ... '):
    messagebox.showerror(
        title,
        exception_message
    )