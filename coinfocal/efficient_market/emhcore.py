#!/usr/bin/env python3

import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from crypto.tsutil import returns

def lungj_box(prices, alpha=0.05, lag=None):
    R = returns.logdiv(prices)
    res = ARIMA(R, order=(0, 0, 0)).fit()

    if lag is None:
        lb_stat, lb_pvalue = sm.stats.acorr_ljungbox(res.resid, 
                                                return_df=True, auto_lag=True)
    else:
        if isinstance(lag, int): 
            lbres = sm.stats.acorr_ljungbox(res.resid, 
                                                lags=[lag], return_df=True)
        else:
            raise ValueError("Parameter 'lag' must be an integer")

    print('lb_pvalue = ', lbres['lb_pvalue'])    

    # Return True if market is efficient, else False
    return lbres.lb_pvalue > alpha
