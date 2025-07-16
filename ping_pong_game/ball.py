from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.s = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.s *= 0.8
        
    def reset(self):
        self.goto(0,0)
        self.s = 0.1
        self.bounce_x()
        
    