# [first method]
""" import requests

def updateCheck():
    update=False
    
    # get downloaded version
    versionSource=open('Version.txt','r')
    versionContents = versionSource.read()
    print("local content is: "+versionContents)
    
    #gets newest version
    updateSource = requests.get("https://raw.githubusercontent.com/elitefantasy/AmazeX-Utility/main/Version.txt")
    updateContents = updateSource.text
    print("source content is: "+updateContents)
    
    #checks for updates
    for i in range(0,20):
        if updateContents[i] != versionContents[i]:
            print("There are data updates availible.\n\n")
            update = True
            break
    
    for i in range(22,42):
        if updateContents[i] != versionContents[i]:
            print("There are version updates availible.\n\n")
            update = True
            break
    
    if update == False:
        print("You are already running the most up to date version.\n\n")

updateCheck() """



# [Second Method]
import urllib.request

def updateCheck():
    update=False
    
    # get downloaded version
    versionSource=open('Version.txt','r')
    versionContents = versionSource.read()
    # print("local content is: "+versionContents)
    
    #gets newest version
    updateSource = urllib.request.urlopen("https://raw.githubusercontent.com/elitefantasy/AmazeX-Utility/main/Version.txt")
    updateContents = updateSource.read().decode('utf-8')
    # print("source content is: "+updateContents)
    
    #checks for updates
    for i in range(0,20):
        if updateContents[i] != versionContents[i]:
            print("There are data updates availible.\n\n")
            update = True
            break
    
    for i in range(22,42):
        if updateContents[i] != versionContents[i]:
            print("There are version updates availible.\n\n")
            update = True
            break
    
    if update == False:
        print("You are already running the most up to date version.\n\n")

updateCheck()