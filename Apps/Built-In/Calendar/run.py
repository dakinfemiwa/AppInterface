import tkinter
from tkinter import *
import time
import calendar

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
        self.FontArray = self.MainInterface.Fonts
        AppScreen = self.AppScreen

        AppScreen.config(highlightthickness = 0, bd = 0, borderwidth = 0, relief = RIDGE)

        self.month = int(time.strftime("%m"))
        self.year = int(time.strftime(("%Y")))

        print(self.month)

        self.calendarMonth =  calendar.month(self.year, self.month)
        self.calendarYear = calendar.calendar(self.year)

        self.Font1 = round(FontArray[6] * 0.9)

        self.CalendarLabel = Text(AppScreen, font=("Segoe", self.Font1), bg="#262626", fg="white", bd=2)
        self.CalendarLabel.insert(END, "\n" + self.calendarMonth)
        self.CalendarLabel.config(state=DISABLED, padx=self.padding, pady=self.padding)
        self.CalendarLabel.place(relx=.0, rely=.0, width=self.screenWidth * .4, height=self.screenHeight*.8)

        InterfaceWindow.mainloop()


