from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=125, height=125)
window.config(padx=20, pady=20) #padding

number = Entry(width=10)
number.grid(row=0,column=1)

miles = Label(text="Miles", font=("Arial", 12))
miles.grid(row=0,column=2)

text = Label(text="is equal to", font=("Arial", 12))
text.grid(row=1,column=0)

value = Label(text=0, font=("Arial", 12))
value.grid(row=1,column=1)

km = Label(text="Km", font=("Arial", 12))
km.grid(row=1,column=2)

def calculate():
    answer = float(number.get()) * 1.609
    value["text"] = round(answer,2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2,column=1)

window.mainloop()