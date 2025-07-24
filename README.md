# Sister-Twin

**Sister-Twin** is a generic captive portal built with Python and Flask. It uses `hostapd` to create an access point, `dnsmasq` to handle DHCP and DNS spoofing, and Flask to serve a custom login or redirection page. Ideal for ethical testing, IoT networks, and educational labs.

---

## ✨ Features

- Lightweight and modular captive portal
- Compatible with most systems (Android, iOS, Linux, Windows)
- Automatically intercepts and redirects clients after connection
- Easily customizable HTML/CSS interface

---

## ⚙️ Dependencies

Install the following packages on Ubuntu:

```bash
sudo apt update
sudo apt install dnsmasq hostapd python3 python3-venv
