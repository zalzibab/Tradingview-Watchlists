
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


BITFINEX = []
BITFINEX_raw = requests.get('https://api-pub.bitfinex.com/v2/tickers?symbols=ALL').json()
for ticker in range(len(BITFINEX_raw)):
    BITFINEX.append(BITFINEX_raw[ticker][0])
BITFINEX = ['BITFINEX:'+x[1:] for x in BITFINEX if x[0] == 't' and ':' not in x and 'CNHT' not in x and 'TEST' not in x and 'BBB' not in x]
BITFINEX.sort()
write_txt('BITFINEX.txt', BITFINEX)


HUOBI = ['HUOBI:'+x['symbol'].upper() for x in requests.get('https://api.huobi.pro/market/tickers').json()['data'] if x['symbol'].upper()[-2:] != 'HT' and '10' not in x['symbol'].upper() and 'BTC3' not in x['symbol'].upper() and 'X8' not in x['symbol'].upper() and 'BTC1' not in x['symbol'].upper()]
HUOBI.sort()
write_txt('HUOBI.txt', HUOBI)


HITBTC = ['HITBTC:'+x['id'] for x in requests.get('https://api.hitbtc.com/api/2/public/symbol').json()]
HITBTC.sort()
write_txt('HITBTC.txt', HITBTC)


BITTREX = ['BITTREX:'+x['symbol'].replace('-', '') for x in requests.get('https://api.bittrex.com/v3/markets/tickers').json()]
BITTREX.sort()
write_txt('BITTREX.txt', BITTREX)


COINBASE = ['COINBASE:'+x['id'].replace('-', '') for x in requests.get('https://api.pro.coinbase.com/products').json()]
COINBASE.sort()
write_txt('COINBASE.txt', COINBASE)


OKEX_raw = [x['instrument_id'].replace('-', '')[:-4] for x in requests.get('https://www.okex.com/api/swap/v3/instruments/ticker').json()]
OKEX = ['OKEX:'+x for x in OKEX_raw if x[-1] == 'T'] + ['OKEX:BTCUSDTPERP', 'OKEX:BTCUSDPERP', 'OKEX:BTCUSDT3M', 'OKEX:BTCUSD3M', 'OKEX:BTCUSDT6M', 'OKEX:BTCUSD6M', 'OKEX:BTCUSDT1W', 'OKEX:BTCUSD1W', 'OKEX:BTCUSDT2W', 'OKEX:BTCUSD2W']
OKEX.sort()
write_txt('OKEX.txt', OKEX)

