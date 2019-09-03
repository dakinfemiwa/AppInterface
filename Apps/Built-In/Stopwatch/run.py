import tkinter
from tkinter import *
import datetime
import time
import threading

class runApp:
    def __init__(self, instance, appName):
        print("RUNNING CLASS")
        self.MainInterface = instance
        self.AppScreen = self.MainInterface.AppScreen
        self.AppName = appName
        self.screenWidth = self.MainInterface.windowWidth
        self.screenHeight = self.MainInterface.windowHeight
        self.padding = self.MainInterface.padding
        self.InterfaceWindow = self.MainInterface.InterfaceWindow
        print(self.AppName)
        self.secondT = 0
        self.Stop = True
        self.FontArray = self.MainInterface.Fonts
        AppScreen = self.AppScreen

        AppScreen.config(highlightthickness = 0, bd = 0, borderwidth = 0, relief = RIDGE)

        self.Clock = Label(AppScreen, text="00:00:00.0", font=("Segoe UI", self.FontArray[3]), bg="#262626", fg="white")
        self.Clock.place(relx=.0, rely=.0, width=self.screenWidth, height=.4 * self.screenHeight)

        self.StartButton = Button(AppScreen, text=" ▶ ", command= lambda: self.startClock(), bg="black", fg="white", cursor="hand2", bd=0)
        self.StartButton.place(relx=.415, rely=.5, width=self.screenWidth * .05, height=self.screenHeight *.1)

        self.PauseButton = Button(AppScreen, text=" ⏸ ", command= lambda: self.pauseClock(), bg="black", fg="white", cursor="hand2", bd=0)
        self.PauseButton.place(relx=.475, rely=.5, width=self.screenWidth * .05, height=self.screenHeight *.1)

        self.StopButton = Button(AppScreen, text=" ⬛ ", command= lambda: self.endClock(), bg="black", fg="white", cursor="hand2", bd=0)
        self.StopButton.place(relx=.535, rely=.5, width=self.screenWidth * .05, height=self.screenHeight *.1)

        self.Buttons = [self.StartButton, self.PauseButton, self.StopButton]

        for button in self.Buttons:
            button.config(font=FontArray[3])

        threading.Thread(target=InterfaceWindow.mainloop(), args=()).start()

    def stopwatch(self):
        #Function to run infinitely
        if self.Stop == False:
            t = time.time()
            #Increment value representing time passed to second Variable
            self.secondT += (t- self.FormerTime)
            self.FormerTime = t
            #Converts to hours, minutes and seconds
            self.Hours = int(self.secondT // 3600)
            self.Minutes = int((self.secondT) // 60)
            self.second = self.secondT % 60

            self.second = round(self.second, 1)

            if self.Hours < 10:
                self.Hours = "0" + str(self.Hours)

            if self.Minutes < 10:
                self.Minutes = "0" + str(self.Minutes)

            if self.second < 10:
                self.second = "0" + str(self.second)

            #Display time
            self.Clock['text'] = "{0}:{1}:{2}".format(self.Hours, self.Minutes, self.second)
        self.Clock.after(100, lambda: self.stopwatch())

        return True


    def startClock(self):
        self.Stop = False
        self.FormerTime = time.time()
        threading.Thread(target= lambda: self.stopwatch(), args=()).start()
        return True

    def pauseClock(self):
        self.Stop = True
        return True
    
    def endClock(self):
        self.secondT = 0
        self.Clock['text'] = "00:00:00.0"
        self.Stop = True
        return True
