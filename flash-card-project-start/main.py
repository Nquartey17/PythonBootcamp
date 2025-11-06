from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcards")
window.minsize(width=900, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR) #padding

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263,image=card_front)
canvas.grid(row=0, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
canvas.create_image(850, 600,image=wrong_img)
canvas.grid(row=1, column=1)






window.mainloop()