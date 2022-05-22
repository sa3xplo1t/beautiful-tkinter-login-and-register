


from atexit import register
from pathlib import Path
import sqlite3
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
os.chdir("../")
mail = ""
password = ""
username = ""

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def register():
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
    def register_get():
        mail = entry_3.get()
        password = entry_2.get()
        username = entry_1.get()
        conn = sqlite3.connect('programwithregister.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, mail))
        conn.commit()
        conn.close()
    button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=register_get,
    relief="flat"
    )
    button_1.place(
    x=89.0,
    y=632.0,
    width=249.0,
    height=100.0
    )

    canvas.create_text(
    133.0,
    148.0,
    anchor="nw",
    text="Register",
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
    highlightthickness=0
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
    761.0,
    anchor="nw",
    text='By clicking "Register" you accept terms of service.',
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

    entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
    214.0,
    551.0,
    image=entry_image_3
    )
    entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
    )
    entry_3.insert(0, "Email")
    entry_3.place(
    x=78.0,
    y=499.0,
    width=272.0,
    height=102.0
    )

    window.resizable(False, False)
    window.mainloop()
register()