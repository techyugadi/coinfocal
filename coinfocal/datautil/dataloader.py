#!/usr/bin/env python3

import numpy as np
import pandas as pd
from datetime import datetime

def loadprices_df(csvfile, startdate=None, enddate=None):
    df = pd.read_csv(csvfile, header=0, usecols=['Date', 'Close'])
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    df['t'] = np.arange(df.shape[0])

    if startdate is not None:
        start = datetime.strptime(startdate, '%Y-%m-%d')
        if enddate is not None:
            end = datetime.strptime(enddate, '%Y-%m-%d')
            mask = (df['Date'] >= start) & (df['Date'] < end)
        else:
            mask = (df['Date'] >= startdate)
        df = df.loc[mask]
        
    return df

def loadprice_col(csvfile, startdate=None, enddate=None):
    df = loadprices_df(csvfile, startdate, enddate)
    
    tcol = df['t'].to_numpy()
    datecol = df['Date'].to_numpy()
    closecol = df['Close'].to_numpy()
    
    return tcol, datecol, closecol