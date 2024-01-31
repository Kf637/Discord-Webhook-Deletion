# Discord Webhook Deletion Script

This is a simple Python script that allows you to delete any Discord webhook by providing its URL. It uses the Requests library to send a HTTP DELETE request to the webhook URL and checks the response status code to determine whether the deletion was successful or not. The script also provides information about the deleted webhook, including its name, guild ID, channel ID, and ID.

## Requirements

- Python 3.x
- Requests library (can be installed via pip)

## Usage

1. Run the script by typing `python delete_webhook.py` in the command line.
2. Enter the URL of the webhook you want to delete when prompted.
3. The script will attempt to delete the webhook and print a success or error message, as well as information about the deleted webhook if it was successfully deleted.

Note: The script will ask you to enter the webhook URL again if it is not a valid Discord webhook URL.

## Information Provided

The script will print the following information about the webhook:

- Webhook Name
- Token
- Guild ID
- Channel ID
- Webhook ID
- Application ID
- Avatar
- Webhook Type


## Limitations

- The script can only delete Discord webhooks. It will not work with other types of webhooks.

## How does it work?

- This script works by interacting with the Discord API. It uses the provided Webhook ID and Token to authenticate and identify the webhook to be deleted. Once identified, it sends a DELETE request to the Discord API to remove the webhook. Importantly, this script can be used by anyone as it does not require a Discord account token.


## License

This script is licensed under the MIT License. Feel free to use, modify and distribute it as you see fit.
