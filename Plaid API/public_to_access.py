public_token = "public-sandbox-51891201-be9f-4bc3-99e6-d1bea7d6b392"  # Replace this with the actual public token
exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
exchange_response = client.item_public_token_exchange(exchange_request)
access_token = exchange_response.access_token
print(f"Access Token: {access_token}")
