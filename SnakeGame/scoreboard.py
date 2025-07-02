from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="highscore.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.setposition(0, 280)
        self.penup()
        self.color("white")
        #Don't use arguments with variable if you want to format text
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            #write new score to file
            with open(file="highscore.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
