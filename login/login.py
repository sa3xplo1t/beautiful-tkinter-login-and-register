

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import sqlite3
os.chdir("../")


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("428x926")
window.configure(bg = "#151C29")


canvas = Canvas(
    window,
    bg = "#151C29",
    height = 926,
    width = 428,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
def check():
    conn = sqlite3.connect('programwithregister.db')
    c = conn.cursor()
    password = entry_2.get()
    username = entry_1.get()
    check = list(c.execute("""SELECT EXISTS(SELECT 1 FROM users WHERE username = ? AND password = ?)""", (username, password)));
    if check[0][0] == 1:
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
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=check,
    relief="flat"
)
button_1.place(
    x=89.0,
    y=506.0,
    width=249.0,
    height=100.0
)

canvas.create_text(
    160.0,
    145.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("MontserratRoman ExtraBold", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    214.0,
    264.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
)
entry_1.insert(0, "Username")
entry_1.place(
    x=78.0,
    y=212.0,
    width=272.0,
    height=102.0
)


entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    214.0,
    411.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.insert(0, "Password")
entry_2.place(
    x=78.0,
    y=359.0,
    width=272.0,
    height=102.0
)

canvas.create_text(
    41.0,
    629.0,
    anchor="nw",
    text="By clicking Login you accept Program with Register terms of service",
    fill="#B9B9B9",
    font=("MontserratRoman ExtraBold", 12 * -1)
)

canvas.create_text(
    118.0,
    886.0,
    anchor="nw",
    text="Copyright 2022 Program with Register",
    fill="#B9B9B9",
    font=("MontserratRoman ExtraBold", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
