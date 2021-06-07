import os.path
import sys
import tkinter as tk

from tkinter import ttk
from PIL import Image, ImageTk

sys.path.append(os.path.dirname(os.path.abspath('__file__')))


class Application(tk.Tk):
    style = None

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('{}x{}'.format(1280, 720))
        self.resizable(0, 0)

        self.wm_title("Analysis Parser&Processor (project: DofE 2021)")
        self.wm_iconphoto(False, self.generate_new_bitmap())
        self.prepare_workspace()

    def prepare_workspace(self):
        tab1 = ttk.Frame(self.tab_controller)
        tab2 = ttk.Frame(self.tab_controller)

        self.tab_controller.add(tab1, text='1')
        self.tab_controller.add(tab2, text='2')
        self.tab_controller.pack(expand=1, fill="both")

    @staticmethod
    def exit_program():
        exit()

    class MainContainer(tk.Frame):
        def __init__(self):
            tk.Frame.__init__()

    '''Method used for generating window wm icon, so no external file is needed
       TODO: Create better image in future
    '''
    @staticmethod
    def generate_new_bitmap():
        image = Image.new('RGB', (255, 255), "black")
        pixel = image.load()
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                pixel[i, j] = (i, j, 100)
        return ImageTk.PhotoImage(image)


def run():
    application = Application()
    application.mainloop()
