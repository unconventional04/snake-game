import turtle as t

from scoreboard import Scoreboard
from snake_class import Snake
from food import Food
import time
screen=t.Screen()
screen.tracer(0)
screen.title("Snake Game")
screen.setup(600,600)
screen.bgcolor("black")
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score = Scoreboard()
is_move=True
while is_move:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -290:
        is_move=False
        score.game_over()
    elif snake.head.ycor() > 290 or snake.head.ycor() < -285:
        is_move=False
        score.game_over()

    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
                is_move=False
                score.game_over()
