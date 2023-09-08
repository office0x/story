import requests
import time
import json
from fake_useragent import UserAgent
import random

# sleep in seconds
sleep_from = 1
sleep_to = 2

# Function to send POST request with email as data
def send_post_request(email):
    # Initialize UserAgent object to generate random User-Agent strings
    ua = UserAgent()

    # Define the URL for the POST request
    url = 'https://www.storyprotocol.xyz/api/subscribe'

    # Define the headers for the POST request
    headers = {
        'authority': 'www.storyprotocol.xyz',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.storyprotocol.xyz',
        'referer': 'https://www.storyprotocol.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': ua.random  # Use a random User-Agent
    }

    data = {

        'email': email,
        'tags': ['general', 'creative']
    }

    proxies = {}  # Initialize an empty proxy dictionary

    try:
        response = requests.post(url, headers=headers, json=data, proxies=proxies, timeout=10)
        response_data = response.json()
        if response.status_code == 200 and response_data.get('status') == 'success':
            print(f"Email: {email}, Status Code: {response.status_code}")
            print('Success')
        else:
            print(f"Email: {email}, Status Code: {response.status_code}, Response: {response_data}")
    except Exception as e:
        print(f"Error sending request for {email}: {str(e)}")

if __name__ == "__main__":
    # Read emails from emails.txt and send POST requests
    with open('emails.txt', 'r') as email_file:
        email_list = email_file.readlines()
        for email in email_list:
            email = email.strip()  # Remove leading/trailing whitespaces
            try:
                send_post_request(email)
            except Exception as e:
                print(f"Error in processing email: {email}")
                print(f"Exception: {str(e)}")

            # Sleep for 100 seconds between requests
            time.sleep(random.randint(sleep_from, sleep_to))
