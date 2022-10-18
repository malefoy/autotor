import time
import os
import subprocess
import requests
import socket


def ma_ip():
    url='https://ipinfo.io/ip'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:5555',https='socks5://127.0.0.1:5555'))
    return get_ip.text

def change():
    os.system("killall -HUP tor")
    print('[+] Your IP has been Changed to : '+str(ma_ip()))
    


print('''\033[1;32;40m \n
                   _          _______
        /\        | |        |__   __|
       /  \  _   _| |_ ___      | | ___  _ __
      / /\ \| | | | __/ _ \     | |/ _ \| '__|
     / ____ \ |_| | || (_) |    | | (_) | |
    /_/    \_\__,_|\__\___/     |_|\___/|_|
                                            V 3.0 by Malefoy
                                                                       ''')


os.system("service tor start")
time.sleep(3)

print("\033[1;32;40m change your  SOCKES to 127.0.0.1:5555 \n")

x = input("[+] time to change Ip in Sec [type=60] >> ")
lin = input("[+] how many time do you want to change your ip [type=1000]for infinte ip change type [0] >>")
#subprocess.Popen("tor")
#time.sleep(3)
if int(lin) ==int(0):

     while True:
         try:
             time.sleep(int(x))
             change()
         except KeyboardInterrupt:
             print('\nauto tor is closed ')
             quit()

else:
    for i in range(int(lin)):
        time.sleep(int(x))
        change()
