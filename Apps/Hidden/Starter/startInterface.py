import tkinter
from tkinter import *
import os, sys


class startInterface:
    def __init__(self, dir, dir2):
        sys.path.append(dir2)
        os.chdir(dir2)

        self.checkLogin()


        self.launchHome()

    def checkLogin(self):
        from collectAppData import collect
        self.data = collect()
        self.data.collectOfflineData

    def launchHome(self):
        from homepage import Homepage
        Homepage(dir)



