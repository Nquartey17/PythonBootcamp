
from tkinter import *
import pandas, random


BACKGROUND_COLOR = "#B1DDC6"
df = pandas.read_csv("data/japanese_words.csv")
words = df.to_dict(orient='records')

#Functions
def random_card():
    current_card = random.choice(words)
    canvas.itemconfig(language_title, text="Japanese")
    canvas.itemconfig(language_word, text=current_card["Japanese"])



window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR) #padding

#Canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Labels
language_title = canvas.create_text(400,150,text="", font=("Arial", 40, "italic"))
language_word = canvas.create_text(400,263,text="", font=("Arial", 60, "bold"))

#Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=random_card)
wrong_button.grid(row=1,column=0)

check_img = PhotoImage(file="images/right.png")
right_button = Button(image=check_img, highlightthickness=0, command=random_card)
right_button.grid(row=1,column=1)

random_card() # Start program with random card


window.mainloop()