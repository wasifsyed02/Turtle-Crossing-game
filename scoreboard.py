from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-350,270)
        self.write("Level 1",align="center",font=("arial",18,"normal"))
    def game_win(self):
        self.goto(0,0)
        self.write("You won this level",align="center",font=("arial",18,"normal"))
    def game_lose(self):
        self.goto(0,0)
        self.write("You hit a car.",align="center",font=("arial",18,"normal"))