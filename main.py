import os, json, random, base64, datetime, time
from colorama import Fore
from pathlib import Path
from math import *
import ctypes
import tls_client
import shutil
import requests
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import json as jsond

def cls():
    os.system('cls' if os.name =='nt' else 'clear')

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f"Token Checker | Synett.cc")
else:
    pass

def logo():
    logo = """
┏┓        
┗┓┓┏┏┓┏┓╋╋
┗┛┗┫┛┗┗ ┗┗
┛   
Synett.cc | Version 1.0 \n
    """
    console_width = shutil.get_terminal_size((80, 20)).columns

    lines = logo.strip().split("\n")
    centered_lines = [line.center(console_width) for line in lines]

    print(f"{Fore.RESET}\n".join(centered_lines) + f"{Fore.RESET}")


config = json.load(open("config.json", encoding="utf-8"))

    
default = {
    "threads": 10,
    "thread_wait_time": 1,
    "proxyless": False,
    "clear_output_files": True,
}

if not os.path.exists("config.json"):
    json_object = json.dumps(default, indent=4)
    with open("config.json", "w") as outfile:
        outfile.write(json_object)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
cls()

logo()

def timestamp():
    timestamp = f"{Fore.RESET}{Fore.LIGHTMAGENTA_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
    return timestamp

  
def sprint(message, type:bool):
    if type == True:
        print(f"{Fore.RESET}[{Fore.MAGENTA}{timestamp()}{Fore.RESET}][{Fore.CYAN}∆{Fore.RESET}]{message}{Fore.RESET}")
    if type == False:
        print(f"{Fore.RESET}[{Fore.MAGENTA}{timestamp()}{Fore.RESET}][{Fore.CYAN}∆{Fore.RESET}]{message}{Fore.RESET}")
        
def checkEmpty(filename):
    mypath = Path(filename)
 
    if mypath.stat().st_size == 0:
        return True
    else:
        return False
    
def process_tokens_in_threads(tokens, output_dir):
    num_threads = config.get("threads", 10)
    thread_wait_time = config.get("thread_wait_time", 1)

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(checktoken, token, getproxy(), output_dir): token for token in tokens}
        
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                sprint(f"Error processing token: {futures[future]} | Exception: {e}", False)
        time.sleep(thread_wait_time)
    
def create_output_directory():
    timestamp = datetime.datetime.now().strftime('[%Y-%m-%d] [%H-%M-%S]')
    output_dir = f"output/{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    for filename in [
        "invalid.txt",
        "locked.txt",
        "used.txt",
        "valid.txt",
        "unlocked.txt",
        "1m-tokens.txt",
        "3m-tokens.txt",
        "other.txt",
        "2-boosts.txt",
        "1-boosts.txt",
        "email-verified.txt",
        "fully-verified.txt",
        "flagged.txt",
        "ratelimited.txt",
        "not-subscribed.txt"
    ]:
        open(os.path.join(output_dir, filename), "w").close()

    return output_dir

 
def write(content: str, filename: str, output_dir: str):
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "a") as f:
        f.write(f"{content}\n")
    
    
def get_all_tokens(filename:str):
    all_tokens = []
    for j in open(filename, "r").read().splitlines():
        if ":" in j:
            j = j.split(":")[2]
            all_tokens.append(j)
        else:
            all_tokens.append(j)
 
    return all_tokens


def getproxy():
    if config.get('proxyless', False):
        return None
    try:
        proxies = [line.strip() for line in open("input/proxies.txt", "r").readlines() if line.strip()]
        if proxies:
            raw_proxy = random.choice(proxies)
            if "@" in raw_proxy:
                creds, ip_port = raw_proxy.split("@")
                username, password = creds.split(":")
                proxy = {
                    'http': f'http://{username}:{password}@{ip_port}',
                    'https': f'http://{username}:{password}@{ip_port}',
                }
            else:
                proxy = {
                    'http': f'http://{raw_proxy}',
                    'https': f'http://{raw_proxy}',
                }
            return proxy
    except FileNotFoundError:
        print("Proxy file not found. Proceeding without proxies.")
    return None

def validate_proxy(proxy):
    try:
        response = requests.get("https://httpbin.org/ip", proxies=proxy, timeout=5)
        return response.status_code == 200
    except Exception:
        return False

class data:
    other = 0; valid = 0; valid_lst = []; one_month_tokens = 0; invalid = 0; used = 0; locked = 0; no_nitro = 0; three_month_tokens = 0; checked = 0; sorted = 0
     
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
]
  
def get_headers(token):
    super_properties = '''{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-GB","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36","browser_version":"112.0.5615.49","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":102113,"client_event_source":null}'''
    super_properties = base64.b64encode(super_properties.encode()).decode()

    headers = {
            'Authorization': token,
            'User-Agent': random.choice(user_agents),
            'Content-Type': 'application/json',
            'Connection': 'keep-alive'
        }

    return headers

def validate_token(client, token):
    try:
        headers = get_headers(token)
        response = client.get("https://discord.com/api/v9/users/@me", headers=headers)
        if response.status_code == 200:
            profile = response.json()
            return f"{profile['username']}#{profile['discriminator']}"
        else:
            return None
    except Exception as e:
        return None
    
def get_full_token(token: str) -> str:
    with open("input/tokens.txt", "r") as f:
        for line in f:
            if token in line:
                return line.strip()
    return token

def checktoken(token, proxy=None, output_dir=None):
    try:
        full_token = get_full_token(token)

        client = tls_client.Session(
            client_identifier="chrome_112",
            random_tls_extension_order=True
        )
        if proxy:
            client.proxies.update(proxy)

        headers = get_headers(token)

        response = client.get("https://discord.com/api/v9/users/@me", headers=headers)
        if response.status_code != 200:
            sprint(f"{Fore.RESET}[{Fore.CYAN}Token: {Fore.MAGENTA}{token[:39]}{Fore.MAGENTA}{Fore.RESET}]{Fore.RESET} {Fore.RESET}|{Fore.RESET} {Fore.CYAN}Flags{Fore.CYAN}: {Fore.RESET}[{Fore.RESET}{Fore.MAGENTA}INVALID{Fore.MAGENTA}{Fore.RESET}]{Fore.RESET}", False)
            data.invalid += 1
            data.checked += 1
            write(full_token, "invalid.txt", output_dir)
            return False

        user_data = response.json()
        email_verified = user_data.get('verified', False)
        phone = user_data.get('phone')
        mfa_enabled = user_data.get('mfa_enabled', False)

        boost_response = client.get("https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        flagged = "Flagged" if boost_response.status_code == 403 else "Unflagged"

        boost_count = 0
        if boost_response.status_code in [200, 201]:
            boosts = boost_response.json()
            boost_count = len(boosts)

        subscription_response = client.get("https://discord.com/api/v9/users/@me/billing/subscriptions", headers=headers)
        days_left = "N/A"
        if subscription_response.status_code in [200, 201]:
            subscriptions = subscription_response.json()
            if subscriptions:
                sub_end = subscriptions[0].get('current_period_end')
                if sub_end:
                    end_date = datetime.datetime.strptime(sub_end, '%Y-%m-%dT%H:%M:%S.%f%z')
                    now = datetime.datetime.now(datetime.timezone.utc)
                    days_left = (end_date - now).days

                if days_left <= 30:
                    write(full_token, "1m-tokens.txt", output_dir)
                elif days_left <= 90:
                    write(full_token, "3m-tokens.txt", output_dir)
                else:
                    write(full_token, "other.txt", output_dir)

        verification_status = "Fully Verified" if email_verified and phone else "Email Verified" if email_verified else "Not Verified"
        unlock_status = "Unlocked" if not mfa_enabled else "Locked"

        sprint(
            f" {Fore.RESET}[{Fore.CYAN}Token: {Fore.MAGENTA}{token[:39]}{Fore.MAGENTA}{Fore.RESET}] | {Fore.RESET}{Fore.CYAN}Flags: {Fore.MAGENTA}{Fore.RESET}[{Fore.RESET}{Fore.CYAN}Boost Available: {Fore.CYAN}{Fore.MAGENTA}{boost_count}{Fore.MAGENTA}{Fore.RESET}]{Fore.RESET},{Fore.RESET}[{Fore.RESET}{Fore.CYAN}Days Left: {Fore.CYAN}{Fore.MAGENTA}{days_left}{Fore.MAGENTA}{Fore.RESET}]{Fore.RESET},{Fore.RESET}[{Fore.RESET}{Fore.MAGENTA}{flagged}{Fore.MAGENTA}{Fore.RESET}]{Fore.RESET},{Fore.RESET}[{Fore.RESET}{Fore.MAGENTA}{verification_status}{Fore.MAGENTA}{Fore.RESET}]{Fore.RESET},{Fore.RESET}[{Fore.RESET}{Fore.MAGENTA}{unlock_status}{Fore.MAGENTA}{Fore.RESET}]{Fore.RESET}",
            True
        )

        if flagged == "Flagged":
            data.locked += 1
            write(full_token, "flagged.txt", output_dir)
        elif days_left != "N/A":
            data.valid += 1
            data.valid_lst.append(token)
            if boost_count == 2:
                write(full_token, "2-boosts.txt", output_dir)
            elif boost_count == 1:
                write(full_token, "1-boosts.txt", output_dir)
            write(full_token, "valid.txt", output_dir)
        else:
            data.no_nitro += 1
            write(full_token, "not-subscribed.txt", output_dir)

        if email_verified and phone:
            write(full_token, "fully-verified.txt", output_dir)
        elif email_verified:
            write(full_token, "email-verified.txt", output_dir)

        data.checked += 1
        return True

    except Exception as e:
        sprint(f"[Error checking token: {token[:39]} | Exception: {e}]", False)
        write(full_token, "ratelimited.txt", output_dir)
        return False
            
def clearfile(filename):
    try:
        open(filename, "w").write("")
    except Exception as e:
        pass
    
def clear_input_tokens_file():

    if config.get("clear_input_tokens", False):
        with open("input/tokens.txt", "w") as f:
            f.truncate(0)
        sprint(f" Cleared Tokens File.{Fore.RESET}", True)

def removeDuplicates(filename:str):
    all_tokens = open(filename, "r").read().splitlines()
    without_duplicates = []
    for i in all_tokens:
        if i not in without_duplicates:
            without_duplicates.append(i)
    open(filename, "w").write("")
    for line in without_duplicates:
        open(filename, "a").write(f"{line}\n")
    return len(without_duplicates)
        
if __name__ == "__main__":
    output_dir = create_output_directory()
    tokens = get_all_tokens("input/tokens.txt")

    if not tokens:
        sprint(f"{Fore.RED}No tokens found in input/tokens.txt. Exiting...{Fore.RESET}", False)
        quit()

    process_tokens_in_threads(tokens, output_dir)

    sprint(f"{Fore.CYAN} Checked: {data.checked} tokens.{Fore.RESET}", True)

    clear_input_tokens_file()
    sprint(
        f" Valid Tokens: {data.valid} | Used: {data.used} | Unlocked: {data.no_nitro} | Locked: {data.locked} | Invalid: {data.invalid}",
        True
    )
    input("Press Enter to exit...")
    quit()
    quit()
