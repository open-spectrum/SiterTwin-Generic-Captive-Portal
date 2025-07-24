from utils.colors import *
from subprocess import run
from config import config

def header(hostapd:bool = False,dnsmasq:bool =False,flask_serve:bool=False):
   hostapd_status = f"{LIGHT_RED}[Off]{END}"
   dnsmasq_status = f"{LIGHT_RED}[Off]{END}"
   flask_serve_status = f"{LIGHT_RED}[Off]{END}"
   captive_portal = f"{LIGHT_CYAN}{config.get_captive_portal_current()} {END}" 
   if hostapd : hostapd_status = f"{LIGHT_GREEN}[Ok]{END}"
   if dnsmasq: dnsmasq_status = f"{LIGHT_GREEN}[Ok]{END}"
   if flask_serve:flask_serve_status = f"{LIGHT_GREEN}[Ok]{END}"
      
   print(f"""{PURPLE}
 █▀ █▄█ █▀ ▀█▀ █▀▀ █▀█   ▀█▀ █░█░█ █ █▄░█
 ▄█ ░█░ ▄█ ░█░ ██▄ █▀▄   ░█░ ▀▄▀▄▀ █ █░▀█
{END}
 {LIGHT_CYAN}𓂃 ִֶָ⋆🌷͙⋆ ִֶָ·𓂃 ִֶָ v1 by @open-spectrum 𓂃˖·ִֶָ🌷͙⋆ ִֶָ·˳ ִֶָ{END}
  Services:
  🧩 HOSTAPD         {hostapd_status}
  🧩 DNSMASQ         {dnsmasq_status} 
  🧩 FLASK           {flask_serve_status}
  🧩 CAPTIVE PORTAL: {captive_portal}
  +++++++++++++++++++++++++++++++++++++++++++++++++++
    """)
def menu():
   print("""
  ✨ Ｍｅｎｕ
  1° Start
  2° Config Ap
  3° Start Captive Portal
  4° Config Captive Portal
  5° Stop 
  9° Exit       
""")
   
def menu_captive():
   dirs = config.get_all_captive_portal()
   print("Choose Captive Portal")
   for i,item in enumerate(dirs):
      print(f"{i}° {item}")

