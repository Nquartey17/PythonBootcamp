from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    #(1,3,5,7) -> work, (2,4,6) -> short break, 8 -> long break

    if reps == 8:
        count_down(long_break)
        timer_label.config(text="Long Break", fg=GREEN)
    elif reps % 2 != 0:
        count_down(work_seconds)
        timer_label.config(text="Work", fg=RED)
    else:
        count_down(short_break)
        timer_label.config(text="Short Break", fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    #Changing text in tkinter, input canvas variable and element you want to change
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")

    if count > 0:
        # after set time in ms, function, **args input(s) to add to function
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") #Use PhotoImage for pictures in tkinter
canvas.create_image(100, 112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0,column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset")
reset_button.grid(row=2,column=2)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)



window.mainloop()