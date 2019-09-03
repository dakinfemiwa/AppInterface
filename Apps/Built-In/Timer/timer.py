import tkinter
from tkinter import *
import datetime
import time
import threading
import os,sys
import pygame
from pygame import mixer
from playsound import playsound


class runApp:
    def __init__(self, AppScreen, AppName, width, height, FontArray, InterfaceWindow, padding):
        print("RUNNING CLASS")
        self.AppScreen = AppScreen
        self.AppName = AppName
        self.screenWidth = width
        self.screenHeight = height
        self.padding = padding
        self.InterfaceWindow = InterfaceWindow
        print(self.AppName)
        self.secondT = 0
        self.Stop = True
        self.FontArray = FontArray

        mixer.init()

        AppScreen.config(highlightthickness=0, bd=0, borderwidth=0, relief=RIDGE)

        self.Clock = Label(AppScreen, text="00:00:00.0", font=("Segoe UI", self.FontArray[3]), bg="#262626", fg="white")
        self.Clock.place(relx=.0, rely=.0, width=self.screenWidth, height=.4 * self.screenHeight)

        self.StartButton = Button(AppScreen, text=" ▶ ", command=lambda: self.startClock(), bg="black", fg="white",
                                  cursor="hand2", bd=0)
        self.StartButton.place(relx=.415, rely=.5, width=self.screenWidth * .05, height=self.screenHeight * .1)

        self.PauseButton = Button(AppScreen, text=" ⏸ ", command=lambda: self.pauseClock(), bg="black", fg="white",
                                  cursor="hand2", bd=0)
        self.PauseButton.place(relx=.475, rely=.5, width=self.screenWidth * .05, height=self.screenHeight * .1)

        self.StopButton = Button(AppScreen, text=" ⬛ ", command=lambda: self.endClock(), bg="black", fg="white",
                                 cursor="hand2", bd=0)
        self.StopButton.place(relx=.535, rely=.5, width=self.screenWidth * .05, height=self.screenHeight * .1)

        self.Buttons = [self.StartButton, self.PauseButton, self.StopButton]

        for button in self.Buttons:
            button.config(font=FontArray[3])

        self.getTime()

    def getTime(self):
        self.a = Frame(self.AppScreen, bg="black")
        self.a.place(relx=.2, rely=.2, width=self.screenWidth * .5, height=self.screenHeight * .5 * .8)

        self.HoursEntry = Entry(self.a, font=("Segoe UI", self.FontArray[3]), bg="white", fg="black", bd=0)
        self.HoursEntry.place(relx=.1, rely=.1, width=self.screenWidth * .1, height=self.screenHeight * .2)

        self.MinutesEntry = Entry(self.a, font=("Segoe UI", self.FontArray[3]), bg="white", fg="black", bd=0)
        self.MinutesEntry.place(relx=.4, rely=.1, width=self.screenWidth * .1, height=self.screenHeight * .2)

        self.SecondsEntry = Entry(self.a, font=("Segoe UI", self.FontArray[3]), bg="white", fg="black", bd=0)
        self.SecondsEntry.place(relx=.7, rely=.1, width=self.screenWidth * .1, height=self.screenHeight * .2)

        self.SelectButton = Button(self.a, text="START", command=lambda: self.process(),
                                   font=("Segoe UI", self.FontArray[5]))
        self.SelectButton.config(bg="darkgray", fg="white", bd=0, cursor="hand2")
        self.SelectButton.place(relx=0, rely=.8, width=self.screenWidth * .5, height=self.screenHeight * .5 * .8 * .2)

        self.Entries = [self.HoursEntry, self.MinutesEntry, self.SecondsEntry]

        for entry in self.Entries:
            entry.config(justify=RIGHT, bg="#0A0A0A", fg="white")

        for colonSeperation in range(2):
            colon = Label(self.a, text=":", font=("Segoe UI", self.FontArray[3]), bg="black", fg="white")
            colon.place(relx=(colonSeperation * .3) + .35, rely=.15)

        self.HoursEntry.insert(0, 0)
        self.MinutesEntry.insert(0, 0)
        self.SecondsEntry.insert(0, 1)

        self.a.bind("<Key>", lambda event: self.validate())

    def validate(self, event):
        for entry in self.Entries:
            i = self.Entries.index(entry)
            if entry.get().isdigit() == False:
                entry.delete(0, END)
                if i == 2:
                    entry.insert(0, 1)
                else:
                    entry.insert(0, 0)
            try:
                if int(entry.get()) < 0:
                    entry.delete(0, END)
                    if i == 2:
                        entry.insert(0, 1)
                    else:
                        entry.insert(0, 0)
                if i > 0:
                    if int(entry.get()) > 59:
                        if i == 2:
                            entry.insert(0, 1)
                        else:
                            entry.insert(0, 0)
            except:
                if i == 2:
                    entry.insert(0, 1)
                else:
                    entry.insert(0, 0)

            return True

    def process(self):
        self.Hours = int(self.HoursEntry.get())
        self.Minutes = int(self.MinutesEntry.get())
        self.Seconds = int(self.SecondsEntry.get())

        self.OriginalTime = (self.Hours * 3600) + (self.Minutes * 60) + self.Seconds
        self.Stop = False
        self.FormerTime = time.time()
        self.secondT = self.OriginalTime
        print((self.secondT))
        self.a.destroy()
        threading.Thread(target=lambda: self.timer(), args=()).start()

    def timer(self):
        # Function to run infinitely
        if self.Stop == False:
            t = time.time()
            # Increment value representing time passed to second Variable
            self.secondT -= (t - self.FormerTime)
            self.FormerTime = t
            # Converts to hours, minutes and seconds
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

            print(self.secondT)

            if self.secondT <= 0:
                self.Clock['text'] = "00:00:00.0"
                self.indicate()
                self.Stop = True
                return True

            # Display time
            self.Clock['text'] = "{0}:{1}:{2}".format(self.Hours, self.Minutes, self.second)

        self.Clock.after(75, lambda: self.timer())

    def indicate(self):
        mixer.music.load("ring.mp3")
        mixer.music.play()

    def startClock(self):
        self.Stop = False
        self.FormerTime = time.time()
        threading.Thread(target=lambda: self.timer(), args=()).start()
        return True

    def pauseClock(self):
        self.Stop = True
        return True

    def endClock(self):
        self.secondT = self.OriginalTime
        self.Clock['text'] = "00:00:00.0"
        self.Stop = True
        self.getTime()
        return True
