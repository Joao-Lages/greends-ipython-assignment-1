import sys
import requests

api_key = 'd54c932c902b0073424e3c5549d7251abc1f4a193dd4f13878f58feabc45af60'

arguments = sys.argv

if len(arguments) < 2:
    sys.exit("Missing command-line argument")

try:
    headers = {'Authorization': f'Bearer {api_key}'}

    amount = float(arguments[1])
    try:
        r = requests.get('https://api.coincap.io/v3/assets/bitcoin', headers=headers)
        data = r.json()
        price_bitcoin = float(data["data"]["priceUsd"])
        total = amount * price_bitcoin
        print(f"${total:,.4f}")

    except requests.RequestException:
        sys.exit("Error fecthing Bitcoin price")

except ValueError:
    sys.exit("Command-line argument is not a number")

