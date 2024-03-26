import requests
import json
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_post_request(url):
    email = generate_random_string(8) + "@faucetearner.org"
    password = generate_random_string(10)
    payload = {'email': email, 'password': password}
    print ("Sent: " + payload['email']);
    response = requests.post(url, json=payload)
    print("Response:", response.json())

if __name__ == "__main__":
    api_url = "https://faucetearner.org/api.php?act=login"
    x = 10
    for i in range(1, x + 1):
        send_post_request(api_url)
