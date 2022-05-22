

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_homepage():
    window = Tk()

    window.geometry("1728x1117")
    window.configure(bg = "#121C29")


    canvas = Canvas(
    window,
    bg = "#121C29",
    height = 1117,
    width = 1728,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
    363.0,
    496.0,
    anchor="nw",
    text="You've successfully logged in",
    fill="#FFFFFF",
    font=("MontserratRoman ExtraBold", 64 * -1)
)
    window.resizable(False, False)
    window.mainloop()