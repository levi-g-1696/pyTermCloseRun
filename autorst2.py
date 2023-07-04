import csv
import os
import time
from subprocess import call
from subprocess import Popen, CREATE_NEW_PROCESS_GROUP, DETACHED_PROCESS
from collections import namedtuple

configfile= ".\\config.csv"
##############################################################
def confreader():
 #   file= globalConfig.configFile
    isEnable=[]
    file=configfile
    appName=[]
    cmdIdentString=[]
    argIdentString= []
    enable=[]

    isAlertEnable=[]
    protocol = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            isEnable= row[3]
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif isEnable=="0" :
                line_count += 1
            else:
                appName.append(row[0])
                cmdIdentString.append(row[1])
                argIdentString.append(row[2])
                enable.append(row[3])
                line_count += 1


    config=  namedtuple('config', 'appName cmdString argString isEnable')
    res = config(appName, cmdIdentString, argIdentString, isEnable )
    return res

################################################
def isAppInRunnigList(cmd,arg):
    output2 = os.popen('wmic process get commandline, description, processid').read()
    processList = output2.split("\n")
    found = False
    for item in processList:
        if cmd in item and (arg =="" or arg  in item):
            found= True

            break
    return  found



 ###########################################################
# Running the aforementioned command and saving its output
output2= os.popen('wmic process get description, processid').read()
output2 = os.popen('wmic process get commandline, description, processid').read()
processList= output2.split("\n")
for m in range (1000):
    found = False
    conf = confreader()
    appNames = conf.appName
    cmdLst = conf.cmdString
    argLst = conf.argString
    for j in range(len(cmdLst)):
        cmd = cmdLst[j]
        arg = argLst[j]
        if not isAppInRunnigList(cmd, arg):
            print (f"{cmd} on {arg} is not running\nTry to open")
            proc = Popen([cmd, arg],
                         creationflags=CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS)
        else:
            print(f"OK. {cmd} for {arg} is running  m:",m)
    time.sleep(5)
    output2 = os.popen('wmic process get commandline, description, processid').read()

    processList = output2.split("\n")

# for k in range (3):
#
#     for line in processList:
#
#       if "python"  in line:
#         found= True
#         print( line)
#     if not found:
#         print ("n++ is closed. try run n++")
#         path= r"C:\Program Files\Notepad++\notepad++.exe"
#         proc = Popen([path, ],
#                      creationflags=CREATE_NEW_PROCESS_GROUP | DETACHED_PROCESS)
#        # os.spawnl(os.P_NOWAIT,  # flag
#        #           path,  # programm
#         #          path, "--startup")  # arguments
#       #  call ([r"C:\Program Files\Notepad++\notepad++.exe"])
#         print ("after run n++")
#         found = True
#     else : print ("n++ is open")
#     time.sleep(2)
#     output2 = os.popen('wmic process get commandline, description, processid').read()
#
#     linelist = output2.split("\n")
