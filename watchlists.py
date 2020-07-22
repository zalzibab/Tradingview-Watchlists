
# coding: utf-8

import requests
import json


def write_txt(filename, list_item):
    with open(filename, 'w') as f:
        for item in list_item:
            f.write('%s\n' % item)


BITMEX = ['BITMEX:'+x['symbol'] for x in requests.get('https://www.bitmex.com/api/v1/instrument/active').json() if x['state'] == 'Open']
BITMEX.sort()
write_txt('BITMEX.txt', BITMEX)


BYBIT = ['BYBIT:'+x['symbol'] for x in requests.get('https://api.bybit.com/v2/public/tickers').json()['result']]
BYBIT.sort()
write_txt('BYBIT.txt', BYBIT)


FTX = ['FTX:'+x['name'].replace('/', '').replace('-', '') for x in requests.get('https://ftx.com/api/markets').json()['result']]
FTX.sort()
write_txt('FTX.txt', FTX)


BINANCE = ['BINANCE:'+x['symbol'] for x in requests.get('https://api.binance.com/api/v3/ticker/price').json()]
BINANCE.sort()
write_txt('BINANCE.txt', BINANCE)

