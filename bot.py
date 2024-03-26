import requests
import json
import random
import string
from concurrent.futures import ThreadPoolExecutor

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_post_request(url):
    email = generate_random_string(8) + "@faucetearner.org"
    password = generate_random_string(10)
    payload = {'email': email, 'password': password}
    print ("Sent: " + payload['email'])
    try:
        response = requests.post(url, json=payload)
        print("Response:", response.json())
    except Exception as e:
        print("Error occurred:", e)
    print("==============================================================================")

if __name__ == "__main__":
    api_url = "https://faucetearner.org/api.php?act=login"
    concurrent_requests = 5  # Number of concurrent requests
    with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        while True:
            futures = []
            for _ in range(concurrent_requests):
                futures.append(executor.submit(send_post_request, api_url))
            for future in futures:
                future.result()  # Wait for response before proceeding to the next batch
