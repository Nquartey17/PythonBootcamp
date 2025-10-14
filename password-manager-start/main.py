from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

#Entries
web_box = Entry(width=35)
web_box.grid(row=1, column=1, columnspan=2, sticky="EW")
email_box = Entry(width=35)
email_box.grid(row=2, column=1, columnspan=2, sticky="EW")
email_box = Entry(width=21)
email_box.grid(row=3, column=1, sticky="EW")

#Buttons
generate_password = Button(text="Generate Password")
generate_password.grid(row=3, column=2, columnspan=1)
add_button = Button(width=36, text="Add")
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")





window.mainloop()