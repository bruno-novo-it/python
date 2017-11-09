#!/usr/bin/python

# To install: pip install requests

from util import bcolors
import sys
import requests
import json

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


# PIN de segurança ==> 4665
# Nome: tab-trader-app
# Identificador: 1a8cb71ea5b65dccec8fcb4acffcc898
# Segredo: 6b40d34d176bf95c4e24ba7dc06fa64305891352dffc3c64efcc3543d85a7678

### Crypto Compare API ###

## BTC ##

BTC_crypto_compare_url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,BRL"

BTC_URL_Response = requests.get(BTC_crypto_compare_url)

## LTC ##

LTC_crypto_compare_url = "https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,BRL"

LTC_URL_Response = requests.get(LTC_crypto_compare_url)

## Print Results ##

print("Bitcoin Price(USD): {}".format(BTC_URL_Response.json()["USD"]),
        "\nBitcoin Price(BRL): {}".format(BTC_URL_Response.json()["BRL"]),
        "\nLitecoin Price(USD): {}".format(LTC_URL_Response.json()["USD"]),
        "\nLitecoin Price(BRL): {}".format(LTC_URL_Response.json()["BRL"]))
