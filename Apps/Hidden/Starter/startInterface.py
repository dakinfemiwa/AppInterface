import tkinter
from tkinter import *
import os, sys


class startInterface:
    def __init__(self, dir, dir2):
        self.dir = dir
        sys.path.append(dir2)
        os.chdir(dir2)

        self.checkLogin()


        self.launchHome()

    def checkLogin(self):
        from collectAppData import collect
        self.data = collect(self.dir)
        #self.data.collectOfflineData

    def launchHome(self):
        from homepage import Homepage
        print(self.dir)
        Homepage(self.dir)



