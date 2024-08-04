from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        self.paddle_position = position
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.paddle_position)

    def go_up(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x, current_y + MOVE_DISTANCE)

    def go_down(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x, current_y - MOVE_DISTANCE)
