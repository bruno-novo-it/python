#!/usr/bin/env python


# To install: pip install requests

from util import bcolors
import sys
import requests
import json
import hashlib
import hmac
import urllib
import http.client
import time

from collections import OrderedDict

#Coin_Type = str(sys.argv[1])
#ticker = "https://www.mercadobitcoin.net/api/%s/ticker/" % Coin_Type
#orderbook = "https://www.mercadobitcoin.net/api/%s/orderbook/" % Coin_Type
#trades = "https://www.mercadobitcoin.net/api/%s/trades/" % Coin_Type

#resp_ticker = requests.get(ticker) # Status code, example: 200
#resp_orderbook = requests.get(orderbook)
#resp_trades = requests.get(trades)

#print("\n{}Ticker Content:{} {}".format(bcolors.Blue,bcolors.Final,resp_ticker.content["ticker"]))

## LTC ##

#LTC_Ticker_URL = "https://www.mercadobitcoin.net/api/LTC/ticker/"

#LTC_Ticker_Response = requests.get(LTC_Ticker_URL)

## BTC ##

#BTC_Ticker_URL = "https://www.mercadobitcoin.net/api/BTC/ticker/"

#BTC_Ticker_Response = requests.get(BTC_Ticker_URL)

## Print Results ##
#print("Bitcoin Price: {}".format(BTC_Ticker_Response.json()["ticker"]["last"]),
#        "\nLitcoin Price: {}".format(LTC_Ticker_Response.json()["ticker"]["last"]))

### Mercado Bitcoin ###

# PIN de segurança ==> 4665
# Nome: tab-trader-app
# Identificador: 1a8cb71ea5b65dccec8fcb4acffcc898
# Segredo: 6b40d34d176bf95c4e24ba7dc06fa64305891352dffc3c64efcc3543d85a7678

# Constantes e Parâmetros
MB_TAPI_ID = '1a8cb71ea5b65dccec8fcb4acffcc898'
MB_TAPI_SECRET = '6b40d34d176bf95c4e24ba7dc06fa64305891352dffc3c64efcc3543d85a7678'
REQUEST_HOST = 'www.mercadobitcoin.net'
REQUEST_PATH = '/tapi/v3/'

# Nonce
tapi_nonce = int(str(time.time()).replace(".", ""))

# Parâmetros (variam de acordo com o método)
params = {
    'tapi_method': 'get_account_info',
    'tapi_nonce': tapi_nonce,
    'coin_pair': 'BRLBTC'
}

# Parâmetros formatados
# Utilizado no request
params = urllib.parse.urlencode(params)

# Gerar MAC
params_string = REQUEST_PATH + '?' + params
TAPI_MAC = hmac.new(MB_TAPI_SECRET.encode('utf-8'), params_string.encode('utf-8'),
             digestmod=hashlib.sha512).hexdigest()

# Gerar cabeçalho da requisição
headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'TAPI-ID': MB_TAPI_ID,
    'TAPI-MAC': TAPI_MAC
}

# Realizar requisição POST
try:
    conn = http.client.HTTPSConnection(REQUEST_HOST)
    conn.request("POST", REQUEST_PATH, params, headers)

    # Print response data to console
    response = conn.getresponse()
    response = response.read()

    # É fundamental utilizar a classe OrderedDict para preservar a ordem dos elementos
    response_json = json.loads(response, object_pairs_hook=OrderedDict)
    print("status: %s" % response_json['status_code'])
    print(json.dumps(response_json, indent=4))
finally:
    if conn:
        conn.close()


### Crypto Compare API ###

## BTC ##

#BTC_crypto_compare_url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,BRL"

#BTC_URL_Response = requests.get(BTC_crypto_compare_url)

## LTC ##

#LTC_crypto_compare_url = "https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,BRL"

#LTC_URL_Response = requests.get(LTC_crypto_compare_url)

## Print Results ##

# print("Bitcoin Price(USD): {}".format(BTC_URL_Response.json()["USD"]),
#         "\nBitcoin Price(BRL): {}".format(BTC_URL_Response.json()["BRL"]),
#         "\nLitecoin Price(USD): {}".format(LTC_URL_Response.json()["USD"]),
#         "\nLitecoin Price(BRL): {}".format(LTC_URL_Response.json()["BRL"]))
