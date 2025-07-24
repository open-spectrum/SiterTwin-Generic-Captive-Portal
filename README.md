# Sister-Twin

**Sister-Twin** is a generic captive portal built with Python and Flask. It uses `hostapd` to create an access point, `dnsmasq` to handle DHCP and DNS spoofing, and Flask to serve a custom login or redirection page. Ideal for ethical testing, IoT networks, and educational labs.

---

## ✨ Features

- Lightweight and modular captive portal
- Compatible with most systems (Android, iOS, Linux, Windows)
- Automatically intercepts and redirects clients after connection
- Easily customizable HTML/CSS interface

---
<img src= "./imgs/f0.png">
<img src ="./imgs/f1.png">
<img src= "./imgs/f2.png">
<img src ="./imgs/f3.png">
## ⚙️ Dependencies

Install the following packages on Ubuntu:

```bash
sudo apt update
sudo apt install dnsmasq hostapd python3 python3-venv

```
in main define
interface = "your_interface"
```bash
git@github.com:open-spectrum/SiterTwin-Generic-Captive-Portal.git
cd SiterTwin-Generic-Captive-Portal
python3 -m venv venv
source venv/bin/activate
pip install flask
```
```bash
sudo python3 main.py
