import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="This is a label", font=("Arial", 24))
my_label.pack(expand=True) #places on screen

#Keeps the window open, keep at the end of the program
window.mainloop()