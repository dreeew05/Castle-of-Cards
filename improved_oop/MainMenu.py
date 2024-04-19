from PIL import Image, ImageTk
import CharacterSelection as cs
import tkinter as tk


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#658ecf")
        self.controller = controller

        # Make the frame fill the entire window
        self.grid(sticky="nsew")

        self.showLogo()
        self.showButtons()

    def showLogo(self):
        # Logo
        tempLogo = Image.open("assets/logo.png")
        resizedLogo = tempLogo.resize((400, 400))
        self.finalImage = ImageTk.PhotoImage(resizedLogo)
        label = tk.Label(self, image=self.finalImage, bg="#658ecf")
        # Center the logo
        label.place(relx=0.5, rely=0.3, anchor="c")

    def showButtons(self):
        # Buttons
        frameButtons = tk.Frame(self, bg="#658ecf")
        # Center the buttons
        frameButtons.place(relx=0.5, rely=0.7, anchor="c")

        buttonOptions = [
            {
                "text": "START",
                "font": ("Gotham Black", 15),
                "bg": "Grey",
                "width": 20,
                "padx": 10,
                "pady": 10,
                "bd": 0,
                "command": lambda: self.controller.show_frame(cs.CharacterSelection),
            },
            {
                "text": "HOW TO PLAY",
                "font": ("Gotham Black", 15),
                "bg": "Grey",
                "width": 20,
                "padx": 10,
                "pady": 10,
                "bd": 0,
                # "command": lambda: instructions(window, esc_icon),
            },
            {
                "text": "QUIT",
                "font": ("Gotham Black", 15),
                "bg": "Red",
                "width": 20,
                "padx": 10,
                "pady": 10,
                "bd": 0,
                "command": quit,
            },
        ]

        for i, options in enumerate(buttonOptions):
            tk.Button(frameButtons, **options).grid(row=i, column=0, pady=5)
