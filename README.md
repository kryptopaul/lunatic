
# Lunatic

A Python bot monitoring your current LUNA holdings and sending updates to your Discord server.



## Requirements

- A Discord Webhook.
- Preferably a remote server to run the bot on.
## Installation

Open the config.json file and fill in the Discord webhook, your LUNA balance (separated by a ".") and a refresh rate in seconds.

### Example:
```
    "discord_webhook": "https://discord.com/api/webhooks/x/x",
    "luna_balance": 217778.85,
    "refresh_rate": 60
```
Save the config and run the main.py file. The app will send updates to your Discord:

![](https://i.imgur.com/c2jjFAD.png)