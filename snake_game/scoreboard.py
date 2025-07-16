from turtle import Turtle
style =  ("Courier",13, "normal")
Align = 'center'

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("/Users/Hp/python/snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(x=-1, y=280)
        self.color("white")
        self.score = 0
        self.write(f'Score: {self.score}', move=False, align = Align, font= style)
        self.hideturtle()
        self.update_scoreboard()
        
    def increase(self):
        self.score += 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} HighScore: {self.high_score}', move=False, align = 'center', font= style)
       
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/Hp/python/snake_game/data.txt", mode ="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()