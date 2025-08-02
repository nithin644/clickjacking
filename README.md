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

## 🖥️ Demo

```bash
$ python3 clickjack_scan.py

[SKULL BANNER BLINKS IN COLOR]

=== Clickjacking Vulnerability Checker (Threaded) ===
Enter a domain or path to file with domains: domains.txt

[1/10] example.com - [NOT VULNERABLE]
[2/10] target.io   - [VULNERABLE]
...

=== Scan Complete ===
Total domains tested   : 10
Vulnerable domains     : 3
Not vulnerable domains : 7
Vulnerable domains saved to: vulnerable_domains.txt
