# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Dashboard')

tickers= ('HINDUNILVR.NS','RELIANCE.NS','HDFCBANK.NS','TSLA','AAPL','MSFT')

dropdown= st.multiselect('Pick your assets',tickers)

start=st.date_input('Start',value= pd.to_datetime('2021-01-01'))
end=st.date_input('End',value= pd.to_datetime('today'))

if len(dropdown)>0:
    df=yf.download(dropdown,start,end)['Adj Close']
    st.line_chart(df)
    