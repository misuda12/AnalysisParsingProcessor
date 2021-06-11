import tkinter as tk

text = """
This software is free to use and delivered to you with a lot of fun
(Discord: MartineC#0001, Mail: 211869@vutbr.cz, Phone: +421 949194280)
"""


class AboutWindow:
    def __init__(self, master):
        super().__init__()
        window = tk.Toplevel(master)
        import src.main.engine as engine
        window.wm_title("Analysis Parser&Processor (project: DofE 2021) - About")
        window.wm_iconphoto(False, engine.generate_new_icon())
        window.resizable(0, 0)
        tk.Label(window, text=text).pack()