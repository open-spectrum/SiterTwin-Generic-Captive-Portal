from utils.menu import menu,header,menu_captive
from utils.colors import *
from subprocess import run, Popen, DEVNULL
import sys
from subprocess import Popen
from config import config
interface = "wlo1"


def start_captive_portal():
    header(True,True,True)
    print(f"{LIGHT_BLUE}Flask Logs{END}")
    run(['venv/bin/python', 'app.py'])




def start(interface):
    print(f"[*]{LIGHT_PURPLE}[Info]{END} {LIGHT_CYAN}Matando serviços conflitantes...{END}")
    run(['sudo', 'airmon-ng', 'check', 'kill'], stdout=DEVNULL, stderr=DEVNULL)

    print(f"[*]{LIGHT_PURPLE}[Info]{END} {LIGHT_CYAN}Parando systemd-resolved...{END}")
    run(['sudo', 'systemctl', 'stop', 'systemd-resolved'])

    print(f"[*]{LIGHT_PURPLE}[Info]{END} {LIGHT_CYAN}Configurando interface {interface}...{END}")
    run(['sudo', 'ip', 'link', 'set', interface, 'up'])
    run(['sudo', 'ip', 'addr', 'add', '192.168.0.1/24', 'dev', interface])

    print(f"[*]{LIGHT_PURPLE}[Info]{END} {LIGHT_CYAN}Iniciando DNSMASQ...{END}")
    run(['sudo', 'dnsmasq', '-C', './config/dns.conf'], stdout=DEVNULL, stderr=DEVNULL)

    print(f"[*]{LIGHT_PURPLE}[Info]{END} {LIGHT_CYAN}Iniciando HostAPD...{END}")
    Popen(['sudo', 'hostapd', './config/hostapd.conf'], stdout=DEVNULL, stderr=DEVNULL)

  

    print(f"{LIGHT_GREEN}[*] Todos os serviços iniciados com sucesso.{END}")
    sys.exit()
    

   
def stop():
   run(['sudo', 'killall', 'dnsmasq'])
   run (['sudo', 'killall', 'hostapd'])

   run (['sudo', 'systemctl' ,'start', 'systemd-resolved'])
   run (['sudo', 'systemctl' ,'start', 'NetworkManager'])




while True:
    run(['clear'])
    header()
    menu()
    option = str(input("Choose Option: "))
    if option == "1":
        start(interface)
       
    elif option == "2":
        ssid = str(input("SSID: "))

        password = str(input("passwd: "))
        if len(password) > 5:
            config.setAp(name_wifi=ssid,passw=password,password=True)
        else:
            config.setAp(name_wifi=ssid,passw=password,password=False)
            print("open wifi")
    elif option == "3":
        start_captive_portal()

    elif option == "4":
        menu_captive()
        opt = int(input("Choose: "))
        config.set_captive_portal(config.get_all_captive_portal()[opt])
    elif option == "5":
        stop()
    elif option == "9":
       break




