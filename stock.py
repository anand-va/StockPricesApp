import pandas as pd
import streamlit as st
from pandas_datareader import data as pdr
from datetime import datetime, timedelta
import yfinance as yfin

yfin.pdr_override()
st.title("Stock Prices App")

stock_name = st.text_input("Enter the stock name: \n")
option = st.slider("How many days of data would you like to see?", 1,60,1)

end = datetime.today().strftime('%Y-%m-%d')
start = (datetime.today() - timedelta(option)).strftime('%Y-%m-%d')

data_load_state = st.text("Loading data...")
#df = pdr.get_data_yahoo(stock_name, start, end)
df=pdr.get_data_yahoo(stock_name, start="2017-01-01", end="2017-04-30")
st.subheader(f'{stock_name} stock prices for the past {option} days')
st.dataframe(df)
chart_data = df[['Close']]
st.subheader("Close Prices")
st.line_chart(chart_data)

data_load_state.text("Data loaded!")
