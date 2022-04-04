import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf


st.sidebar.title("Options")

option = st.sidebar.selectbox("Which dashboard?", ("twitter", "wsb", "yahoo finance"))

st.title(option)

if option == "yahoo finance":
	ticker = st.sidebar.text_input("Ticker", value="AAPL", max_chars=5)
	stock = yf.Ticker(ticker)
	#stock.news
	for item in stock.news:
		st.subheader(item["title"])
		st.write(item["publisher"])
		st.write(item["link"])
		st.write("\n")

if option == "wsb":
	pass

if option == "twitter":
	pass

