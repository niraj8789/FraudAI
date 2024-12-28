import azure.functions as func
import requests
from datetime import datetime, timedelta
import json


end_date = datetime.now()
start_date = end_date - timedelta(days=30)  # Get last 30 days of transactions

start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Replace with your Plaid API endpoint and headers
        plaid_url = "https://sandbox.plaid.com/transactions/get"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "access-sandbox-f609aea2-0a1d-4eba-8bd6-8febc565b3d2"
        }
        body = {
            "client_id": "676e51d3491dca001bd2ee44",
            "secret": "61e9f1ebfc09db7ad40ffe8c618a5b",
            "access_token": "access-sandbox-f609aea2-0a1d-4eba-8bd6-8febc565b3d2",
            "start_date": start_date_str,
            "end_date": end_date_str
        }

        response = requests.post(plaid_url, headers=headers, json=body)
        response_data = response.json()

        # Return the data as a response
        return func.HttpResponse(
            json.dumps(response_data, indent=4),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            f"Error occurred: {str(e)}",
            status_code=500
        )
