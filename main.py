import time
from api_binance import api_key,api_secret
from binance.client import Client
client = Client(api_key, api_secret)
from binance.exceptions import BinanceAPIException

while True:
    def balance(client):
        balance = client.get_asset_balance("bts")
        print(balance)
        return float(balance["free"])

    def bot_binance(client,coin,address,addressTag,amount):
        try:
            # name parameter will be set to the asset value by the client if not passed
            result = client.withdraw(
                coin=coin,
                address=address,
                addressTag=addressTag,
                amount=amount)

        except BinanceAPIException as e:
            print(e)
        else:
            print("Success")
    time_sleep=balance(client)
    if time_sleep>1:
        bot_binance(client=client,coin="",address="",addressTag="",amount=balance(client))
    else:
        time.sleep(2)





