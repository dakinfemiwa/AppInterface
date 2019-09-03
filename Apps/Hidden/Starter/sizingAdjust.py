import tkinter
from tkinter import *

class sizingAdjust:
    def __init__(self, file, fonts, padding):
        self.width1 = file.winfo_screenwidth()
        self.height1 = file.winfo_screenheight()
        self.fonts = fonts
        self.padding = padding

        self.sizeWindow()
        self.determinePos()
        self.makeFonts()

    def sizeWindow(self):

        ratio = self.width1 / self.height1
        #print(ratio)

        if ratio < 2:
            self.width = self.width1
            self.height = self.width / 2
        else:
            self.height = self.height1
            self.width = self.height1 * 2

        #print("Sizing:", (self.width1, self.height1) )


    def determinePos(self):
        self.canvasPosY = (self.height1 - self.height) / (2 * self.height1)

        if self.width1 > 4000:
            self.canvasPosX = (self.width1 - 4000) / (2 * self.width)
            self.oversize = True
        else:
            self.canvasPosX = 0
            self.oversize = False

    def makeFonts(self):
        if self.width1 >=600 and self.width1 <=675:
            for font in self.fonts:
                i = self.fonts.index(font)
                self.fonts[i] *= (self.width1 / 1650)
                self.padding  *= (self.width1 / 1650)
        elif self.width1 < 750:
            for font in self.fonts:
                i = self.fonts.index(font)
                self.fonts[i] *= (self.width1 / 1600)
                self.padding  *= (self.width1 / 1600)
        elif self.width1 < 1000:
            for font in self.fonts:
                i = self.fonts.index(font)
                self.fonts[i] *= (self.width1 / 1650)
                self.padding  *= (self.width1 / 1650)
        elif self.width1 <= 1200:
            for font in self.fonts:
                i = self.fonts.index(font)
                self.fonts[i] *= (self.width1 / 1550)
                self.padding *= (self.width1 / 1550)
        elif self.width1 < 1250:
            for font in self.fonts:
                i = self.fonts.index(font)
                self.fonts[i] *= (self.width1 / 1250)
                self.padding *= (self.width1 / 1250)
