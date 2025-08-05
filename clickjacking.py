import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init

init(autoreset=True)

vulnerable = []
secure = []
errors = []

# Skull ASCII art
skull = r"""
                               _,.-------.,_
                            ,;~'             '~;,
                          ,;                     ;,
                         ;                         ;
                        ,'                         ',
                       ,;                           ;,
                       ; ;      .           .      ; ;
                       | ;   ______       ______   ; |
                       |  `/~"     ~" . "~     "~\'  |
                       |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                         |   |        }:{        |   |
                         |   l       / | \       !   |
                         .~  (__,.--" .^. "--.,__)  ~.
                         |     ---;' / | \ `;---     |
                          \__.       \/^\/       .__/
                           V| \                 / |V
       __                  | |T~\___!___!___/~T| |                  _____
    .-~  ~"-.              | |`IIII_I_I_I_IIII'| |               .-~     "-.
   /         \             |  \,III I I I III,/  |              /           Y
  Y          ;              \   `~~~~~~~~~~'    /               i           |
  `.   _     `._              \   .       .   /               __)         .'
    )=~         `-.._           \.    ^    ./           _..-'~         ~"<_
 .-~                 ~`-.._       ^~~~^~~~^       _..-'~                   ~.
/                          ~`-.._           _..-'~                           Y
{        .~"-._                  ~`-.._ .-'~                  _..-~;         ;
 `._   _,'     ~`-.._                  ~`-.._           _..-'~     `._    _.-
    ~~"              ~`-.._                  ~`-.._ .-'~              ~~"~
  .----.            _..-'  ~`-.._                  ~`-.._          .-~~~~-.
 /      `.    _..-'~             ~`-.._                  ~`-.._   (        ".
Y        `=--~                  _..-'  ~`-.._                  ~`-'         |
|                         _..-'~             ~`-.._                         ;
`._                 _..-'~                         ~`-.._            -._ _.'
   "-.="      _..-'~                                     ~`-.._        ~`.
    /        `.                                                ;          Y
   Y           Y       Click-Jack Vurnablity Check            Y           |
   |           ;                                              `.          /
   `.       _.'                                                 "-.____.-'
     ~-----"
"""

colors = [Fore.RED, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

def blinking_skull():
    for _ in range(4):  # blink 4 times
        for color in colors:
            os.system('clear' if os.name != 'nt' else 'cls')
            print(color + skull + Fore.YELLOW + "\n           Author: Nithin Palegar")
            time.sleep(0.2)
            os.system('clear' if os.name != 'nt' else 'cls')
            time.sleep(0.1)

def check_clickjacking(domain):
    try:
        url = domain if domain.startswith("http") else f"http://{domain}"
        response = requests.get(url, timeout=5)
        headers = response.headers

        xfo = headers.get("X-Frame-Options", "").lower()
        csp = headers.get("Content-Security-Policy", "").lower()

        if "deny" in xfo or "sameorigin" in xfo or "frame-ancestors" in csp:
            return domain, False
        else:
            return domain, True

    except requests.exceptions.RequestException:
        return domain, "Site is not alive"

def main():
    blinking_skull()
    print(Fore.CYAN + "=== Clickjacking Vulnerability Checker (Threaded) ===" + Style.RESET_ALL)
    user_input = input(Fore.YELLOW + "Enter a domain or path to file with domains: " + Style.RESET_ALL).strip()

    if user_input.endswith(".txt"):
        with open(user_input, "r") as f:
            domains = [line.strip() for line in f if line.strip()]
    else:
        domains = [user_input]

    total = len(domains)
    print(f"\n{Fore.YELLOW}[+] Total domains to check: {total}\n")

    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_domain = {executor.submit(check_clickjacking, domain): domain for domain in domains}
        for i, future in enumerate(as_completed(future_to_domain), 1):
            domain = future_to_domain[future]
            try:
                result = future.result()
                if isinstance(result[1], str):
                    print(f"[{i}/{total}] {domain} - {Fore.RED}ERROR: {result[1]}")
                    errors.append(domain)
                elif result[1]:
                    print(f"[{i}/{total}] {domain} - {Fore.RED}[VULNERABLE]")
                    vulnerable.append(domain)
                else:
                    print(f"[{i}/{total}] {domain} - {Fore.GREEN}[NOT VULNERABLE]")
                    secure.append(domain)
            except Exception as e:
                print(f"[{i}/{total}] {domain} - {Fore.RED}EXCEPTION: {str(e)}")
                errors.append(domain)

    with open("vulnerable_domains.txt", "w") as vf:
        vf.write("\n".join(vulnerable))

    print(Fore.CYAN + "\n=== Scan Complete ===")
    print(f"{Fore.YELLOW}Total domains tested   : {total}")
    print(f"{Fore.RED}Vulnerable domains     : {len(vulnerable)}")
    print(f"{Fore.GREEN}Not vulnerable domains : {len(secure)}")
    print(f"{Fore.MAGENTA}Errors during scan     : {len(errors)}")
    print(f"{Fore.CYAN}Vulnerable domains saved to: vulnerable_domains.txt")

if __name__ == "__main__":
    main()
