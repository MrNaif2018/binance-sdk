import requests
import urllib
try:
    from . import errors, models
except (ImportError, ValueError):
    import models,errors

BINANCE_BASE_URL="https://testnet-dex.binance.org/api/v1/"

def send_request(base_url, method, format_s="", **kwargs):
    url=base_url+method+format_s
    query_string=urllib.parse.urlencode(kwargs)
    if query_string:
        url+="?"+query_string
    try:
        request_json=requests.get(url).json()
    except Exception as e:
        raise errors.BinanceRequestError(e)
    try:
        code=request_json.get("code",200)
        if not (code >= 200 and code < 300):
            raise errors.BinanceApiError(code,"Error code: {}. {}".format(code,request_json.get("message","")))
    except (IndexError, KeyError):
        pass
    if type(request_json) == dict:
        return models.JsonDict(request_json)
    else:
        json_list=[]
        for i in request_json:
            json_list.append(models.JsonDict(i))
        return json_list

class Binance:
    def __init__(self,base_url=None):
        self.base_url=base_url or BINANCE_BASE_URL

    def __getattr__(self,method):
        def wrapper(format_s="",**kwargs):
            return send_request(self.base_url, method, format_s, **kwargs)
        return wrapper

    def tx(self, tx_hash):
        return send_request(self.base_url, "tx","/{hash}".format(hash=tx_hash),format="json")
