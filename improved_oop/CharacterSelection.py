from PIL import Image, ImageTk
import tkinter as tk
import ScreenProperties as sp


class CharacterSelection(tk.Frame, sp.ScreenProperties):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.grid(sticky="nsew")

        self.showStartBg()
        self.showSelectBanner()

    def showSelectBanner(self):
        # Placard
        _PLACARD_BG_COLOR = "#007DA1"
        _PLACARD_WIDTH = self.winfo_screenwidth()
        _PLACARD_HEIGHT = self.winfo_screenheight() // 5
        placard = tk.Frame(
            self, width=_PLACARD_WIDTH, height=_PLACARD_HEIGHT, bg=_PLACARD_BG_COLOR
        )
        placard.place(relx=0.5, rely=0, anchor="c")

        # Placard Text
        _PLACARD_TEXT = "SELECT YOUR CHARACTER"
        _PLACARD_TEXT_COLOR = "White"
        _PLACARD_TEXT_SIZE = 30
        _PLACARD_TEXT_FONT = "Gotham Black"
        placardText = tk.Label(
            placard,
            text=_PLACARD_TEXT,
            font=(_PLACARD_TEXT_FONT, _PLACARD_TEXT_SIZE),
            fg=_PLACARD_TEXT_COLOR,
            bg=_PLACARD_BG_COLOR,
        )
        placardText.place(relx=0.5, rely=0.75, anchor="c")

    def showStartBg(self):
        tempStartBg = Image.open("assets/backgrounds/start_bg.png")
        resizedStartBg = tempStartBg.resize(
            (super().getScreenWidth(), super().getScreenHeight())
        )
        self.startBg = ImageTk.PhotoImage(resizedStartBg)
        label = tk.Label(self, image=self.startBg)
        label.place(x=0, y=0, relwidth=1, relheight=1)
