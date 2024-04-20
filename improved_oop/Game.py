import tkinter as tk
import ScreenProperties as sp
import MainMenu as mm
import CharacterSelection as cs


class Game(tk.Tk, sp.ScreenProperties):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.GAME_NAME = "Castle of Cards"

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Initialize the screen
        self.initializeScreen()

        self.frames = {}

        for page in (mm.MainMenu, cs.CharacterSelection):
            frame = page(self.container, self)

            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(mm.MainMenu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def initializeScreen(self):
        self.title(self.GAME_NAME)
        self.resizable(False, False)
        # Configure the grid to expand
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        # Position the window in the center of the screen
        posX = (self.winfo_screenwidth() // 2) - (super().getScreenWidth() // 2)
        posY = (self.winfo_screenheight() // 2) - (super().getScreenHeight() // 2)
        self.geometry(
            f"{super().getScreenWidth()}x{super().getScreenHeight()}+{posX}+{posY}"
        )


if __name__ == "__main__":
    game = Game()
    game.mainloop()
