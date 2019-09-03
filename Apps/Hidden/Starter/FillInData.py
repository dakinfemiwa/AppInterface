import os



directory = os.getcwd()
os.chdir(directory + "\\Data")

link ="https://raw.githubusercontent.com/interfaceLogins/InterfaceData/master/tool1a.pdf"

with open("tool1b.pdf", "w") as fillInData:
    fillInData.write(link)