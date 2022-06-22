from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-200, y=250)
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=("Menlo", 20, "normal"))

    def add_point(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER.", align="center", font=("Menlo", 20, "normal"))

