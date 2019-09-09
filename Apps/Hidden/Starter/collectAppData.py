import os, sys
import importlib
import airtable

class collect:
    def __init__(self, Dir):
        self.OriginalDirectory = Dir
        self.getOnlineRecords()
        self.collectDownloadedData()
        print("Collecting data...")

    def display(self):
        print("HI!!!")

    def add(self, action):
        self.sheet2.insert_row(action, 2)

    def getOfflineData(self):
        dir = os.getcwd()
        os.chdir(dir + "\\Data")



    def getOnlineRecords(self):
        os.chdir(self.OriginalDirectory + "\\Apps\\Hidden\\Starter\\Data")
        sys.path.append(self.OriginalDirectory + "\\Apps\\Hidden\\Starter\\Data")
        with open("tool1a.pdf", "r") as toolFile:
            tools = toolFile.readlines()
            a = tools[0]

        with open("tool1b.pdf", "r") as toolFile:
            tools = toolFile.readlines()
            b = tools[0]

        #from tool2a import encryptText

        c = importlib.import_module("tool2a")

        class_ = getattr(c, "encryptText")
        DeCipher = class_(a)
        DeCipher.decrypt()
        a = str(DeCipher.plaintext)

        DeCipher = class_(b)
        DeCipher.decrypt()
        b = str(DeCipher.plaintext)

        #a = "app3vyBPcNfb9yJY5"
        tableName = "User"
        #b = "keyo7Gn0KX5IV0E8v"

        self.usersList = airtable.Airtable(a, "User", b)
        self.filesList = airtable.Airtable(a, "Files", b)
        self.appInformation = airtable.Airtable(a, "AppInfo", b)

        self.usersList1 = self.usersList.get_all()
        self.filesList1 = self.filesList.get_all()
        self.appInformation1 = self.appInformation.get_all()


        os.chdir(self.OriginalDirectory)

    def collectDownloadedData(self):
        #Changes directory to the directory of the apps file
        self.Dir = os.getcwd()

        self.DirApps = self.OriginalDirectory + "\\Apps"
        os.chdir(self.DirApps)

        dataTypes = ["Built-In", "Downloaded"]

        #Sets a temporary variable and the variable being referenced
        self.appsOffline = []
        self.appsOffline1 = []
        self.appsOffline2 = []

        for dataType in dataTypes:
            dir = os.getcwd()
            os.chdir(dir + "\\" + dataType)
            apps = os.listdir()
            apps.remove("__init__.py")
            for app in apps:
                i = apps.index(app)
                self.appsOffline.append([])
                l = len(self.appsOffline)
                self.appsOffline[l-1].append(app)
                self.appsOffline[l-1].append(dataType)
            os.chdir(dir)

        os.chdir(self.Dir)

if __name__ in '__main__':
    collect("C:/Users/Abisucceed/OneDrive/David2/A LEVEL STUFF/PROGRAMS/Interface")
