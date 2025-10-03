from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="This is a label", font=("Arial", 24))
my_label.pack() #places on screen

#Config/change properties of created component
my_label["text"] = "New Text"
my_label.config(text="New Text")

#Buttons

def button_clicked():
    # Challenge - get entry text print when button is clicked
    my_label["text"] = entry_input.get()
    print("I got clicked")

button = Button(text="Click Me", command=button_clicked) #Command gets name of function, doesn't need ()
button.pack()

#Entry

entry_input = Entry(width=10)
entry_input.pack()
print(entry_input.get())


#Keeps the window open, keep at the end of the program
window.mainloop()