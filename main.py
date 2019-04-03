import requests
import urllib
from . import errors

BINANCE_BASE_URL="https://testnet-dex.binance.org/api/v1/"


class JsonDict:
    def __init__(self, json):
        self.json=json

    def __getattr__(self, key):
        return self.json[key]

    def __getitem__(self, key):
        return self.json[key]
        
    def __repr__(self):
        return str(self.json)

class Binance:
    def __init__(self,base_url=None):
        self.base_url=base_url or BINANCE_BASE_URL

    def __getattr__(self,method):
        def wrapper(format_s="",**kwargs):
            '''try:
                format_s=args[0]
            except IndexError:
                format_s=""'''
            url=self.base_url+method+format_s
            query_string=urllib.parse.urlencode(kwargs)
            if query_string:
                url+="?"+query_string
            try:
                request_json=requests.get(url).json()
            except Exception as e:
                raise errors.BinanceRequestError(e)
            if not (request_json.get("code",200) >= 200 < 300):
                raise errors.BinanceApiError("Error code: {}. Message: {}".format(request_json.get("code",200),request_json.get("message","")))
            return JsonDict(request_json)
        return wrapper

binance=Binance()
print(binance.transactions())