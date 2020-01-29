import os
import subprocess
import platform
from cpuinfo import get_cpu_info
import socket
from win32api import GetUserName
from mem import ram, ramtotal
import cpumodule
import intchoose
from datemodule import datefunc
import menusystem
import psutil

cls = lambda: print('\n' * 100)
ip_address = socket.gethostbyname(socket.gethostname())
username = GetUserName()
cbrand = get_cpu_info()['brand']

#Basic code help
#Before print text, use cls()
#Keep if selection == 0: always last
#Keep 99 reserved for back commands
#Use \n instead of print("")
#If no == comparing after while True, use os.system("pause")

#Else: break, if user has a choice to not go back

def cpuinfo():
    print("CPU Model:\n")
    print(get_cpu_info()["brand"])
    print(psutil.cpu_count(logical=False), "Cores")
    print(psutil.cpu_count(logical=True), "Threads\n")
    print("System architecture:", platform.machine(), "\n")

def modelcheck():
    if "3840QM" in cbrand:
        cls()
        os.system("start \"\" https://ark.intel.com/content/www/us/en/ark/products/70846/intel-core-i7-3840qm-processor-8m-cache-up-to-3-80-ghz.html")
        while True:
            try:
                pos = input("Press enter to go back.")
            except ValueError:
                cls()
                mainMenu()
            else:
                break

    else:
        print("\nSorry,", get_cpu_info()["brand"], "has not yet been added to the program's catalog.")
        while True:
            try:
                neg = input("Press enter to go back.")
            except ValueError:
                cls()
                mainMenu()
            else:
                break

#def tryfunction(phrase):
   #while True:
        #try:
            #int(input(phrase))
        #except ValueError:
            #cls()
            #mainMenu()
        #else:
            #break

def mainMenu():
    datefunc()
    print("\nHandy-Dandy Toolkit v0.3")
    print("--------------------------")
    print("1 - System information")
    print("2 - System Tweak Tools")
    print("3 - System Management")
    print("4 - System Tweaks")
    print("5 - About\n")
    selection_menu = int(input("Enter choice: "))

    if selection_menu == 1:
        cls()
        print("System Information Tools")
        print("------------------------")
        print("1 - System info (msinfo32.exe)")
        print("2 - System details\n")
        # tryfunction(phrase="Enter choice, or don't, it'll go back: ")
        while True:
            try:
                selection_menu1 = int(input("Enter choice, or don't, it'll go back: "))
            except ValueError:
                cls()
                mainMenu()
            else:
                break

        if selection_menu1 == 1:
            os.system("msinfo32.exe")
            print("\n")
            os.system("pause")

        if selection_menu1 == 2:
            # Selection menu 2 inside menu 1 inside menu
            cls()
            print("Available System Info")
            print("---------------------")
            print("1 - CPU")
            print("2 - Architecture")
            print("3 - OS Specific version")
            print("4 - RAM")
            print("5 - IP")
            print("6 - Username")
            print("0 - Help\n")
            # tryfunction(phrase="Enter your choice: ")
            while True:
                try:
                    selection_menu12 = int(input("Enter your choice: "))
                except ValueError:
                    cls()
                    mainMenu()
                else:
                    break

            if selection_menu12 == 1:
                cls()
                cpuinfo()
                while True:
                    try:
                        selection_menu121 = int(input("Type 1 to see more or press enter to go back."))
                    except ValueError:
                        cls()
                        mainMenu()
                    else:
                        break

                if selection_menu121 == 1:
                    modelcheck()

            if selection_menu12 == 2:
                cls()
                print("Architecture:")
                print(platform.machine())

            if selection_menu12 == 3:
                cls()
                print("Result:")
                print(platform.platform)

            if selection_menu12 == 4:
                cls()
                print("RAM Available in Gb's")
                print(round(ram), "Gb's\n")
                print("RAM Total in Gb's")
                print(ramtotal, "Gb's\n")
                print("The first number is usually correct, decimals might be wrong\nRam available seems to be okay.\n")
                while True:
                    try:
                        selection_menu124 = int(input("Press enter to go back."))
                    except ValueError:
                        cls()
                        mainMenu()
                    else:
                        break

            if selection_menu12 == 5:
                cls()
                print("IP Address:")
                print(ip_address)

            if selection_menu12 == 6:
                cls()
                print("Username:")
                print(username)

            if selection_menu12 == 0:
                cls()
                print("Available System Info Help")
                print("--------------------------\n")
                print("I don't think this category even needs a help section, like, look\nat this, it's all self explanatory!")

    if selection_menu == 2:
        cls()
        print("System Tweak Tools")
        print("------------------")
        print("1 - Registry editor")
        while True:
            try:
                selection_menu2 = int(input("Enter choice: "))
            except ValueError:
                cls()
                mainMenu()
            else:
                break

        if selection_menu2 == 1:
            os.system("regedit.exe")
            while True:
                try:
                    selection_menu21 = int(input("\nPress enter to go back."))
                except ValueError:
                    cls()
                    mainMenu()
                else:
                    break

    if selection_menu == 3:
        cls()
        print("System Management Tools")
        print("-----------------------")
        print("1 - Device manager")
        print("0 - Help\n")
        selection_menu3 = int(input("Enter choice: "))
        if selection_menu3 == 1:
            os.system("devmgmt.msc")
            while True:
                try:
                    selection_menu31 = int(input("\nPress enter to go back."))
                except ValueError:
                    cls()
                    mainMenu()
                else:
                    break

        if selection_menu3 == 0:
            cls()
            print("System Management Tools Help")
            print("----------------------------\n")
            print("Device manager")
            print("Well, who doesn't know Device Manager? Ugh.. anyways,\nyou can manage your hardware settings here")
            while True:
                try:
                    selection_menu30 = int(input("\nPress enter to go back, or don't, it'll go anyways"))
                except ValueError:
                    cls()
                    mainMenu()
                else:
                    break

    if selection_menu == 4:
        cls()
        print("System Tweaks")
        print("------------")
        print("DNS Flush 1")
        print("SFC 2")
        print("Help 0\n")
        selection_menu4 = int(input("Enter choice:"))
        if selection_menu4 == 1:
            os.system('ipconfig /flushdns')

        if selection_menu4 == 2:
            os.system('sfc /scannow')
            #subprocess.call(['runas', '/user:Administrator', 'sfc /scannow'])
            print("Executing SFC.....")

        if selection_menu4 == 0:
            cls()
            print("System Tweak Help")
            print("-----------------\n")
            print("DNS Flush might help resolve network problems by resetting the\ndns address.\n")
            print("SFC aka System File Checker is a helpful tool to find and fix\nfound filesystem problems and corruptions. Corrupted system files\nmight make your PC crash more often and can create instability.\n")

    if selection_menu == 5:
        cls()
        print("A Small application made to work as an easier way to find information about")
        print("your computer and apply tweaks. Currently in alpha, new features are being implemented")
        print("as time goes on.")

    #Prototype function
    if selection_menu == 6:
        cls()
        print("Type something to search.")
        intchoose.searchvaluefunc()

# Main routine
cls()
mainMenu()
