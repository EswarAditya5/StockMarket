#!/usr/bin/env python
# coding: utf-8

# !pip install streamlit

# !pip install yfinance
yfinance
# !pip install ta

# In[1]:


import io
import os
import numpy as np
import pandas as pd
import datetime


# In[2]:


#Finance App
import streamlit as st
import yfinance as yf


# In[3]:


ticker=st.sidebar.text_input('Enter a valid stock ticker','GOOG')
ticker=yf.Ticker(ticker)
today=datetime.date.today()
before=today-datetime.timedelta(days=700)
start_date=st.sidebar.date_input('start date',before)
end_date=st.sidebar.date_input('end date',today)
if start_date < end_date:
    st.sidebar.success('Start Date:`%s`\n\n End date:`%s`'%(start_date,end_date))
else:
    st.sidebar.error('Error: End date must be after start date')


# ticker=st.sidebar.selectbox('Select Ticker',('INFY.NS','TCS.NS','WIPRO.NS'))
# today=datetime.date.today()
# before=today-datetime.timedelta(days=700)
# start_date=st.sidebar.date_input('start date',before)
# end_date=st.sidebar.date_input('end date',today)
# if start_date < end_date:
#     st.sidebar.success('Start Date:`%s`\n\n End date:`%s`'%(start_date,end_date))
# else:
#     st.sidebar.error('Error: End date must be after start date')

# In[4]:


from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator


# In[5]:


stock_df=ticker.history('ld',start=start_date,end=end_date)


# stock_df=yf.download(ticker,start=start_date,end=end_date,progress=False)

# In[6]:


stock_df.head()


# In[7]:


bb_ind=BollingerBands(stock_df['Close'])
bb=stock_df
bb['bb_h']=bb_ind.bollinger_hband()
bb['bb_l']=bb_ind.bollinger_lband()
bb=bb[['Close','bb_h','bb_l']]


# In[8]:


macd=MACD(stock_df['Close']).macd()


# In[9]:


rsi=RSIIndicator(stock_df['Close']).rsi()


# In[10]:


st.line_chart(bb)
progress_bar=st.progress(0)
st.area_chart(macd)
st.line_chart(rsi)


# In[ ]:





# In[ ]:




