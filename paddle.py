from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -220:
            self.goto(self.xcor(), self.ycor() - 20)