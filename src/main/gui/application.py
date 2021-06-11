import os.path
import sys
import tkinter as tk

from tkinter import ttk

sys.path.append(os.path.dirname(os.path.abspath('__file__')))

master = None


class Application(tk.Tk):
    style = None

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.update_idletasks()
        self.wm_title("Analysis Parser&Processor (project: DofE 2021)")
        # Center application to the middle of screen
        self.geometry('{}x{}+{}+{}'.format(
            360, 240,
            int((self.winfo_screenwidth () / 2) - (360 / 2)),
            int((self.winfo_screenheight() / 2) - (240 / 2))
        ))
        self.resizable(False, False)
        import src.main.engine as engine
        self.wm_iconphoto(False, engine.generate_new_icon())
        self.prepare_workspace()

        """Code that will auto-destroy Tk from memory and will close application"""
        self.bind('<Escape>', lambda event: self.exit())

    def prepare_workspace(self):
        label_frame = tk.LabelFrame(self, text="General")
        label_frame.config(font=('Helvetical bold', 20))
        label_frame.pack(fill="both", expand="yes")
        """LabelFrame packed"""

        tk.Label      (label_frame, text="Test", justify=tk.LEFT)\
            .grid(column=0, row=0, sticky=tk.W)
        ttk.OptionMenu(label_frame, tk.StringVar(), "Scanners", {})\
            .grid(column=1, row=0)

    def exit(self):
        self.destroy()
        pass


def run():
    global master
    if master:
        master.mainloop()
    else:
        master = Application()
        master.mainloop()
