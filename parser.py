import csv
import requests
from pandas import read_csv

CSV_URL = 'https://www.bfxdata.com/csv/vwapHourlyBTCUSD.csv'

last = []

def download(url):

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
    return my_list

def last_possiton(my_list):
    j = 0

    for row in my_list:
        last.append(row[1:3])
        j = j +1
        if j == 25:
            break;

    last.pop(0)

df1 = read_csv(download(CSV_URL))

def main():
    my_list = download(CSV_URL)
    last_possiton(my_list)
    #print(last)
    print(df1)
if __name__ == '__main__':
    main()
