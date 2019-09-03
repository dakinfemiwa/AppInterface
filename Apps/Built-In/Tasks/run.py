import tkinter
from tkinter import *
import time
import calendar

class RunP:
    def __init__(self, AppScreen, AppName, FontArray, InterfaceWindow):
        self.AppScreen = AppScreen
        self.AppName = AppName
        self.screenWidth = width
        self.screenHeight = height
        print(self.AppName)

        self.month = int(time.strftime("%m"))
        self.year = int(time.strftime(("%Y")))

        self.calendarMonth =  calendar.month(self.year, self.month)
        self.calendarYear = calendar.calendar(self.year)

        self.CalendarLabel = Label(AppScreen, text=self.month, font=FontArray[6])
        self.CalendarLabel.place(relx=.05, rely=.05)

        InterfaceWindow.mainloop()



