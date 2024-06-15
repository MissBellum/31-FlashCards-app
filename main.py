from tkinter import *
import pandas
from random import *

rand_word = {}
french_dict = {}

try:
    french_words = pandas.read_csv("data/learn.csv")
except FileNotFoundError:
    french_words = pandas.read_csv("data/french_words.csv")
    french_dict = french_words.to_dict(orient="records")
else:
    french_dict = french_words.to_dict(orient="records")


def pick_word():
    global rand_word, flip_timer
    window.after_cancel(flip_timer)
    rand_word = choice(french_dict)
    canvas.itemconfig(f_title_text, text="French", fill="black")
    canvas.itemconfig(f_card_text, text=rand_word["French"], fill="black")
    canvas.itemconfig(f_image, image=card_front)
    flip_timer = window.after(3000, func=change_card)


def change_card():
    canvas.itemconfig(f_title_text, text="English", fill="white")
    canvas.itemconfig(f_card_text, text=rand_word["English"], fill="white")
    canvas.itemconfig(f_image, image=card_back)


def remove_card():
    french_dict.remove(rand_word)
    data = pandas.DataFrame(french_dict)
    data.to_csv("data/learn.csv", index=False)

    pick_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="light green")
flip_timer = window.after(3000, func=change_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
f_image = canvas.create_image(400, 263, image=card_front)
f_title_text = canvas.create_text(400, 150, text="", font=("Calibri", 30, "italic"))
f_card_text = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))
canvas.config(bg="light green", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=pick_word)
wrong.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=remove_card)
right.grid(row=1, column=1)

pick_word()


window.mainloop()
