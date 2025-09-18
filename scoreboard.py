from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  
        self.penup()
        self.hideturtle()
        self.goto(0, +285)
        self.color("white")
        self.pendown()
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 20, "bold"))

    def update_score(self):
        self.write(f" Score: {self.score}", align="center", font=("Arial", 12, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


