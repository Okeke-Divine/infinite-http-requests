import requests

def send_requests(url, num_requests):
    for i in range(1, num_requests + 1):
        response = requests.get(url)
        print(f"{i}: {response}")


if __name__ == "__main__":
    url = "https://faucetearner.org/api.php?act=login"
    url = "http://locahost:8000"
    x = 10
    send_requests(url, x)
