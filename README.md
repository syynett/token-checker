# Synett Token Checker

![Synett Token Checker](https://cdn.discordapp.com/attachments/1327322280308772957/1337477003829317654/WindowsTerminal_7UMHPri26v.png?ex=67ce7a46&is=67cd28c6&hm=9e99242a0c7881c419bfec193030d6fdf10c218300a26c8c3dffdd722d3fe1c0&)

## Introduction
**Synett Token Checker** is a powerful and efficient tool for advanced Discord tokens check with advanced features such as boost availability checks, verification status, flag detection, and more. Designed with a clean user interface, multi-threaded performance, and advanced TLS spoofing, it ensures maximum efficiency and stealth during token checks.

---

## Features

### 🔍 **Comprehensive Token Checks**
- **Boost Availability**: Detect how many boosts are available for each token.
- **Flags**: Identify if tokens are flagged, unlocked, or valid.
- **Subscription Details**: Check remaining subscription days.
- **Verification Status**:
  - Email Verified.
  - Phone Verified.
  - Not Verified.

### 📂 **Organized Output**
- Automatically organizes results into dated folders for better tracking.
- Output files include:
  - `1m-tokens.txt`
  - `3m-tokens.txt`
  - `2-boosts.txt`
  - `1-boost.txt`
  - `email-verified.txt`
  - `flagged.txt`
  - And more...

### ⚙️ **Easy Configuration**
- **Proxyless** operation for added simplicity.
- Supports **multi-threading** for faster processing.
- Clear input file structure for tokens.
- Threads Wait time
  
### 🖥️ **Clean User Interface**
- Organized console displaying real-time updates and detailed statistics.

### 🛡️ **Safe and Undetectable**
- Ensures **0% token locks** after checks.
- No CAPTCHAs, token locks, or rate limits triggered.
- Recommand to use proxies for more safety

### 🧪 **TLS Spoofing**
- Mimics legitimate traffic to avoid detection.
- No risk of tokens being flagged or locked.

### 📂 **Dated Output Folder:**

-All Checks are dated and oragnized in specific files and folder

```output/```
  - ```[YYYY-MM-DD] [HH-MM-SS]/```
    - ```invalid.txt```
    - ```locked.txt```
    - ```used.txt```
    - ```valid.txt```
    - ```1m-tokens.txt```
    - ```3m-tokens.txt```
    - ```2-boosts.txt```
    - ```1-boost.txt```
    - ```email-verified.txt```
    - ```flagged.txt```
    - ```ratelimited.txt```

--- 

### 🔥 **How to use**
- 1 Input your tokens in ```./input/tokens.txt``` with format: ```email:pass:token```
- 2 Fill your proxies in ```./input/proxies.txt``` if you dont have proxies then leave blank and set proxyless to ```true``` in config file
- 3 Run cmd and run ```pip install -r requirements.txt```
- 4 Now your all done just run ```python main.py``` in the cmd !

--- 

### ⚠️ **Disclaimer**
- This tool is not completely finished yet (can have error/bugs) so be comprehensive.
- **Stars Are Very Appreciated**

