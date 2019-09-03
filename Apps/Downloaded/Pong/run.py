import time
from tkinter import *
from threading import Thread
from time import sleep

class runApp:
    def __init__(self, instance, appName):
        if __name__ == '__main__':
            pass
        Game = Pong(instance, appName)

class Pong:
    def __init__(self, instance, appName):
        self.MainInterface = instance
        self.Window1 = self.MainInterface.AppScreen
        self.InterfaceWindow = self.MainInterface.InterfaceWindow
        self.FontArray = self.MainInterface.Fonts

        self.width1 = self.MainInterface.windowWidth
        self.height1 = self.MainInterface.windowHeight

        self.width = self.width1
        self.height = (350 / 400) * self.height1
        self.Window1.config(bg='#040404')

        self.Window = Canvas(self.Window1, bg="#141414")
        self.Window.place(relx=0, rely=0, width=self.width, height=self.height)

        self.Game_Active = True
        self.Game_Information = Label(self.Window, bg='#141414', font=('MS PGothic', 18, 'bold'), fg='#16a085')
        self.Paddle_1 = Paddle(self, [0.05, 0.35])
        self.Paddle_2 = Paddle(self, [0.95, 0.35])
        self.Ball_Position = [0.45, 0.45]
        self.Ball_Direction = [0.0025, 0.0075]
        self.Ball = Label(self.Window, height=1, width=2)
        self.Ball.place(relx=self.Ball_Position[0], rely=self.Ball_Position[1])

        self.InterfaceWindow.bind('<Up>', lambda event: self.Paddle_2.movePaddle(-0.03))
        self.InterfaceWindow.bind('<Down>', lambda event: self.Paddle_2.movePaddle(0.03))
        self.InterfaceWindow.bind('<W>', lambda event: self.Paddle_1.movePaddle(-0.03))
        self.InterfaceWindow.bind('<S>', lambda event: self.Paddle_1.movePaddle(0.03))
        self.InterfaceWindow.bind('<w>', lambda event: self.Paddle_1.movePaddle(-0.03))
        self.InterfaceWindow.bind('<s>', lambda event: self.Paddle_1.movePaddle(0.03))

        self.Game_Scores = Scores(self, 11, [self.width, self.height])


        timeNow = time.strftime("%H:%M")

        Thread(target=self.ballMovement).start()

    def ballMovement(self):
        while self.Game_Active:
            self.Ball_Position[0] += self.Ball_Direction[0]
            self.Ball_Position[1] += self.Ball_Direction[1]
            self.Ball.place(relx=self.Ball_Position[0], rely=self.Ball_Position[1])
            if self.Ball_Position[1] > 0.95 or self.Ball_Position[1] < 0.05:
                self.Ball_Direction[1] *= -1
            if self.Ball_Position[0] >= self.Paddle_2.Paddle_Location[0] - 0.01:
                if self.Paddle_2.Paddle_Location[0] + 0.22 > self.Ball_Position[1] > self.Paddle_2.Paddle_Location[1]:
                    self.Ball_Direction[0] *= -1
            if self.Ball_Position[0] <= self.Paddle_1.Paddle_Location[0]:
                if self.Paddle_1.Paddle_Location[1] + 0.22 > self.Ball_Position[1] > self.Paddle_1.Paddle_Location[1]:
                    self.Ball_Direction[0] *= -1
            if self.Ball_Position[0] > 1.0:
                self.Ball_Position = [0.45, 0.45]
                self.Game_Scores.incrementScore(0)
            elif self.Ball_Position[0] < 0.0:
                self.Ball_Position = [0.45, 0.45]
                self.Game_Scores.incrementScore(1)
            sleep(0.009)
        else:
            self.Ball.place_forget()
            self.Game_Information.config(text=f'{self.Game_Scores.Game_Winner.upper()} SIDE WINS THE GAME!')
            self.Game_Information.place(relx=.3, rely=.4)


class Scores:
    def __init__(self, instance, score, sizing):
        self.width = sizing[0]
        
        self.Game_Instance = instance
        self.Game_Winner = None
        self.Game_Scores = [0, 0]
        self.Game_Strings = ['Left', 'Right']
        self.Score_Limit = score
        self.Score_Frame = Frame(self.Game_Instance.Window, bg='#141414')
        self.Score_Frame.place(relx=.425, rely=.0, width=.15*self.Game_Instance.width, height=self.Game_Instance.height * .15)
        self.Score_A = Label(self.Score_Frame, font=('Franklin Gothic Heavy', instance.FontArray[6], ''), text='0', bg='#141414', fg='#95A5A6')
        self.Score_A.place(relx=.08, rely=.1)
        self.Score_B = Label(self.Score_Frame, font=('Franklin Gothic Heavy', instance.FontArray[6], ''), text='0', bg='#141414', fg='#95A5A6')
        self.Score_B.place(relx=.72, rely=.1)
        self.Score_Splitter = Label(self.Score_Frame, font=('Franklin Gothic Heavy', instance.FontArray[6], ''), text='-', bg='#141414', fg='#95A5A6')
        self.Score_Splitter.place(relx=.44, rely=.1)
        self.Score_Information = Label(self.Score_Frame, text=f'FIRST TO {self.Score_Limit}', font=('Franklin Gothic Heavy', 12, ''), bg='#141414', fg='#95a5a6', justify=CENTER)
        self.Score_Information.place(relx=.08, rely=.65)

    def incrementScore(self, index):
        self.Game_Scores[index] += 1
        self.updateScores()
        self.checkWinner()

    def updateScores(self):
        self.Score_A.config(text=self.Game_Scores[0])
        self.Score_B.config(text=self.Game_Scores[1])

    def checkWinner(self):
        for scores in self.Game_Scores:
            if scores == self.Score_Limit:
                self.Game_Instance.Game_Active = False
                self.Game_Winner = self.Game_Strings[self.Game_Scores.index(scores)]



class Paddle:
    def __init__(self, instance, position):
        self.Game_Instance = instance
        self.Paddle_Location = position
        self.Game_Paddle = Label(self.Game_Instance.Window)
        self.Game_Paddle.place(relx=self.Paddle_Location[0], rely=self.Paddle_Location[1], height=75, width=15)

    def movePaddle(self, direction):
        self.Paddle_Location[1] += direction
        self.Game_Paddle.place(relx=self.Paddle_Location[0], rely=self.Paddle_Location[1])


