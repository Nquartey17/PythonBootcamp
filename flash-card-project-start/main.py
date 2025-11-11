from os import remove
from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    #look for saved file
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    #Read from populated list if save file isn't found
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")

words = df.to_dict(orient='records')
# print(words[0])
current_card = {} #initialize global variable

#Functions
def random_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # Reset timer once new card is displayed
    current_card = random.choice(words)
    canvas.itemconfig(language_title, text="French",fill="black")
    canvas.itemconfig(language_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_title, text="English", fill="white")
    canvas.itemconfig(language_word, text=current_card["English"], fill="white")

def word_known():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False) #index false stops index numbers from being added repeatedly after save
    random_card()

#window
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR) #padding

flip_timer = window.after(3000, func=flip_card)

#Canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front)
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
right_button = Button(image=check_img, highlightthickness=0, command=word_known)
right_button.grid(row=1,column=1)

random_card() # Start program with random card


window.mainloop()