import requests
import json

BASE_API_URL_V3 = "https://api.coingecko.com/api/v3"
PING = f"{BASE_API_URL_V3}/ping"
COINS_LIST = f"{BASE_API_URL_V3}/coins/list"
COINS_GET_BY_ID=f"{BASE_API_URL_V3}/coins"


def coins_get_list():
    params = {
        "include_platform": False
    }
    response = requests.get(COINS_LIST, params=params)
    coins_info = response.json()

    with open("coins_list.json", "w+") as f:
        coins_info_str = json.dumps(coins_info)
        f.write(coins_info_str)


def coins_get_by_id(coin_id: str):
    params = {
        "localization": False,
        "tickers": False,
        "market_data": False,
        "community_data": False,
        "developer_data": False,
        "sparkline": False
    }
    response = requests.get(
        f"{COINS_GET_BY_ID}/{coin_id}",
        params=params)

    coin_info = response.json()
    coin_name = coin_info.get("name", "No name")
    symbol = coin_info.get("symbol", "No symbol")
    market_cap_rank = coin_info.get("market_cap_rank", "No market cap rank")

    print(f"Coin name: {coin_name} || Symbol: {symbol} || Market cap rank: {market_cap_rank}")


if __name__ == '__main__':
    # coins_get_list()
    coins_get_by_id("bitcoin")
    coins_get_by_id("ripple")
