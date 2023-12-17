from login import *


api_url = "https://apiconnect.angelbroking.com/rest/secure/angelbroking/order/v1/searchScrip"

def findTickToken(exchange,tick):

    # Request payload
    payload = {
        "exchange": exchange,
        "searchscrip": tick
    }

    # Request headers
    headers = {
        'Authorization': authToken,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-UserType': 'USER',
        'X-SourceID': 'WEB',
        'X-MACAddress': mac_address,
        'X-PrivateKey': api_key
    }

    # Make the API request
    response = requests.post(api_url, json=payload, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()['data'][0]
        symboltoken = data.get('symboltoken')
        return symboltoken
        
    else:
        print(f"Error: {response.status_code} - {response.text}")
        sys.exit(1)



