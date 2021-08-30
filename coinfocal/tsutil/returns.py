#!/usr/bin/env python3

from math import log

def logdiv(prices):
    ret = []
    
    nprices = len(prices)
    t = 1
    while t < nprices:
        r_t = ( log(prices[t]) / log(prices[t-1]) ) * 100
        ret.append(r_t)
        t += 1
    
    print('ret=', ret)    
    return ret

def logdiff(prices):
    ret = []
    
    nprices = len(prices)
    t = 1
    while t < nprices:
        r_t = ( log(prices[t]) - log(prices[t-1]) ) * 100
        ret.append(r_t)
        t += 1
        
    return ret