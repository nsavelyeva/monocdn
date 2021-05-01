import os
import sys
import json
import urllib.request
from datetime import date


XRATES_FOLDER = os.environ.get('XRATES_FOLDER', 'x-rates')
if not os.path.isdir(XRATES_FOLDER):
    print(f'Exiting with code 1: the folder {XRATES_FOLDER} does not exist.')
    sys.exit(1)  # at least one error in getting currency exchange rates

API_KEY = os.environ.get('API_KEY', '')
if not API_KEY:
    print(f'Exiting with code 2: could not get X-Rates API Token.')
    sys.exit(2)  # at least one error in getting currency exchange rates

API_URL = f'https://free.currconv.com/api/v7/convert?compact=ultra&apiKey={API_KEY}'
XRATES = {
    'BYN': {'RUB': None, 'EUR': None, 'USD': None},
    'RUB': {'BYN': None, 'EUR': None, 'USD': None},
    'EUR': {'BYN': None, 'RUB': None, 'USD': None},
    'USD': {'BYN': None, 'RUB': None, 'EUR': None}
}

for currency_from in XRATES.keys():
    for currency_to in XRATES[currency_from].keys():
        url = API_URL + f'&q={currency_from}_{currency_to}'
        print(f'Accessing URL {url}')
        response = urllib.request.urlopen(url)
        body = response.read().decode()
        print(f'Response returned:\n{body}')
        try:
            XRATES[currency_from][currency_to] = float(json.loads(body).get(f'{currency_from}_{currency_to}'))
            print(XRATES)
        except (TypeError, ValueError, json.JSONDecodeError) as err:
            print(f'Exiting with code 3 due to {err}')
            sys.exit(3)  # at least one error in getting currency exchange rates


file_path = date.today().strftime('%Y/%m/%d')  # Linux!
XRATES = {'date': file_path, 'rates': XRATES}
with open(os.path.join(XRATES_FOLDER, file_path), 'w', encoding='utf-8') as xrates_file:
    json.dump(XRATES, xrates_file, ensure_ascii=False, indent=4)

sys.exit(0)
