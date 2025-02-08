import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
words = []
flash_card_word = {}

def flip_card():
    global flash_card_word, task_id
    canvas.itemconfig(language, text="English", fill="#ffffff")
    canvas.itemconfig(meaning, text=f'{flash_card_word["English"]}', fill="#ffffff")
    canvas.itemconfig(card_image, image=back_card)

def maru():
    words.remove(flash_card_word)
    to_learn_df = pandas.DataFrame(words)
    to_learn_df.to_csv("data/to_learn.csv", index=False)
    next_word()

def next_word():
    global flash_card_word, task_id
    window.after_cancel(task_id)
    flash_card_word = random.choice(words)
    canvas.itemconfig(language, text="French", fill="#000000")
    canvas.itemconfig(card_image, image=front_card)
    canvas.itemconfig(meaning, text=f'{flash_card_word["French"]}', fill="#000000")
    task_id = window.after(3000, func=flip_card)

def load_data():
    global words
    file_path = "./data/to_learn.csv"
    try:
        df = pandas.read_csv(file_path)
    except FileNotFoundError:
        df = pandas.read_csv("./data/french_words.csv")
    finally:
        words = df.to_dict(orient="records")


window = Tk()
window.title("Flash Card")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
load_data()

maru_image = PhotoImage(file="./images/right.png")
basu_image = PhotoImage(file="./images/wrong.png")
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
canvas.grid(row=0, column=0, columnspan=2)
card_image = canvas.create_image(400, 265, image=front_card)
language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
meaning = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))

basu_button = Button(image=basu_image, highlightthickness=0, borderwidth=0, command=next_word)
basu_button.grid(row=1, column=0)
maru_button = Button(image=maru_image, highlightthickness=0, borderwidth=0, command=maru)
maru_button.grid(row=1, column=1)
task_id = window.after(0, next_word)

window.mainloop()
