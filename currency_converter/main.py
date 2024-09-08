import json
import requests

def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)


def convert(amount: float, base: str, target: str, rates: dict[str, dict]) -> float:
    base = base.lower()
    target = target.lower()

    from_rates = rates.get(base)
    to_rates = rates.get(target)

    if from_rates is not None and to_rates is not None:
        if base == 'eur':
            return amount * to_rates.get('rate')
        else:
            return amount * (to_rates['rate'] / from_rates['rate'])
    else:
        print(f'Error: Invalid currency code for {base} or {target}.')


def convert_api(amount: float, base: str, target: str) -> float:
    base = base.lower()
    target = target.lower()
    apiKey = #TBD
    query = f'{base}_{target}'
    url = f'https://free.currconv.com/api/v7/convert?q={query}&compact=ultra&apiKey={apiKey}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        conversion_rate = data.get(query)

        if conversion_rate:
            return amount * conversion_rate
        else:
            print(f'Error: Conversion rate for {base.upper()} to {target.upper()} not found.')
            return None
    else:
        print(f'Error: Failed to fetch data from API. Status code: {response.status_code}')
        return None


def main() -> None:
    rates = load_rates('./rates.json')
    amount = float(input('Amount to be converted: '))
    base = input('Base currency (3-letter code): ')
    target = input('Target currency (3-letter code): ')
    source = input('Use json file or api? (json/api) ')
    
    if source == 'json':
        conversion = convert(amount=amount, base=base, target=target, rates=rates)
    elif source == 'api':
        conversion = convert_api(amount=amount, base=base, target=target)
    else:
        print('Please try again with a valid source')
        return None
    
    if conversion is not None:
        print(f'{base.upper()} {amount:,.2f} = {target.upper()} {conversion:,.2f}')
    else:
        print('Conversion failed.')

if __name__ == "__main__":
    main()
