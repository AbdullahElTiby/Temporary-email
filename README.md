# 📬 Temp Email Generator with Code Reader

This Python script allows you to **generate temporary email addresses** and automatically **receive and read messages** (such as verification codes) using the [mail.tm](https://mail.tm/) public API.

## ✅ Features

- Generates a random temporary email
- Registers the email on `mail.tm`
- Authenticates and retrieves access token
- Polls the inbox every 5 seconds for incoming messages
- Automatically prints the subject and content of the first message received

---

## 💻 Requirements

- Python 3.7+
- `requests` library

### Install dependencies:
```bash
pip install requests

## 🚀 How to Use

1. **Clone or download this repo**

2. **Run the script**:

   ```bash
   python temp_email.py
Copy the generated email and use it in any service that requires email verification.

The script will wait for a new email and print its contents once received.

🧠 Example Output
plaintext
Copy
Edit
Generated email: xlmzbdtjs@mail.tm
Waiting for email...
Subject: Your Verification Code
Body:
Here is your code: 948372
🛡️ Disclaimer
This tool is intended for educational and testing purposes only.

Do not use it for spam, illegal activity, or to bypass systems.

Some websites may block mail.tm or other temp email domains.

📚 Resources
mail.tm Public API Docs

Temp Mail API Alternatives


