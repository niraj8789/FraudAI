from plaid.api import plaid_api
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.exceptions import ApiException

# Initialize the configuration
configuration = Configuration(
    host="https://sandbox.plaid.com",
    api_key={
        "clientId": "676e51d3491dca001bd2ee44",
        "secret": "61e9f1ebfc09db7ad40ffe8c618a5b",
    }
)

# Create an API client
api_client = ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

# Exchange link token for public token (Simulated by Plaid Sandbox)
public_token = "public-sandbox-51891201-be9f-4bc3-99e6-d1bea7d6b392"

try:
    # Exchange public token for access token
    exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
    exchange_response = client.item_public_token_exchange(exchange_request)
    access_token = exchange_response.access_token
    print(f"Access Token: {access_token}")
except ApiException as e:
    print(f"Error during API call: {e}")
