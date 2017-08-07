
import numpy as np
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

BTCUSD_URL = 'https://www.bfxdata.com/csv/vwapHourlyBTCUSD.csv'

# Paser url, parametr: BTCUSD_HOURLY_CSV_URL - url of csv, names - edit names of column
BTCUSD_HOURLY = pd.io.parsers.read_csv(BTCUSD_HOURLY_CSV_URL, names = ['Timestamp', 'Date', 'Value','Volume'])
# Read and edit: .head() - header list /// .loc[] - edit column /// .ix[] - edit row
BTCUSD_HOURLY_24 = BTCUSD_HOURLY.head(25).ix[1:].loc[:,['Date','Value']]

first = BTCUSD_HOURLY_24.iloc[0,1]
last = BTCUSD_HOURLY_24.iloc[23,1]
# Rewrite and read csv file
#BTCUSD_HOURLY_24.to_csv('BTC.csv', index=False)
print(BTCUSD_HOURLY_24)
print('____________________')
print(first)
print(last)
