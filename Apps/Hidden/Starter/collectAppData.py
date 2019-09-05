import os, sys
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

        for tool in tools:
            tool.strip("\n")


        a = tools[0]
        b = tools[1]

        from tool2a import encryptText
        DeCipher = encryptText(a)
        DeCipher.decrypt()
        a = DeCipher.plaintext

        DeCipher = encryptText(b)
        DeCipher.decrypt()
        b = DeCipher.plaintext

        self.usersList = airtable.Airtable(a, "User", b)
        self.filesList = airtable.Airtable(a, "Files", b)
        self.appInformation = airtable.Airtable(a, "AppInfo", b)

        os.chdir(self.OriginalDirectory)

    def collectDownloadedData(self):
        #Changes directory to the directory of the apps file
        self.Dir = os.getcwd()

        self.DirApps = self.Dir + "\\Apps"
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
    collect()
