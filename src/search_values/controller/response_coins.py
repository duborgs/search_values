import requests
from src import utils
from src.search_values.core import settings

coins = 'USD-BRL,JPY-BRL,EUR-BRL'

def response_coins():
    r = requests.get(f'{settings.URL_COIN}/{coins}')
    response = r.json()

    data = utils.format_coin(response)
    return utils.format_response(data)
