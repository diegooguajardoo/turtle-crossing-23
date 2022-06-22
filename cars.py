from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
colors = ["blue", "red", "orange", "grey"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.setx(300)
        self.sety(random.randint(-250, 250))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.fillcolor(random.choice(colors))

    def move(self, level):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * level
        self.goto(new_x, self.ycor())

    def check_run_over(self, player):
        if self.distance(player) <= 20:
            self.fillcolor("black")
            print(self.distance(player))
            return True
