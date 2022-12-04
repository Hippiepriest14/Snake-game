from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


def continue_game():
    global game_is_on
    action = screen.textinput("Game over.Continue?", " Type Y or N: ")
    if action == "Y".lower():
        screen.listen()
        game_is_on = True

    else:
        game_is_on = False

def snake_game():

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()


        if snake.head.distance(food) < 15:
            food.refresh()
            snake.add_snakes()
            scoreboard.increase_score()

        #Collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290:
            scoreboard.reset_scoreboard()
            snake.reset_snake()
            continue_game()

        for segment in snake.snakes[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset_scoreboard()
                snake.reset_snake()
                continue_game()

snake_game()




# screen.exitonclick()
