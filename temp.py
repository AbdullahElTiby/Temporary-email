import requests
import random
import string
import time

def random_name(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

base_url = "https://api.mail.tm"

# Step 1: get domains
domains = requests.get(f"{base_url}/domains").json()
domain = domains['hydra:member'][0]['domain']

# Step 2: register temp account
email = f"{random_name()}@{domain}"
password = "Test1234!"
account = requests.post(f"{base_url}/accounts", json={"address": email, "password": password}).json()

print(f"Generated email: {email}")

# Step 3: get token
token_data = requests.post(f"{base_url}/token", json={"address": email, "password": password}).json()
token = token_data["token"]

# Step 4: poll inbox
headers = {"Authorization": f"Bearer {token}"}
print("Waiting for email...")
while True:
    messages = requests.get(f"{base_url}/messages", headers=headers).json()
    if messages['hydra:member']:
        msg = messages['hydra:member'][0]
        print("Subject:", msg['subject'])
        content = requests.get(f"{base_url}/messages/{msg['id']}", headers=headers).json()
        print("Body:\n", content['text'])
        break
    time.sleep(5)
