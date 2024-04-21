from PIL import Image, ImageTk
import tkinter as tk
import ScreenProperties as sp


class CharacterSelection(tk.Frame, sp.ScreenProperties):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.grid(sticky="nsew")

        self._initializeScreenCanvas()

        # Show the start background
        self._showStartBg()
        self._showSelectBanner()
        self._showCharacterSelection()

    def _initializeScreenCanvas(self):
        self._screenCanvas = tk.Canvas(
            self,
            width=super().getScreenWidth(),
            height=super().getScreenHeight(),
            highlightthickness=0,
        )

        self._screenCanvas.pack()

    def _showSelectBanner(self):
        # Placard
        PLACARD_BG_COLOR = "#007DA1"
        PLACARD_WIDTH = self.winfo_screenwidth()
        PLACARD_HEIGHT = self.winfo_screenheight() // 7
        self._placard = tk.Frame(
            self,
            width=PLACARD_WIDTH,
            height=PLACARD_HEIGHT,
            bg=PLACARD_BG_COLOR,
        )
        self._placard.place(relx=0.5, rely=0, anchor="c")

        # Placard Text
        _PLACARD_TEXT = "SELECT YOUR CHARACTER"
        _PLACARD_TEXT_COLOR = "White"
        _PLACARD_TEXT_SIZE = 30
        _PLACARD_TEXT_FONT = "Gotham Black"
        self._placardText = tk.Label(
            self._placard,
            text=_PLACARD_TEXT,
            font=(_PLACARD_TEXT_FONT, _PLACARD_TEXT_SIZE),
            fg=_PLACARD_TEXT_COLOR,
            bg=PLACARD_BG_COLOR,
        )
        self._placardText.place(relx=0.5, rely=0.75, anchor="c")

    def _showStartBg(self):
        tempStartBg = Image.open("assets/backgrounds/start_bg.png")
        resizedStartBg = tempStartBg.resize(
            (super().getScreenWidth(), super().getScreenHeight())
        )
        self.screenBg = ImageTk.PhotoImage(resizedStartBg)
        self.charBg = self._screenCanvas.create_image(
            0, 0, image=self.screenBg, anchor="nw"
        )

    def _resizeImage(self, img, width, height):
        # Character Icons
        tmpImg = Image.open(img)
        resizedImg = tmpImg.resize((width, height))
        return ImageTk.PhotoImage(resizedImg)

    def _showCharacterSelection(self):
        # Character Icons Frame
        self._charFrame = tk.Frame(self._screenCanvas, bg="#007DA1")
        self._charFrame.place(relx=0.5, rely=0.8, anchor="c")

        # Character Icons
        ICON_WIDTH = 60
        ICON_HEIGHT = 60
        self.berserkerIcon = self._resizeImage(
            "assets/icons/berserker_icon.png",
            ICON_WIDTH,
            ICON_HEIGHT,
        )
        self.rangerIcon = self._resizeImage(
            "assets/icons/ranger_icon.png",
            ICON_WIDTH,
            ICON_HEIGHT,
        )
        self.mageIcon = self._resizeImage(
            "assets/icons/mage_icon.png",
            ICON_WIDTH,
            ICON_HEIGHT,
        )
        self.assassinIcon = self._resizeImage(
            "assets/icons/assassin_icon.png",
            ICON_WIDTH,
            ICON_HEIGHT,
        )
        self.tankIcon = self._resizeImage(
            "assets/icons/tank_icon.png",
            ICON_WIDTH,
            ICON_HEIGHT,
        )

        # Character Backgrounds
        self.berserkerBg = self._resizeImage(
            "assets/backgrounds/berserker_bg.png",
            super().getScreenWidth(),
            super().getScreenHeight(),
        )
        self.rangerBg = self._resizeImage(
            "assets/backgrounds/ranger_bg.png",
            super().getScreenWidth(),
            super().getScreenHeight(),
        )
        self.mageBg = self._resizeImage(
            "assets/backgrounds/mage_bg.png",
            super().getScreenWidth(),
            super().getScreenHeight(),
        )
        self.assassinBg = self._resizeImage(
            "assets/backgrounds/assassin_bg.png",
            super().getScreenWidth(),
            super().getScreenHeight(),
        )
        self.tankBg = self._resizeImage(
            "assets/backgrounds/tank_bg.png",
            super().getScreenWidth(),
            super().getScreenHeight(),
        )

        # Character Presentation Images
        CHAR_IMG_WIDTH = 1000
        CHAR_IMG_HEIGHT = 1000
        self.berserkerMain = self._resizeImage(
            "assets/main/berserker_main.png",
            CHAR_IMG_WIDTH,
            CHAR_IMG_HEIGHT,
        )
        self.rangerMain = self._resizeImage(
            "assets/main/ranger_main.png",
            CHAR_IMG_WIDTH,
            CHAR_IMG_HEIGHT,
        )
        self.mageMain = self._resizeImage(
            "assets/main/mage_main.png",
            CHAR_IMG_WIDTH,
            CHAR_IMG_HEIGHT,
        )
        self.assassinMain = self._resizeImage(
            "assets/main/assassin_main.png",
            CHAR_IMG_WIDTH,
            CHAR_IMG_HEIGHT,
        )
        self.tankMain = self._resizeImage(
            "assets/main/tank_main.png",
            CHAR_IMG_WIDTH,
            CHAR_IMG_HEIGHT,
        )
        # Character Presentation Placement
        CHAR_IMG_WIDTH = 750
        CHAR_IMG_HEIGHT = 750
        self._characterMain = self._screenCanvas.create_image(
            super().getScreenWidth() / 2, super().getScreenHeight() / 2, anchor="c"
        )
        # Move x and y coordinates to desired
        self._screenCanvas.move(self._characterMain, -200, 150)

        BERSERKER_THEME_COLOR_COLOR = "#1b6c87"
        RANGER_THEME_COLOR_COLOR = "#9e3b1d"
        MAGE_THEME_COLOR_COLOR = "#642f10"
        ASSASSIN_THEME_COLOR_COLOR = "#5876aa"
        TANK_THEME_COLOR_COLOR = "#4e504f"

        changeCharacterCommands = {
            0: lambda: self._changeCharacter(
                BERSERKER_THEME_COLOR_COLOR, self.berserkerBg, self.berserkerMain
            ),
            1: lambda: self._changeCharacter(
                RANGER_THEME_COLOR_COLOR, self.rangerBg, self.rangerMain
            ),
            2: lambda: self._changeCharacter(
                MAGE_THEME_COLOR_COLOR, self.mageBg, self.mageMain
            ),
            3: lambda: self._changeCharacter(
                ASSASSIN_THEME_COLOR_COLOR, self.assassinBg, self.assassinMain
            ),
            4: lambda: self._changeCharacter(
                TANK_THEME_COLOR_COLOR, self.tankBg, self.tankMain
            ),
        }

        self._buttonOptions = [
            {
                # "width": ICON_WIDTH,
                # "height": ICON_HEIGHT,
                # "image": character,
                # "bg": "#007DA1",  # Default color
                # "anchor": "c",
                # "command": changeCharacterCommands[i],
                "button": tk.Button(
                    self._charFrame,
                    width=ICON_WIDTH,
                    height=ICON_HEIGHT,
                    image=character,
                    bg="#007DA1",
                    anchor="c",
                    command=changeCharacterCommands[i],
                ),
                "image": character,
            }
            for i, character in enumerate(
                [
                    self.berserkerIcon,
                    self.rangerIcon,
                    self.mageIcon,
                    self.assassinIcon,
                    self.tankIcon,
                ]
            )
        ]

        for i, options in enumerate(self._buttonOptions):
            # button = tk.Button(self._charFrame, **options)
            button = options["button"]
            button.grid(row=0, column=i, padx=10, pady=5)

    def _changeCharacter(self, charThemeColor, bg, charMain):
        self._placard.config(bg=charThemeColor)
        self._placardText.config(bg=charThemeColor)
        self._charFrame.config(bg=charThemeColor)
        self._screenCanvas.itemconfig(self.charBg, image=bg)
        self._screenCanvas.itemconfig(self._characterMain, image=charMain)

        for button in self._buttonOptions:
            button["button"].config(bg=charThemeColor)
