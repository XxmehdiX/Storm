from colorama import Fore , init
from time import sleep
from actions import ip_user,menu_web,Banner,osname
import requests


def Menu() :
    try :
        req = requests.get("https://www.google.com").status_code
        if req == 200 :
            osname()

            init()
            sleep(0.2)
            Banner()

            sleep(0.2)
            print(Fore.RED+"[1]  "+Fore.CYAN+"|Web Option|"+"\n")
            sleep(0.2)
            print(Fore.RED+"[2]  "+Fore.CYAN+"|Get User information with IP|"+"\n")
            sleep(0.2)
            print(Fore.RED+"[3]  "+Fore.CYAN+"|Exit|"+"\n"+"\n")
            sleep(0.2)

            num = input(Fore.YELLOW+" ┌─["+Fore.LIGHTGREEN_EX+"STORM"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")

            if num == "1" :
                menu_web()
            elif num == "2" :
                ip_user()
            elif num == "3" :
                print("")
                pass
            else :
                print("\n"+Fore.RED+"[!] ERROR , Select True Number")
                sleep(3)
                osname()
        else : 
            osname()
            print(Fore.RED+"ERROR")
    except :
        osname()
        print(Fore.RED+"ERROR , Check Your Internet")
        pass
Menu()