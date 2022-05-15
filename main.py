import requests
import json
import time

def main():
  while True:
    #Fetches the LUNA price from Coingecko
    r_luna = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=terra-luna&vs_currencies=usd', headers={'accept': 'application/json'})
    luna_price = float(r_luna.json()['terra-luna']['usd'])
    
    #Loads the configuration
    config = json.load(open('config.json'))
    luna_balance = config['luna_balance']
    discord_webhook = config['discord_webhook']
    refresh_rate = config['refresh_rate']
    
    #Message for Discord
    message = {
      "content": None,
      "embeds": [
        {
          "title": "LUNA Prices",
          "description": f"Current LUNA price: {luna_price} USD",
          "color": 4897036,
          "fields": [
            {
              "name": "Your LUNA holdings",
              "value": f"You own {luna_balance} LUNA worth {round(luna_price * luna_balance, 2)} USD"
            }
          ],
          "thumbnail": {
            "url": "https://cryptologos.cc/logos/terra-luna-luna-logo.png"
          },
        }
      ],
      "attachments": []
    }

    #Send the request and wait <refresh_rate> seconds 
    requests.post(discord_webhook, json=message)
    time.sleep(refresh_rate)

if __name__ == "__main__":
  main()