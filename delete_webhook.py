import requests
import re
import os
import time

url_pattern = r'^https?://(?:www\.)?(?:discord\.com|discordapp\.com)/\S+$'

while True:
    url = input("Enter the URL of the webhook to delete: ")
    if not re.match(url_pattern, url):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Not a valid URL. Please enter a valid URL.")
        url = None
        continue

    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        webhook_info = response.json()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Failed to retrieve webhook with status code: ', response.status_code)
        print('Please try again.')
        url = None
        continue

    response = requests.delete(url)
    if response.status_code == requests.codes.not_found:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Webhook not found')
        url = None
    elif response.status_code == requests.codes.no_content:
        time.sleep(.4)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Webhook deleted successfully\n\nDeleted URL: {url}\nWebhook Name: {webhook_info["name"]}\nToken: {webhook_info["token"]}\nGuild ID: {webhook_info["guild_id"]}\nChannel ID: {webhook_info["channel_id"]}\nWebhook ID: {webhook_info["id"]}\nApplication ID: {webhook_info["application_id"]}\nAvatar: {webhook_info["avatar"]}\nWebhook Type: {webhook_info["type"]}\nApplication ID: {webhook_info["application_id"]}')
        url = None
        for x in range(3):
            print("")
    else:
        print('Failed to delete webhook with status code: ', response.status_code)
        print('Please try again.')
        url = None
