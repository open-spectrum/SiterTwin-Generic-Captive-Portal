from subprocess import run

def setAp(password:bool = False,name_wifi:str="free",passw:str="12345678"):
    config = ""
    if password:
      config =  f"""interface=wlo1
        driver=nl80211
        ssid={name_wifi}
        hw_mode=g
        channel=1
        macaddr_acl=0
        auth_algs=1
        ignore_broadcast_ssid=0
        wpa=2
        wpa_passphrase={passw}
        wpa_key_mgmt=WPA-PSK
        wpa_pairwise=TKIP
        rsn_pairwise=CCMP""".replace(" ","")
    else:
       config = f"""interface=wlo1
        driver=nl80211
        ssid={name_wifi}
        hw_mode=g
        channel=1
        macaddr_acl=0
        auth_algs=1
        ignore_broadcast_ssid=0
       """.replace(" ","")


    with open("./config/hostapd.conf","w") as file:
        file.write(config)
        
def set_captive_portal(new_captive_portal):

  new_config = ""
  with open("./config/global_config.txt","r") as file:
     contents = file.read().split("\n")
     for content in contents:
      
        if "captive_portal_current:" in content:
           new_config+="captive_portal_current:"+new_captive_portal+"\n"
        else:
            new_config+=content
     

     with open("./config/global_config.txt","w") as fileWrite:
        fileWrite.write(new_config)

def get_captive_portal_current():
 
  with open("./config/global_config.txt","r") as file:
     contents = file.read().split("\n")
     for content in contents:
      
        if "captive_portal_current:" in content:
          return content[content.find(":")+1:]

def get_all_captive_portal():
   dirs = run(['ls','./templates/site_static'],capture_output=True,text=True).stdout.split("\n")
   dirs.pop()
   return dirs
