class BinanceError(Exception):
    pass

class BinanceRequestError(BinanceError):
    pass

class BinanceApiError(BinanceError):
    def __init__(self, code, msg):
        if code == 404:
            raise BinanceApi404Error(msg)
        else:
            super().__init__(msg)

class BinanceApi404Error(BinanceRequestError): 
    pass
