# Recoded By IQ1
# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhottool
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhottool")
    time.sleep(1)
    os.system('python2 bhot.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		

##### LOGO #####
logo="""
\033[1;96m ------------------------
 \033[1;32m < OFFICIAL RECODE By IQ1 >
 \033[1;96m ------------------------
\033[1;91m        _   _ _ _    _ _ 
\033[1;91m       | | /  _  \ /    |
\033[1;91m       | ||  | |  ||__  |
\033[1;91m       | ||  |_|  |  |  |
\033[1;91m       | | \_ _  /  _|  |_
\033[1;91m       |_|     \_\ |_ _ _ |                                             
\033[1;93m  INI BUKAN HANYA NAMA, INI MEREK
\033[1;97m---------------------------------------
\033[1;95m
 AUTHOR     : IQ1
 FACEBOOK   : FACEBOOK.COM/NoFacebook
 YOUTUBE    : YOUTUBE.COM/NoYoutube
 GITHUB     : GITHUB.COM/NoGithub
\033[1;32m
------------------------------------------------
                                """

cusr = "iq1"
cpwd = "iq198"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/NoYoutube')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : iq1 (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : iq1 (correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/NoFacebook')
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print(" TOOL USERNAME : iq1 (correct)")
    print(" TOOL PASSWORD : iq198 (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    jalan("\033[1;93mSilakan Tunggu 2 Menit, Mengecek Semua Paket.....")
  
    time.sleep(1)
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
