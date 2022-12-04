from turtle import Turtle
from turtle import Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        x = 0
        for position in range(0, 3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            x -= 20
            snake.goto(x, 0)
            self.snakes.append(snake)

    def add_snakes(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(-400, -400)
        self.snakes.append(snake)


    def reset_snake(self):
        for segments in self.snakes:
            segments.goto(1000,1000)

        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def move(self):

        for snakes_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snakes_num - 1].xcor()
            new_y = self.snakes[snakes_num - 1].ycor()
            self.snakes[snakes_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snakes[0].seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snakes[0].seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snakes[0].seth(RIGHT)
