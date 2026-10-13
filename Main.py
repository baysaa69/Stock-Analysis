import pandas as pd
import yfinance as yf
from datetime import date
import numpy as np
import matplotlib.pyplot as plt 

#Load CSV File
df = pd.read_csv('assets july 7 2025.csv')
# print(df.head().to_string(index=False))

#FX Rates

# Retrieve the Exchange Rates
pair = "USDEUR=X"
exchange_rate = yf.Ticker(pair).history(period="1d")["Close"].iloc[-1]
# print(exchange_rate)


# Function Retrieve the Exchange Rates

def get_fx_rate(from_currency: str, to_currency :str = "EUR") -> float:
  """ Get the live FX rate from Yahoo. Returns 1.0 if the same currency is used. """
  if from_currency == to_currency: 
    return 1.0 
  
  pair = f"{from_currency}{to_currency}=X"
  data = yf.Ticker(pair).history(period="1d")
  return float(data["Close"].iloc[-1])


print(get_fx_rate("USD","EUR"))

#Cache the FX rates
fx_cache = {}
for fx in df['Currency Yahoo'].unique():
  if fx =="EUR":
    fx_cache[fx] = 1.0
  else:
    fx_cache[fx] = get_fx_rate(fx)

#Display the cache
print("FX Cache", fx_cache)


# Retreive price data in local currency
#Retrieve the price of one ticker
yf.Ticker("BTC-USD").history(period = "1d")['Close']
# Build a function to fetch prices 
def get_price_local(row) -> float:
  """ Fetch the yahoo price in native currency and convert to local currency """
  try:
    price_native = (
      yf.Ticker(row['Ticker']).history(period = "1d")['Close'].iloc[-1]
    )
    return price_native * fx_cache[row['Currency Yahoo']]
  except Exception:
    print(f"Error fetching {row['Ticker']}")

    return np.nan

df['Price EUR'] =df.apply(get_price_local, axis=1)
print(df)