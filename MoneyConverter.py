import requests

def get_exchange_rates(base='USD'):
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get('result') == 'success':
            return data.get('rates')
        else:
            print(f"Failed to retrieve data: {data.get('error-type', 'Unknown error')}")
    else:
        print(f"Connection error: {response.status_code}")
    return None

def main():
    print("Welcome to the Real-Time Currency Converter!")
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    
    rates = get_exchange_rates(base_currency)
    if rates is None:
        print("Sorry, couldn't fetch the exchange rates at the moment.")
        return

    print("Available currencies:", ', '.join(rates.keys()))

    try:
        amount = float(input(f"Enter the amount in {base_currency}: "))
        target_currency = input("Convert to currency (e.g., EUR): ").upper()

        if target_currency not in rates:
            print("Sorry, that currency is not available.")
            return

        converted_amount = amount * rates[target_currency]
        print(f"{amount:.2f} {base_currency} is approximately {converted_amount:.2f} {target_currency}")

    except ValueError:
        print("Please enter a valid number for the amount.")

if __name__ == "__main__":
    main()
