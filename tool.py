"""
Name: Automation Tool
Author :  Samir Nabadov
Position: DevOps Engineer
Description : Automation Tool based Python
Source Code Website : www.github.com/...
"""
import sys, os, pyfiglet, subprocess, time

from modules.uptime import *
from modules.subnetCalculator import *
from modules.system import *
from modules.user import *
from modules.file import *
from modules.process import *
from modules.passwd import *
from modules.status import *
from modules.scan import *

usage = """
Optional arguments:
    scan                        Port scanner
    system                      Get details about system
    disk                        Get details about disks
    file                        Find large size files on the system
    user                        Determining user expiration times (must be sudo priviledge)
    process                     Get process highest memory useage
    exists                      Check if the process is alive
    passwd                      Password validator
    pwdgenerator                Password generation
    network                     Check the connection
    calculator                  Subnet calculator
    site                        Check the web site is reacable
    filestatus                  Check file status
    time                        Check uptime
    h, help                     help
    q, quit, exit               exit from tool
    """

def banner():
    os.system("clear")
    print("-----------------------------------------------------------------------------")
    result = pyfiglet.figlet_format("Automation Tool")
    print(result)
    print("-----------------------------------------------------------------------------")
    
def header():
    banner()
    print(usage)

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()

    show(0)

    for i, item in enumerate(it):
        yield item
        show(i+1)

    file.write("\n")
    file.flush()

def package():
    for i in progressbar(range(10), "Loading: ", 100):
        time.sleep(0.1)

    output = subprocess.Popen("pip install -r requirements.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if "" == output.stderr.readline():
        return True
    else:
        return False

def main():
    banner()
    print("Installing required packages...")
    
    if package() == True:
        print("Installation successfully required packages!")
        time.sleep(1)
        header()
    else:
        print("Installation failed. Exiting...")
        sys.exit(1)

    while True:
        option = str(input("Enter your option: ")).lower()
        if option == "scan":
            portScan()
        elif option == "system":
            osDetail()
        elif option == "disk":
            diskDetail()
        elif option == "file":
            getFile()
        elif option == "user":
            checkExpire()
        elif option == "process":
            getProcessHighestMemoryUsage()
        elif option == "exists":
            processExists()
        elif option == "passwd":
            checkPasswordStrength()
        elif option == "pwdgenerator":
            generateRandomPassword()
        elif option == "network":
            socketNet()
        elif option == "site":
            isSiteReachable()
        elif option == "calculator":
            subnetCalc()
        elif option == "filestatus":
            fileStatus()
        elif option == "time":
            timeDetails()
        elif option == "h" or option == "help":
            header()
        elif option == "q" or  option == "quit" or option == "exit":
            print("Exiting...")
            sys.exit(1)
        else:
            print("Incorrect option!")

if __name__ == '__main__':
    main()
    