import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go


st.title("Yahoo Finance Stock Data")

ticker = st.text_input("Ticker", value="AAPL", max_chars=5)
stock = yf.Ticker(ticker)
data = stock.history(period="6mo")

fig = go.Figure(data=[go.Candlestick(
	x=data.index,
	open=data["Open"],
	high=data["High"],
	low=data["Low"],
	close=data["Close"],
	name=ticker)])
fig.update_xaxes(type="category")
fig.update_layout(height=700)
st.plotly_chart(fig, use_container_width=True)

for item in stock.news:
	st.subheader(item["title"])
	st.write(item["publisher"])
	st.write(item["link"])
	st.write("\n")




