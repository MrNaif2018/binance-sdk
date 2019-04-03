#!/usr/bin/env python3
from client import Binance
import sys

if len(sys.argv) == 1:
    print("Usage: binance-cli command [options]")
else:
    binance=Binance()
    args=sys.argv[1:]
    command=args[0]
    kwargs={}
    for i in args[1:]:
        key,value=i.split("=")
        kwargs[key]=value
    print(getattr(binance,command)(**kwargs))

