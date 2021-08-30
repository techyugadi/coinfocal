#!/usr/bin/env python3

import crypto.datautil.dataloader as loader
import crypto.efficient_market.emhcore as emhcore

def emh(csvfile, startdate=None, enddate=None):
    _, _, prices = loader.loadprice_col(csvfile, startdate, enddate)
    efficient = emhcore.lungj_box(prices, lag=10)
    
    print("Market is efficient: ", efficient)
    
if __name__ == "__main__":
    # TO DO: Change hardcoded path
    emh('/home/techie/Downloads/BTC-USD.csv')
