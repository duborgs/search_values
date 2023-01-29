from src.search_values.model.coins import Coins


def format_response(data):
    return {"data": data}

def format_coin(response):

    data = {}
    for coin in response:
        data[coin] = {response[Coins.USD]['codein'] : response[Coins.USD]['high']}
    return data

