import config
import requests

class BitFinex:
    def __init__(self, url):
        self.url = config.url + url

    def mid(self):
        # get information
        mid = requests.get(self.url, timeout=1).text
        # str to dict & get param: 'mid'
        mid = eval(mid).get('mid')
        return mid

    def low(self):
        low =   eval(requests.get(self.url, timeout=1).text).get('low')
        return low

    def high(self):
        high =   eval(requests.get(self.url, timeout=1).text).get('high')
        return high
