from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    #Join password tuple by ""
    rand_password = "".join(password_list)
    password_box.delete(0, END) #clear password input if something already exists
    password_box.insert(0, rand_password)
    pyperclip.copy(rand_password) #password saved to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_box.get()
    email = email_box.get()
    user_password = password_box.get()
    new_data = {
        website: {
            "email": email,
            "password": user_password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(user_password) == 0:
        messagebox.showwarning(title="Warning", message="Make sure all fields have values")

    else:
        # is_ok = messagebox.askokcancel(title=web_box.get(), message=f"Details entered:\nEmail: {email_box.get()}\nPassword: {password_box.get()}\n"
        #                                f"Do you want to save these inputs?")

        # if is_ok:
        with open("password.json", "r") as file:
            # json.dump(new_data, file, indent=4) write to new json file
            #Read old data
            data = json.load(file)
            #Update old data [new_data in this case] with new data
            data.update(new_data)

        with open("password.json", "w") as file:
            #Saving updated data
            json.dump(data, file, indent=4)
        web_box.delete(0, END)
        password_box.delete(0, END)
        print("Saved")


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
web_box.focus() #cursor will automatically start here
email_box = Entry(width=35)
email_box.grid(row=2, column=1, columnspan=2, sticky="EW")
email_box.insert(0,"niikwarteiq@gmail.com") #Start with commonly used email
password_box = Entry(width=21)
password_box.grid(row=3, column=1, sticky="EW")

#Buttons
generate_password = Button(text="Generate Password",command=random_password)
generate_password.grid(row=3, column=2, columnspan=1)
add_button = Button(width=36, text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")





window.mainloop()