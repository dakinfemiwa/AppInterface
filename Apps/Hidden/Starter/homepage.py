import importlib
import pygame
import tkinter
from tkinter import *
from sizingAdjust import sizingAdjust
from collectAppData import collect
import time
from playsound import playsound
import threading
import os, sys
#from appViewer import AppViewer

class Homepage:
    def __init__(self, dir):
        self.Fonts = [90, 80, 70, 60, 50, 40, 30]
        self.FontFamily = ["Segoe UI", "Ebrima"]
        self.backBackground="black"
        self.History = ["HOME"]
        self.AppView = False
        self.defaultSYSPath = sys.path
        self.appButtonsSelect = []
        self.padding = 80
        self.interfaceDirectory = dir
        print(dir)
        os.chdir(dir)
        self.interfaceDirectory1 = sys.path
        

        self.InterfaceWindow = Tk()
        sizing = sizingAdjust(self.InterfaceWindow, self.Fonts, self.padding)
        self.data = collect(self.interfaceDirectory)
        self.padding = sizing.padding
        #print("self.appOffline2", self.data.appsOffline2)
        self.InterfaceWindow.overrideredirect(1)
        self.InterfaceWindow.attributes("-topmost", True)
        self.InterfaceWindow.config(bg="black")
        self.Homepage = True
        self.appsOffline2 = self.data.appsOffline

        self.backgroundImg = PhotoImage(file="default.png")

        self.windowWidth = sizing.width
        self.windowHeight = sizing.height

        #print("Screen Size:", (sizing.width, sizing.height) )

        geometry = str(sizing.width1) + "x"+ str(sizing.height1) + "+0+0"
        self.InterfaceWindow.geometry(geometry)

        self.InterfaceCanvas = Canvas(self.InterfaceWindow, width=self.windowWidth, height=self.windowHeight)
        self.InterfaceCanvas.config(bg="white", highlightthickness=0, bd=0, borderwidth=0, relief=RIDGE)
        self.InterfaceCanvas.place(relx=sizing.canvasPosX, rely= sizing.canvasPosY)

        if sizing.oversize == True:
            self.foreground1 = "black"
        else:
            self.foreground1 = "white"
            self.InterfaceCanvas.create_image(0,0, image=self.backgroundImg)

        self.InterfaceCanvas.create_rectangle(0, .9*self.windowHeight, self.windowWidth, self.windowHeight, fill="black")

        self.Buttons = [["<", 0, True], ["⌂", 1, False], ["☐", 2, True]]
        self.ButtonA = []

        for Button1 in self.Buttons:
            i = self.Buttons.index(Button1)

            ButtonInterface = Button(self.InterfaceCanvas, text=self.Buttons[i][0], font=(self.FontFamily[0], round(self.Fonts[5])))
            ButtonInterface.config(bg="black", bd=0, highlightthickness=0, foreground="white", cursor="hand2")
            ButtonInterface.config(activebackground="black", activeforeground="gray")

            ButtonInterface.place(relx=i / 3, rely=.9, height=(self.windowHeight * .1), width=(self.windowWidth / 3))
            self.ButtonA.append(ButtonInterface)

        self.ButtonA[2].config(command=lambda: self.showApps())
        self.ButtonA[1].config(command=lambda: self.returnToHome())
        self.ButtonA[0].config(command=lambda: self.showPreviousTask())


        self.TimeNot = self.InterfaceCanvas.create_rectangle(0,0, self.windowWidth * (9/40), self.windowHeight *.9, fill="black")

        self.TimeCanvas = Frame(self.InterfaceCanvas, bd=0, background="black")
        self.TimeCanvas.place(relx=.0, rely=.0, width=self.windowWidth * (9/40), height=self.windowHeight / 2)

        self.TimeLabel = Label(self.TimeCanvas, font=(self.FontFamily[0], round(self.Fonts[0])), bg="black", fg="white")
        self.TimeLabel.place(relx=.0, rely=.3, width=self.windowWidth * (9/40))

        self.DateLabel = Label(self.TimeCanvas, font=(self.FontFamily[0], round(self.Fonts[6])), bg="black", fg="white")
        self.DateLabel.place(relx=.0, rely=.8, width=self.windowWidth * (9/40))

        self.TitleBar = Canvas(self.InterfaceCanvas, bg="black", width=self.windowWidth, highlightthickness=0, bd=0)

        self.TimeLabel1 = Label(self.TitleBar, font=(self.FontFamily[0], round(self.Fonts[6])), anchor=E, bg="black", fg="white")
        self.TimeLabel1.place(relx=.0, rely=.0, width=self.windowWidth)

        self.InterfaceWindow.bind("<Button-1>", lambda event: self.ChooseApp(event))

        threading.Thread(target=self.tick(), args=()).start()
        threading.Thread(target=self.dateChange(), args=()).start()
        threading.Thread(target=self.InterfaceWindow.mainloop(), args=()).start()

    def tick(self):
        time1 = time.strftime('%H:%M')
        self.TimeLabel.config(text=time1)
        self.TimeLabel.after(1000, lambda: self.tick())

    def tick1(self):
        time1 = time.strftime('%H:%M')
        self.TimeLabel1.config(text=time1)
        self.TimeLabel1.after(1000, lambda: self.tick())

    def dateChange(self):
        date1 = time.strftime("%d/%m/%Y")
        self.DateLabel.config(text=date1)
        self.DateLabel.after(100, lambda: self.dateChange())

    def ChooseApp(self, event):
        x = 0
        #print(self.appButtonsSelect)
        try:
            for app in range(0, len(self.appButtonsSelect)):
                #print((self.appButtonsSelect[app], app))
                if event.widget == self.appButtonsSelect[app]:
                    #print(self.data.appsOffline[app])
                    self.AppsList.destroy()
                    self.appViewer(self.data.appsOffline[app])
        except NameError:
            pass

    def returnToHome(self):
        self.appButtonsSelect = []
        #print(self.Homepage)
        if self.Homepage == True:
            pass
        else:
            try:
                self.AppScreen.destroy()
            except:
                pass
            self.TitleBar.place_forget()
            try:
                self.AppsList.destroy()
            except:
                pass

            self.data.appsOffline = self.appsOffline2

            self.TimeCanvas.place(relx=.0, rely=.0, width=self.windowWidth * (9 / 40), height=self.windowHeight / 2)
            self.TimeNot = self.InterfaceCanvas.create_rectangle(0, 0, self.windowWidth * (9 / 40), self.windowHeight * .9, fill="black")
            self.History.append("HOME")
            #print(self.History)
            self.Homepage = True

    def showApps(self):
        
        sys.path = [self.interfaceDirectory1]
        os.chdir(self.interfaceDirectory)
        self.appButtonsSelect = []
        #print(self.Homepage)
        if self.Homepage == True:
            try:
                self.InterfaceCanvas.delete(self.TimeNot)
                threading.Thread(target=self.tick1(), args=()).start()
                self.TimeCanvas.place_forget()
            except:
                pass
        else:
            pass

        print(("Finished",self.appButtonsSelect))

        #Place TitleBar
        self.TitleBar.place(relx=.0, rely=.0, width=self.windowWidth, height=self.windowHeight *.1)
        self.History.append("APPS")
        self.Homepage = False

        self.AppsList = Frame(self.InterfaceCanvas, bg="black")
        self.AppsList.place(relx=1/16, rely=1/4, width=(7/8)*self.windowWidth, height=self.windowHeight * .5)

        appBlock = 150

        self.numberOfOfflineApps = len(self.data.appsOffline[0])
        #print(self.windowWidth * (7/8))
        #print("Number of Apps:", self.numberOfOfflineApps)
        self.AppsOnARow = int((self.windowWidth * (7/8)) // appBlock)
        #print("Max number of Rows:", self.AppsOnARow)

        columns = (self.numberOfOfflineApps // self.AppsOnARow) + 1

        #print("Columns:", columns)


        #print(self.data.appsOffline)

        if columns == 1:
            for app in self.data.appsOffline:
                i = self.data.appsOffline.index(app)
                AppButton = Button(self.AppsList, text=app[0], bg="black", bd=0, fg="white", anchor=CENTER)
                AppButton.place(relx=(appBlock/self.windowWidth)*i, rely=0, width=appBlock, height=appBlock)
                self.appButtonsSelect.append(AppButton)
        else:
            for column in range(columns):
                for app in range(self.AppsOnARow):
                    i = (column * self.AppsOnARow) + app
                    if i < self.numberOfOfflineApps:
                        #print("Creating Icon for", self.data.appsOffline[0][i] )
                        AppButton = Button(self.AppsList, text=self.data.appsOffline[0][i].strip(" "), bg="black", bd=0, fg="white", anchor=CENTER)
                        AppButton.place(relx=(appBlock / self.windowWidth) * app, y=appBlock*(column), width=appBlock, height=appBlock * 0.9)
                        self.appButtonsSelect.append(AppButton)


        #print(self.appButtonsSelect)


    def returnToApps(self):
        self.AppScreen.destroy()
        self.showApps()


    def showPreviousTask(self):
        if len(self.History) == 1:
            if self.History[0] == "HOME":
                self.InterfaceWindow.destroy()
                quit()
        else:
            tasks = len(self.History)
            if self.History[tasks - 1] == "HOME":
                self.InterfaceWindow.destroy()
            elif self.History[tasks - 1] == "APPS":
                self.returnToHome()
            elif self.History[tasks - 1] == "APPVIEWER":
                self.returnToApps()

    def appViewer(self, app):
        self.AppView = True
        self.History.append("APPVIEWER")
        self.AppScreen = Canvas(self.InterfaceCanvas, bg="#262626", highlightthickness=0, bd=0, borderwidth=0, relief=RIDGE)
        self.AppScreen.place(relx=.0, rely=.1, width=self.windowWidth, height=self.windowHeight * .8)

        appName = app[0]
        appFile = app[1]

        #print((appName, appFile))

        #action = "opened app:" + appName

        #time = time.strftime("%H:%M")

        #actions = ["Guest", appName, action, time]
        #print(actions)



        #print(self.data.Dir)
        self.Dir = self.data.Dir + "\\" + "Apps" + "\\" + appFile
        self.newDir = self.data.Dir + "\\" + "Apps" + "\\" + appFile + "\\" + appName

        #print(self.newDir)

        os.chdir(self.Dir)

        sys.path = [self.Dir]
        #print(sys.path)
        #print()

        a = appName + "." "run"
        #print(a)



        b = importlib.import_module(a)

        class_ = getattr(b, "runApp")
        instance = class_(self, appName)

        #b.main(self.AppScreen, appName, self.windowWidth, self.windowHeight, self.Fonts, self.InterfaceCanvas, self.padding, self.newDir)

        #if __name__ in '__main__':
            #b(self.AppScreen, appName, self.windowWidth, self.windowHeight, self.Fonts, self.InterfaceCanvas, self.padding)



