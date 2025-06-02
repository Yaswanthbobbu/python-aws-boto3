import boto3
import requests


def get_converted_currency(amount, from_currency='USD', to_currency='INR'):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        rate = float(data['rates'].get(to_currency))
        if rate:
            converted_amount = amount * rate
            print(f"Total AWS Cost in rupees : ₹{converted_amount:.2f}")
            return None
        else:
            raise ValueError(f"Currency {to_currency} not found in the exchange rates.")
    except requests.RequestException as e:
        print(f"An error occurred while fetching exchange rates: {e}")
        return None


def get_billing_info(year, month):
    client = boto3.client('ce', region_name='us-east-1')

    start_date = f"{year}-{month:02d}-01"
    if month == 12:
        end_date = f"{year + 1}-01-01"
    else:
        end_date = f"{year}-{month + 1:02d}-01"

    try:
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date,
                'End': end_date
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost']
        )
        total_cost_usd = float(response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount'])

        print(f"Total AWS Cost in dollars: ${total_cost_usd:.2f}")
        get_converted_currency(float(total_cost_usd))

    except Exception as e:
        print(f"An error occurred: {e}")


get_billing_info(2025, 5)
