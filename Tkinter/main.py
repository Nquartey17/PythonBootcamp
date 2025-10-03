from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) #padding

#Label
my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0,row=0)

#Buttons
def button_clicked():
    # Challenge - get entry text print when button is clicked
    my_label["text"] = entry_input.get()
    print("I got clicked")

button = Button(text="Click Me", command=button_clicked) #Command gets name of function, doesn't need ()
button.grid(column=1,row=1)

button2 = Button(text="New button")
button2.grid(column=2,row=0)

#Entry
entry_input = Entry(width=10)
print(entry_input.get())
entry_input.grid(column=3,row=2)

#Note - pack and grid are incompatible
#Keeps the window open, keep at the end of the program
window.mainloop()