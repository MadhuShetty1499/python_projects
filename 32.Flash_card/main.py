import random
from tkinter import *
import pandas
# --------------------- CONSTANTS ------------------------ #
BACKGROUND_COLOR = "#B1DDC6"

# --------------------- READ DATA ------------------------ #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
french_word = None
english_word = None
rand_index = None


# --------------------- FUNCTIONS ------------------------ #
def next_card():
    global french_word, english_word, flip_timer, rand_index
    window.after_cancel(flip_timer)
    rand_index = random.choice(to_learn)
    french_word = rand_index["French"]
    english_word = rand_index["English"]
    flash_card.itemconfig(front_card, image=front_img)
    flash_card.itemconfig(front_title, text="French", fill="black")
    flash_card.itemconfig(front_word, text=french_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global english_word
    flash_card.config(bg=BACKGROUND_COLOR)
    flash_card.itemconfig(front_title, text="English", fill="white")
    flash_card.itemconfig(front_card, image=back_img)
    flash_card.itemconfig(front_word, text=english_word, fill="white")


def learnt_word():
    global rand_index
    to_learn.remove(rand_index)
    print(len(to_learn))
    to_learn_df = pandas.DataFrame(to_learn)
    to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------------- UI --------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
front_card = flash_card.create_image(400, 263, image=front_img)
front_title = flash_card.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
front_word = flash_card.create_text(400, 263, font=("Arial", 60, "bold"))
flash_card.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=learnt_word)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

# --------------------- FLIP CARD ------------------------ #





window.mainloop()
