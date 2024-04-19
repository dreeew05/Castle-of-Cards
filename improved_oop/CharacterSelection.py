import tkinter as tk
from tkinter import ttk


class CharacterSelection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.grid(sticky="nsew")
