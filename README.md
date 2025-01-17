# Synett Token Checker

![Synett Token Checker](https://media.discordapp.net/attachments/1328850377864646767/1329788041539096626/WindowsTerminal_ikJwPWKA4l.png?ex=678b9d1f&is=678a4b9f&hm=7e4e38aa744180e2b5affd9dd13fec6bc6a6733854879afafcc758d20b31f1f8&)

## Introduction
**Synett Token Checker** is a powerful and efficient tool for analyzing Discord tokens with advanced features such as boost availability checks, verification statuses, flag detection, and more. Designed with a clean user interface, multi-threaded performance, and advanced TLS spoofing, it ensures maximum efficiency and stealth during token checks.

---

## Features

### 🔍 **Comprehensive Token Checks**
- **Boost Availability**: Detect how many boosts are available for each token.
- **Verification Status**:
  - Email Verified.
  - Phone Verified.
  - Not Verified.
- **Flags**: Identify if tokens are flagged, unlocked, or valid.
- **Subscription Details**: Check remaining subscription days.

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

### 🖥️ **Clean User Interface**
- Organized console displaying real-time updates and detailed statistics.

### 🛡️ **Safe and Undetectable**
- Ensures **0% token locks** after checks.
- No CAPTCHAs, token locks, or rate limits triggered.

### 🧪 **Advanced TLS Spoofing**
- Mimics legitimate traffic to avoid detection.
- No risk of tokens being flagged or locked.

---

3m-tokens.txt

2-boosts.txt

1-boost.txt

email-verified.txt

flagged.txt

And more...

⚙️ Easy Configuration
Proxyless operation for added simplicity.

Supports multi-threading for faster processing.

Clear input file structure for tokens.

🖥️ Clean User Interface
A clean and organized console that displays real-time updates and stats.

🛡️ Safe and Unflagged
Ensures 0% token lock after checks.

No CAPTCHA triggers, locked tokens, or rate limits.

🧪 Advanced TLS Spoofing
Mimics legitimate traffic to avoid detection.

No risk of tokens being flagged or locked.

Installation
Clone the repository:

git clone https://github.com/yourusername/synett-token-checker.git
Navigate to the directory:

cd synett-token-checker
Install dependencies:

pip install -r requirements.txt
Run the tool:

python main.py
Usage
Place your tokens in the input.txt file.

Configure settings in the config.json file (if applicable).

Run the tool using:

python main.py
Check the results in the automatically generated dated output folder.

Output Structure
The tool organizes results into a dated output folder with the following structure:

output/
  [YYYY-MM-DD] [HH-MM-SS]/
    invalid.txt
    locked.txt
    used.txt
    valid.txt
    1m-tokens.txt
    3m-tokens.txt
    2-boosts.txt
    1-boost.txt
    email-verified.txt
    flagged.txt
    ratelimited.txt
    ...
Disclaimer
This tool is intended for educational purposes only. The developer is not responsible for any misuse of this software.

License
This project is licensed under the MIT License.

Contribution
Feel free to submit issues or contribute by opening a pull request. We welcome all contributions to improve the tool further!
