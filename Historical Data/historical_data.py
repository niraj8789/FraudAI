import requests
import json

# FraudLabs Pro API key (replace with your own key)
API_KEY = "7SQT0NNBRLH9JHGE6GHE9D3WB7KQJDJE"

# Endpoint URL
URL = f"https://api.fraudlabspro.com/v1/transaction?key={API_KEY}"

# Fetching data
response = requests.get(URL)
if response.status_code == 200:
    fraud_data = response.json()
    print("Data fetched successfully!")
    # Save data locally
    with open('historical_fraud_data.json', 'w') as file:
        json.dump(fraud_data, file)
        print("Data saved to historical_fraud_data.json")
else:
    print("Failed to fetch historical data:", response.status_code)
