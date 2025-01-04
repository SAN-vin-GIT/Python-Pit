from tkinter import *

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
f_bg = "#91c2af"
FONT_NAME = "Poppins"

random_choice = {}
to_learn = {}

# ........................New Flash
try:
    raw_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/words.csv")
    data_dicts = original_data.to_dict(orient='records')
else:
    data_dicts = raw_data.to_dict(orient='records')

def new_flash():
    global  random_choice,flip_timer
    window.after_cancel(flip_timer)
    random_choice = random.choice(data_dicts)
    title_label.config(text="The Word is",fg="black", font=(FONT_NAME, 40, "italic"), bg="white")
    word_label.config(text=random_choice["Vocab"], fg="black", font=(FONT_NAME, 60, "bold"), bg="white")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

# ........................Flip Card
def flip_card():
    global  random_choice
    title_label.config(text="Meaning of the Word",fg="white", font=(FONT_NAME, 40, "italic"), bg=f_bg)
    word_label.config(text=random_choice["Meaning"],fg="white", font=(FONT_NAME, 60, "bold"), bg=f_bg)
    canvas.itemconfig(card_background, image = card_back)

# ..........................Save Words
def is_known():
    data_dicts.remove(random_choice)
    data = pandas.DataFrame(random_choice)
    data.to_csv("data/words_to_learn.csv", index=False)


    new_flash()




# ...............................UI
window = Tk()
window.title("Vocab Voyager")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="/Users/nightmare/PycharmProjects/vocab_voyager/images/card_front.png")
card_back = PhotoImage(file="/Users/nightmare/PycharmProjects/vocab_voyager/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)


# ................... Labels ...
title_label = Label(window, text="Your Word is", fg="black", font=(FONT_NAME, 40, "italic"), bg="white")
title_label.place(x=400, y=150, anchor="center")
word_label = Label(window, text="Word", fg="black", font=(FONT_NAME, 60, "bold"), bg="white")
word_label.place(x=400, y=263, anchor="center")

#............................ Buttons ...
right_image = PhotoImage(file="/Users/nightmare/PycharmProjects/vocab_voyager/images/right.png",)
wrong_image = PhotoImage(file="/Users/nightmare/PycharmProjects/vocab_voyager/images/wrong.png")
right_button = Button(image=right_image,bd=0,highlightthickness=0, command=new_flash)
right_button.grid(row=1,column=1)

wrong_button = Button(image=wrong_image,bd=0,highlightthickness=0,command=new_flash)
wrong_button.grid(row=1,column=0)



new_flash()
window.mainloop()