from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        with open('highscore.txt') as hs:
            self.highscore = int(hs.read())
        self.penup()
        self.goto(0,260)
        self.write(f'Final Score: {self.score} High score: {self.highscore} ', False, align='center', font=('Serif',24,'normal'))
        self.hideturtle()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align='center', font=('Arial',50,'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Final Score: {self.score} High score: {self.highscore} ', False, align='center', font=('Serif',24,'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt', 'w') as hs:
                hs.write(f"{self.highscore}")
                
        self.score = 0