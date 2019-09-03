import gspread
import os, sys
from oauth2client.service_account import ServiceAccountCredentials
import urllib.request
import sqlite3

import pprint

class collect:
    def __init__(self):
        #self.getOnlineRecords()
        #self.collectDownloadedData()
        print("Collecting data...")

    def display(self):
        print("HI!!!")

    def add(self, action):
        self.sheet2.insert_row(action, 2)

    def getOfflineData(self):
        dir = os.getcwd()
        os.chdir(dir + "\\Data")



    def getOnlineRecords(self, file):
        link = "https://raw.githubusercontent.com/dakinfemiwa/Tools/master/Tool2/tool2a.py"
        fileName = "tool2a.py"

        urllib.request.urlretrieve(link, fileName)

        from tool2a import Cryptographer
        Cryptographer.encrypt(file)
        Cryptographer.decrypt(file)

        with open("tool1a.txt", "r") as accountRead:
            accountsStr = accountRead.readlines()

        accounts = []

        for account in accountsStr:
            accountArray = account.split(",")
            print(accountArray)
            for data in accountArray:
                i = accountArray.index(data)
                if data == "":
                    accountArray.remove(data)
                elif "\n" in data:
                    data = data[0:len(data) - 2]
                    accountArray[i] = data
                    if data == "":
                        accountArray.remove(data)
            accounts.append(accountArray)

        print()
        for account in accounts:
            print(account)

        Cryptographer.encrypt(file)

        os.remove("tool2a.py")"""
        
        
        try:
            with open("link.pdf", "r") as linkFile:
                urlA = linkFile.readlines()
                url = urlA[0]
        except:
            pass

        url = "https://raw.githubusercontent.com/dakinfemiwa/Tools/master/Tool1/tool1b.json?token=AGOA24MNPQFJSNFTCZAW2ZC5OEUYW"

        urllib.request.urlretrieve(url, "tool1b.json")


        #Accesses sheet from Google sheets
        self.scope1 = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.creds1 = ServiceAccountCredentials.from_json_keyfile_name('tool1b.json', self.scope1)
        self.client1 = gspread.authorize(self.creds1)
        self.sheet1 = self.client1.open('GameRecordsSheets').sheet1
        self.sheet2 = self.client1.open('InterfaceActions').sheet1

        os.remove("tool1b.json")

        #Collects the name of the app and the ID
        self.appsOnlines1 = self.sheet1.col_values(3)
        self.gameIDNo = self.sheet1.col_values(1)

        #Variable for the apps online
        self.appsOnline = []

        #Data containts repeated use of files, so algorithm selecets one name and one gameID
        j = 0
        for game in self.appsOnlines1:
            i = self.appsOnlines1.index(game)
            if i == j:
                pass
            else:
                self.appsOnline.append([])
                self.appsOnline[len(self.appsOnline) - 1].append(game)
                self.appsOnline[len(self.appsOnline) - 1].append(self.gameIDNo[i])
            j = i




        #print(self.appsOnline)"""

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
