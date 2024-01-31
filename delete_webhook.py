import requests
import re
import os
from time import sleep
url_pattern = r'^https?://(?:www\.)?(?:discord\.com|discordapp\.com)/\S+$'
status_codes = {
    404: 'Webhook does not exist or could not be found.',
    400: 'Bad Request',
    401: 'Unauthorized',
    408: 'Request Timeout',
    429: 'URL Had Too Many Requests',
    500: 'Internal Server Error',
    502: 'Bad Gateway',
    503: 'Service Unavailable',
    504: 'Gateway Timeout',
    505: 'HTTP Version Not Supported',
    508: 'Loop Detected'
}

while True:
    url = input("Enter the URL of the webhook to delete: ")
    if not re.match(url_pattern, url):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Not a valid URL. Please enter a valid URL.")
        url = None
        continue

    print('Retrieving Webhook Info...')
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        webhook_info = response.json()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nWebhook Name: {webhook_info['name']}\nToken: {webhook_info['token']}\nGuild ID: {webhook_info['guild_id']}\nChannel ID: {webhook_info['channel_id']}\nWebhook ID: {webhook_info['id']}\nApplication ID: {webhook_info['application_id']}\nAvatar: {webhook_info['avatar']}\nWebhook Type: {webhook_info['type']}\nApplication ID: {webhook_info['application_id']}\n")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        message = status_codes.get(response.status_code, 'Unknown status code')
        print(f'Respond: {response.status_code} {message}\nPlease try again.\n')
        url = None
        continue

    confirmation = input("Are you sure you want to delete this webhook? (Y/N): ")
    if confirmation.lower() == "y" or confirmation.lower() == "yes":
        response = requests.delete(url)
        if response.status_code == requests.codes.no_content:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Webhook deleted successfully')
            url = None
            for x in range(3):
                print("")
        else:
            print('Failed to delete webhook with status code: ', response.status_code)
            print('Please try again.')
            url = None
        
    elif confirmation.lower() == "n":
        print('Action Canceled\nPlase Wait...')
        sleep(3)
        url = None
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        while confirmation.lower() not in ["y", "n"]:
            print('Invalid input')
            confirmation = input("Are you sure you want to delete this webhook? (Y/N): ")
        if confirmation.lower() == "y":
            response = requests.delete(url)
            if response.status_code == requests.codes.no_content:
                os.system('cls' if os.name == 'nt' else 'clear')

                url = None
                for x in range(2):
                    print("")
            else:
                print('Failed to delete webhook with status code: ', response.status_code)
                print('Please try again.')
                url = None
        else:
            url = None
