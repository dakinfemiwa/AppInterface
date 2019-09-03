import os, sys
import importlib

class run:
    def __init__(self):
        self.Dir1 = os.getcwd()
        self.Dir2 = self.Dir1 + "\\Apps\\Hidden\\Starter"
        os.chdir(self.Dir2)
        print(os.getcwd())
        self.importModules()

    def importModules(self):
        startInterface = importlib.import_module("Apps.Hidden.Starter.startInterface")
        startInterfaceClass  = getattr(startInterface, "startInterface")
        instance = startInterfaceClass(self.Dir1, self.Dir2)

if __name__ in '__main__':
    run()