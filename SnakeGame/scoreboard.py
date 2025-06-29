from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.setposition(0, 280)
        self.penup()
        self.color("white")
        #Don't use arguments with variable if you want to format text
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.score += 1
        self.undo()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
