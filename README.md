# 🔍 Clickjacking Vulnerability Scanner

A fast, threaded, and colorful Clickjacking vulnerability scanner built for bug bounty hunters and web security researchers. This tool checks whether target domains are vulnerable to UI redressing (Clickjacking) by analyzing security response headers.

![Skull](https://github.com/user-attachments/assets/2208448f-b285-4c22-88a1-68a532e65f54) <!-- Optional: Replace with a hosted image of your ASCII art if desired -->

---

## 🎯 Features

- ✅ Supports **single domain** or **bulk list input**
- ✅ Detects missing or weak `X-Frame-Options` / `Content-Security-Policy` headers
- ✅ Uses **multithreading** for high-speed scanning
- ✅ **Colorized and blinking ASCII skull** intro (for style 😎)
- ✅ Saves vulnerable domains to `vulnerable_domains.txt`
- ✅ Built in pure Python (3.x)

---

## 🖥️ Installation

```bash
git clone https://github.com/nithin644/clickjacking.git

cd clickjacking

chmod +x clickjacking.py

pip3 install -r requirements.txt --break-system-packages

python3 clickjacking.py

