#converts given dollar value to bitcoin

#import libraries
import requests
import sys

#request api
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

#find float rate of bitcoin in api
try:
    object = response.json()
    btc = object["bpi"]["USD"]["rate_float"]
    
#multiply dollar value by bitcoin value
    dollar_btc = btc * float(sys.argv[1])
    print(f"${dollar_btc:,.4f}")

#when no command line argument given
except IndexError:
        print("Missing command line argument")

        sys.exit(1)
#when cmdln argument is invalid
except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)


