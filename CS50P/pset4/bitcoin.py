# Bitcoin Price - implement a program that:
# Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. 
# Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.

import json
import sys
import requests

if len(sys.argv) == 2:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = response.json()
        rate = response["bpi"]["USD"]["rate_float"]
        amount = rate * float(sys.argv[1])
        print(f"${amount:,.4f}")

    except requests.RequestException:
        sys.exit()

elif len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.exit("Missing command-line argument")

else:
    sys.exit("Command-line argument is not a number")
