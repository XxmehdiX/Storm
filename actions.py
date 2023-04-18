import builtwith
from colorama import Fore,init
from os import system
from time import sleep
import socket
import requests
import platform


init()

def Banner():
    print(Fore.RED+"""                               _                                          
                              | |                                         
  ______ ______  __      _____| | ___ ___  _ __ ___   ___   ______ ______ 
 |______|______| \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |______|______|
                  \ V  V /  __/ | (_| (_) | | | | | |  __/                
                   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|""")
    print("\n"+"\n")

def menu_web() :
    osname()
    
    sleep(0.2)
    print(Fore.RED+"[1]  "+Fore.CYAN+"|Get website information|"+"\n")
    sleep(0.2)
    print(Fore.RED+"[2]  "+Fore.CYAN+"|Get website IP|"+"\n")
    sleep(0.5)
    print(Fore.RED+"[3]  "+Fore.CYAN+"|Http Methods|"+"\n")
    sleep(0.2)
    print(Fore.RED+"[4]  "+Fore.CYAN+"|Insecure Http header|"+"\n"+"\n")
    
    num = input(Fore.YELLOW+" ┌─["+Fore.LIGHTGREEN_EX+"STORM"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
    
    if num == "1" :
        Info_website()
    elif num == "2" :
        Ip_site()
    elif num == "3" :
        http_method()
    elif num == "4" :
        inscure_http()
    else :
        osname()
        print(Fore.RED+"Use the default number")


def osname():
    osn = platform.uname()[0]

    if osn=="Windows" :
        system("cls")
    elif osn=="Linux" :
        system("clear")


def Info_website():
    osname()
    url = input("Enter the Url Whith "+Fore.YELLOW+"https:// => ")
    
    if "https://" in url[:8] or "http://" in url[:7] :    
        try :
            http = requests.get(url)
            http_ = http.status_code
            if http_ == 200 :
                print(Fore.GREEN+"[-] Please Wait...")
                info = builtwith.parse(url)
                osname()
                for names in info:
                    name = names.replace("-"," ").title()
                    for val in info[names] :
                        sleep(0.1)
                        print(Fore.LIGHTBLUE_EX+names+" : "+Fore.RED+val)
                inp =str(input(Fore.GREEN+"\n\n\n\n\nfor back to menu click Enter..."))
                menu_web()
            menu_web()
        except:
                print(Fore.RED+"[!] The URL Invalid")
                sleep(3)
                menu_web()
    else :
        osname()
        print(Fore.RED+"[!] Plese use https:// , http:// in your URL")
        sleep(3)
        menu_web()


def Ip_site():
    osname()
    url = input("\n"+Fore.CYAN+"Enter the URL" +Fore.RED+"(with out https:// or http:// )"+Fore.CYAN+ "=> ")
    
    if "https://" in url:
        osname()
        print("\n"+Fore.RED+"[!] Please Select True url whith out https:// or http://")
    elif "http://" in url:
        osname()
        print("\n"+Fore.RED+"[!] Please Select True url whith out https:// or http://")
    else :
        try:
            check = socket.gethostbyname(url)
            osname()
            print("  \n\n"+Fore.YELLOW+"[+] IP site ==> ",check)
            inp =str(input(Fore.GREEN+"\n\n\n\n\nfor back to menu click Enter..."))
            menu_web()
        except:
            osname()
            print(Fore.RED+"[!] The URL Invalid"+"\n")
            sleep(3)
            menu_web()


def ip_user() :
    osname()
    
    ip = input("Enter The Ip Target => ")
    info = requests.get("http://ip-api.com/"+ip)
    osname()
    print(info.text)

def http_method() :
    osname()
    print(Fore.GREEN+"In This Section, We Check What the Website has http requests...")
    print("")
    
    web = input(Fore.YELLOW+"Enter The WebSite Name Whith "+Fore.GREEN+"https:// => ")
    
    if "https://" in web[:8] or "http://" in web[:7] :
        
        verbs = ['GET', 'POST', 'PUT',"delete", 'OPTIONS', 'TRACE','TEST']

        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 
                "Cookie" : "mkt=en-US;ui=en-US;SRCHHPGUSR=NEWWND=0&ADLT=DEMOTE&NRSLT=50" ,
                "Accept-Language" : "en-us,en" }
        osname()
        for verb in verbs:
            try:    
                req = requests.request(verb,web,headers=hdr)
                print(Fore.GREEN+"------------")
                print (Fore.GREEN+verb, req.status_code,req.reason)
                print(Fore.GREEN+"------------")
                print("")
                if verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
                    print ('Possible Cross Site Tracing vulnerability(XST) Found')
            except:
                pass
        inp =str(input(Fore.GREEN+"\n\n\nfor back to menu click Enter...\n\n"))
        menu_web()
    else :
        osname()
        print(Fore.RED+"[!] Plese use https:// , http:// in your URL")
        sleep(3)
        menu_web()


def inscure_http() :
    osname()
    
    print(Fore.GREEN+"Which Security Options Are There Or Not At Response Headers")
    print("")
    
    web = input(Fore.YELLOW+"Enter The WebSite Name whith " + Fore.GREEN+"https:// =>")
    
    if "https://" in web[:8] or "http://" in web[:7] :
        url = web

        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 
                "Cookie" : "mkt=en-US;ui=en-US;SRCHHPGUSR=NEWWND=0&ADLT=DEMOTE&NRSLT=50" ,
                "Accept-Language" : "en-us,en" }

        req = requests.get(url,headers=hdr)
        osname()
        print("")
        try:
            xssprotect = req.headers['X-XSS-Protection']
            if xssprotect != '1; mode=block':
                    print (Fore.GREEN+'X-XSS-Protection not set properly, XSS may be possible:', xssprotect)
        except:
            print (Fore.RED+'X-XSS-Protection not set, XSS may be possible')

        try:
            contenttype = req.headers['X-Content-Type-Options']
            if contenttype != 'nosniff':
                print (Fore.GREEN+'X-Content-Type-Options not set properly:',contenttype)
        except:
            print (Fore.RED+'X-Content-Type-Options not set')

        try:
            hsts = req.headers['Strict-Transport-Security']
        except:
            print (Fore.RED+'HSTS header not set, MITM attacks may be possible')

        try:
            csp = req.headers['Content-Security-Policy']
            print (Fore.GREEN+'Content-Security-Policy set:', csp)
        except:
            print (Fore.CYAN+'Content-Security-Policy missing')
        inp =str(input(Fore.GREEN+"\n\n\nfor back to menu click Enter..."))
        menu_web()
    else :
        osname()
        print(Fore.RED+"[!] Plese use https:// , http:// in your URL")
        sleep(3)
        menu_web()

def check_net() :
    try :
        req = requests.get("https://www.google.com").status_code
    except :
        print(Fore.RED+"ERROR , Check Your Internet")
        pass