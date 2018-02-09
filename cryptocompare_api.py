#!/usr/bin/env python


# To install: 

# pip install requests
# pip install colorama

from colorama import *
import sys
import requests
import json
import hashlib
import hmac
import urllib
import http.client
import time
import random
import uuid

from collections import OrderedDict

### Crypto Compare API ###

## BTC ##

BTC_crypto_compare_url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,BRL"

BTC_URL_Response = requests.get(BTC_crypto_compare_url)

Bitcoin_updated_price_usd = float(BTC_URL_Response.json()["USD"])
Bitcoin_updated_price_brl = float(BTC_URL_Response.json()["BRL"])

## LTC ##

LTC_crypto_compare_url = "https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,BRL"

LTC_URL_Response = requests.get(LTC_crypto_compare_url)

Litecoin_updated_price_usd = float(LTC_URL_Response.json()["USD"])
Litecoin_updated_price_brl = float(LTC_URL_Response.json()["BRL"])

## Print RealTime Prices ##
def print_the_prices():
    print("{}\nBitcoin Updated Price(USD):{} {}".format(Fore.YELLOW, Style.RESET_ALL,
        Bitcoin_updated_price_usd))
    print("{}Bitcoin Updated Price(BRL):{} {}".format(Fore.YELLOW, Style.RESET_ALL,
        Bitcoin_updated_price_brl))
    print("\nLitecoin Updated Price(USD): {}".format(
        Litecoin_updated_price_usd))
    print("Litecoin Updated Price(BRL): {}".format(
        Litecoin_updated_price_brl))

## Print the Updated Values
print("{}\nCrypto Currency Updated Prices{}".format(Fore.BLUE, Style.RESET_ALL))
print_the_prices()

### Mercado Bitcoin ###

# PIN de segurança ==> 4665
# Nome: tab-trader-app
# Identificador: 1a-Big_Number
# Segredo: 6b-Very_Big_Number

# Variáveis e Parâmetros
MB_TAPI_ID = 'Identificador'
MB_TAPI_SECRET = 'segredo'
REQUEST_HOST = 'www.mercadobitcoin.net'
REQUEST_PATH = '/tapi/v3/'

# Nonce
## I like using uuid1, since it generates the uuid based on 
## current host and time and has the time property that you can 
## extract if you need both.
def generate_nonce_timestamp():
    """Generate pseudo-random number and seconds since epoch (UTC)."""
    nonce = uuid.uuid1()
    oauth_timestamp = str(nonce.time)
    return oauth_timestamp

tapi_nonce = generate_nonce_timestamp()

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
# Função para Imprimir os Resultados
def print_the_request():
    #print("{}\nStatus Code:{} {}".format(
    #     Fore.RED, Fore.RESET, response_json['status_code']))
    #print(json.dumps(response_json, indent=4))
    #print(response_json['response_data']['balance'])
    print("{}\nBalance Available(BRL):{} {}".format(
        Fore.GREEN, Style.RESET_ALL, Balance_available_brl))
    print("{}Balance Total(BRL):{} {}".format(
        Fore.GREEN, Style.RESET_ALL, Balance_total_brl))
    print("{}\nBalance Available(BTC):{} {}".format(
        Fore.YELLOW, Style.RESET_ALL, Balance_available_btc))
    print("{}Balance Total(BTC):{} {}".format(
        Fore.YELLOW, Style.RESET_ALL, Balance_total_btc))
    print("{}Amount Open Orders(BTC):{} {}".format(
        Fore.YELLOW, Style.RESET_ALL, Balance_amount_open_orders_btc))
    print("\nBalance Available(LTC): {}".format(
        Balance_available_ltc))
    print("Balance Total(LTC): {}".format(
        Balance_total_ltc))
    print("Amount Open Orders(LTC): {}".format(
        Balance_amount_open_orders_ltc))

# Realizar requisição POST
try:
    conn = http.client.HTTPSConnection(REQUEST_HOST)
    conn.request("POST", REQUEST_PATH, params, headers)

    # Print response data to console
    response = conn.getresponse()
    response = response.read()

    # É fundamental utilizar a classe OrderedDict para preservar a ordem dos elementos
    response_json = json.loads(response, object_pairs_hook=OrderedDict)

    Balance_available_brl = float(
        response_json['response_data']['balance']['brl']['available'])
    Balance_total_brl = float(
        response_json['response_data']['balance']['brl']['total'])
    Balance_available_btc = float(
        response_json['response_data']['balance']['btc']['available'])
    Balance_total_btc = float(
        response_json['response_data']['balance']['btc']['total'])
    Balance_amount_open_orders_btc = float(
        response_json['response_data']['balance']['btc']['amount_open_orders'])
    Balance_available_ltc = float(
        response_json['response_data']['balance']['ltc']['available'])
    Balance_total_ltc = float(
        response_json['response_data']['balance']['ltc']['total'])
    Balance_amount_open_orders_ltc = float(
        response_json['response_data']['balance']['ltc']['amount_open_orders'])

    print("{}\nMercado Bitcoin API Response{}".format(Fore.RED, Style.RESET_ALL))
    print_the_request()

finally:
    if conn:
        conn.close()