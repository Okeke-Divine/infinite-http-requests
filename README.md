# Url Cloud

### Note

Phython script to send unlimited request to an API in an attempt to c****--- it. (NOTE: THIS IS FOR EDUCATION PURPOSES ONLY) (WARNING: IF YOU USE IT ON A LIVE SITE AND IT GET'S TAKEN DOWN, YOU'LL BE RESPONSIBLE FOR DAMAGES) {sys.die()}


### Brief documentation
- The main code is in bot.py
- List of user agents -> data/userAgents.json
- To add your target url set api_url = "https://url.com"
#### Payload
```
payload = {'email': email, 'password': password}
```
You can add more data in the dictionary

----------------------

Phthon normal sends on requests and wait for a response before intialising the next one but with
```
concurrent_requests = 100  # Number of concurrent requests
    with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
      ...
```
... you can send out 100 request instantly.

#### Delay
This code add a randomly of 1 - 5 seconds in each interval
```
delay = random.uniform(1, 5)
print("Waiting for " + str(delay) + " seconds after the batch")
time.sleep(delay)  # Random delay between 1 to 10 seconds
```
