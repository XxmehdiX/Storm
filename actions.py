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
    sleep(0.2)
    print(Fore.RED+"[3]  "+Fore.CYAN+"|Http Methods|"+"\n")
    sleep(0.2)
    print(Fore.RED+"[4]  "+Fore.CYAN+"|Insecure Http header|"+"\n"+"\n")
    
    num = input(Fore.YELLOW+"[-] Enter the number => ")
    
    if num == "1" :
        Info_website()
    elif num == "2" :
        Ip_site()
    elif num == "3" :
        http_method()
    elif num == "4" :
        inscure_http()


def osname():
    osn = platform.uname()[0]

    if osn=="Windows" :
        system("cls")
    elif osn=="Linux" :
        system("clear")


def Info_website():
    osname()
    url = input("Enter the Url "+"Using  " + Fore.YELLOW+"https:// => ")
    
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
                print("\n")
        except:
                print(Fore.RED+"[!] The URL Invalid")
    else :
        osname()
        print(Fore.RED+"[!] Plese use https:// , http:// in your URL")


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
            print("\n"+Fore.YELLOW+"[+] IP site ==> ",check+"\n")
        except:
            osname()
            print(Fore.RED+"[!] The URL Invalid"+"\n")


def ip_user() :
    osname()
    
    ip = input("Enter The Ip Target => ")
    info = requests.get("http://ip-api.com/"+ip)
    print(info.text)


def proxy() :
    
    osname()
    vpn = input(Fore.RED+"please go turn on your VPN \nif Your VPN is on click ENTER For continue... ")
    osname()
    
    print(Fore.GREEN+"---Welcom---"+"\n"+"\n")
    print(Fore.RED+"[1]  "+Fore.CYAN+"HTTP"+"\n")
    print(Fore.RED+"[2]  "+Fore.CYAN+"SOCKS4"+"\n")
    print(Fore.RED+"[3]  "+Fore.CYAN+"SOCKS5"+"\n")
    
    try :
        num = int(input("Select your type ==> "))

        if num == 1 :
            url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        elif num == 2 :
            url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all"
        elif num == 3 :
            url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
        else :
            print(Fore.RED+"[!]  please Select True Number")
        http = requests.get(url)
        response = http.text
        
        file1 = open("Proxys.txt","a+")
        file1.write(response.replace("\n",""))
        file1.close()
        
        osname()
        print(Fore.GREEN+"The proxys Save in the proxys.txt")
        sleep(2)
        
    except :
        osname()
        print(Fore.RED+"[!] Select True Number , or Check Your VPN")


def http_method() :
    osname()
    print(Fore.GREEN+"In This Section, We Check What the Website has http requests...")
    print("")
    
    web = input(Fore.YELLOW+"Enter The WebSite Name "+"Using  " + Fore.GREEN+"https:// => ")
    
    if "https://" in web[:8] or "http://" in web[:7] :
        
        verbs = ['GET', 'POST', 'PUT',"delete", 'OPTIONS', 'TRACE','TEST']

        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 
                "Cookie" : "mkt=en-US;ui=en-US;SRCHHPGUSR=NEWWND=0&ADLT=DEMOTE&NRSLT=50" ,
                "Accept-Language" : "en-us,en" }

        for verb in verbs:
            try:    
                req = requests.request(verb,web,headers=hdr)
                print(Fore.GREEN+"------------")
                print (Fore.GREEN+verb, req.status_code,req.reason)
                print(Fore.GREEN+"------------")
                if verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
                    print ('Possible Cross Site Tracing vulnerability(XST) Found')
            except:
                pass
    else :
        osname()
        print(Fore.RED+"[!] Plese use https:// , http:// in your URL")


def inscure_http() :
    osname()
    
    print(Fore.GREEN+"Which Security Options Are There Or Not At Response Headers")
    print("")
    
    web = input(Fore.YELLOW+"Enter The WebSite Name "+"Using  " + Fore.GREEN+"https:// >>  : ")
    
    if "https://" in web[:8] or "http://" in web[:7] :
        url = web

        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)', 
                "Cookie" : "mkt=en-US;ui=en-US;SRCHHPGUSR=NEWWND=0&ADLT=DEMOTE&NRSLT=50" ,
                "Accept-Language" : "en-us,en" }

        req = requests.get(url,headers=hdr)

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
    else :
        osname()
        print(Fore.RED+"[!] Plese use https:// , http:// in your URL")