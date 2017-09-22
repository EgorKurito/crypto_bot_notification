import config
import numpy as np
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

################################################

def BTCUSD_24(url):
    # Paser url, parametr: BTCUSD_HOURLY_CSV_URL - url of csv, names - edit names of column
    BTCUSD_HOURLY = pd.io.parsers.read_csv(url, names = ['Timestamp', 'Date', 'Value','Volume'])
    # Read and edit: .head() - header list /// .loc[] - edit column /// .ix[] - edit row
    BTCUSD_HOURLY_24 = BTCUSD_HOURLY.head(25).ix[1:].loc[:,['Date','Value']]

    return(BTCUSD_HOURLY_24)

def BTCUSD_price_change_proc(parr):
    BTCUSD_first = float(parr.iloc[0,1])
    BTCUSD_last = float(parr.iloc[23,1])

    BTCUSD_proc_change = BTCUSD_first * 100 / BTCUSD_last - 100

    return(BTCUSD_proc_change)

def BTCUSD_price_change(parr):
    BTCUSD_first = float(parr.iloc[0,1])
    BTCUSD_last = float(parr.iloc[23,1])

    BTCUSD_change = BTCUSD_first - BTCUSD_last

    return(BTCUSD_change)

################################################

def ETHUSD_24(url):
    ETHUSD_HOURLY = pd.io.parsers.read_csv(url, names = ['Timestamp', 'Date', 'Value','Volume'])
    ETHUSD_HOURLY_24 = ETHUSD_HOURLY.head(25).ix[1:].loc[:,['Date','Value']]

    return(ETHUSD_HOURLY_24)

def ETHUSD_price_change_proc(parr):
    ETHUSD_first = float(parr.iloc[0,1])
    ETHUSD_last = float(parr.iloc[23,1])

    ETHUSD_proc_change = ETHUSD_first * 100 / ETHUSD_last - 100

    return(ETHUSD_proc_change)

def ETHUSD_price_change(parr):
    ETHUSD_first = float(parr.iloc[0,1])
    ETHUSD_last = float(parr.iloc[23,1])

    ETHUSD_change = ETHUSD_first - ETHUSD_last

    return(ETHUSD_change)

################################################

def ETCUSD_24(url):
    ETCUSD_HOURLY = pd.io.parsers.read_csv(url, names = ['Timestamp', 'Date', 'Value','Volume'])
    ETCUSD_HOURLY_24 = ETCUSD_HOURLY.head(25).ix[1:].loc[:,['Date','Value']]

    return(ETCUSD_HOURLY_24)

def ETCUSD_price_change_proc(parr):
    ETCUSD_first = float(parr.iloc[0,1])
    ETCUSD_last = float(parr.iloc[23,1])

    ETCUSD_proc_change = ETCUSD_first * 100 / ETCUSD_last - 100

    return(ETCUSD_proc_change)

def ETCUSD_price_change(parr):
    ETCUSD_first = float(parr.iloc[0,1])
    ETCUSD_last = float(parr.iloc[23,1])

    ETCUSD_change = ETCUSD_first - ETCUSD_last

    return(ETCUSD_change)

################################################

def main():

    BTCUSD = BTCUSD_24(config.BTCUSD_URL)
    BTC_CHANGE_P = BTCUSD_price_change_proc(BTCUSD)
    BTC_CHANGE = BTCUSD_price_change(BTCUSD)
    BTCUSD.to_csv('projects.csv', sep='\t', encoding='utf-8')

    ETHUSD = ETHUSD_24(config.ETHUSD_URL)
    ETH_CHANGE_P = ETHUSD_price_change_proc(ETHUSD)
    ETH_CHANGE = ETHUSD_price_change(ETHUSD)

    ETCUSD = ETCUSD_24(config.ETCUSD_URL)
    ETC_CHANGE_P = ETCUSD_price_change_proc(ETCUSD)
    ETC_CHANGE = ETCUSD_price_change(ETCUSD)

    print(BTCUSD)
    print("%.2f" % BTC_CHANGE_P + ' %')
    print("%.2f" % BTC_CHANGE)

    print(ETHUSD)
    print("%.2f" % ETH_CHANGE_P + ' %')
    print("%.2f" % ETH_CHANGE)

    print(ETCUSD)
    print("%.2f" % ETC_CHANGE_P + ' %')
    print("%.2f" % ETC_CHANGE)

    #print("%.2f" % a)

if __name__ == '__main__':
    main()

# Rewrite and read csv file
#BTCUSD_HOURLY_24.to_csv('BTC.csv', index=False)
