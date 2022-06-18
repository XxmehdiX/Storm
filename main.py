from colorama import Fore , init
from time import sleep
from actions import ip_user,proxy,menu_web,Banner,osname

def Menu() :
    osname()

    init()
    sleep(0.2)
    Banner()

    sleep(0.2)
    print(Fore.RED+"[1]  "+Fore.CYAN+"|Web Option|"+"\n")
    sleep(0.2)
    print(Fore.RED+"[2]  "+Fore.CYAN+"|Get User information with IP|"+"\n")
    sleep(0.2)
    print(Fore.RED+"[3]  "+Fore.CYAN+"|Get proxy list(Turn on your vpn)|"+"\n")
    sleep(0.2)
    print(Fore.RED+"[4]  "+Fore.CYAN+"|Exit|"+"\n"+"\n")
    sleep(0.2)

    num = input(Fore.YELLOW+"[-] Enter the number => ")

    if num == 1 or 2 or 3 or 4 or 5:
        if num == "1" :
            menu_web()
        elif num == "2" :
            ip_user()
        elif num == "3" :
            proxy()
        elif num == "4" :
            print("")
            pass
        else :
            print("\n"+Fore.RED+"[!] ERROR , Select True Number")
            sleep(3)
            osname()
Menu()