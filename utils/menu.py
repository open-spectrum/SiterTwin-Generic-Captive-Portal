from utils.colors import *
from subprocess import run
from config import config

def header(interface):
   
  captive_portal = f"{LIGHT_CYAN}{config.get_captive_portal_current()} {END}" 
  ap_name = f"{LIGHT_GREEN}[{config.get_ap_name()}]{END}"
  ap_password = f"{LIGHT_GREEN}[{config.get_ap_password()}]{END}"
  interface = f"{LIGHT_GREEN}[{interface}]{END}"
      
  print(f"""{PURPLE}
 █▀ █▄█ █▀ ▀█▀ █▀▀ █▀█   ▀█▀ █░█░█ █ █▄░█
 ▄█ ░█░ ▄█ ░█░ ██▄ █▀▄   ░█░ ▀▄▀▄▀ █ █░▀█
{END}
 {LIGHT_CYAN}𓂃 ִֶָ⋆🌷͙⋆ ִֶָ·𓂃 ִֶָ v1.01 by @open-spectrum 𓂃˖·ִֶָ🌷͙⋆ ִֶָ·˳ ִֶָ{END}
  Ap Info:
  🧩 WIFI NAME:         {ap_name}
  🧩 PASSWORD:          {ap_password} 
  🧩 INTERFACE:         {interface}
  🧩 CAPTIVE PORTAL:    {captive_portal}
  +++++++++++++++++++++++++++++++++++++++++++++++++++
    """)
def menu():
   print("""
  ✨ Ｍｅｎｕ
  0° Start All       
  1° Start Ap
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

