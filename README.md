# Stock Analysis Learning Project

A Python learning project that reads an asset CSV, retrieves prices and exchange
rates from Yahoo Finance with yfinance, and converts asset prices to EUR.

The current script does not yet use LangChain or an AI model.

## Setup

Use Python 3.11 and run these commands in the project folder:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Input data

Create a local file named `assets july 7 2025.csv`. The script requires columns
named `Ticker` and `Currency Yahoo`. For example:

```csv
Ticker,Currency Yahoo
AAPL,USD
BTC-USD,USD
```

CSV files are excluded from Git to keep local financial data private.

## Run

```sh
python Main.py
```

An internet connection is required. The script prints exchange rates and the
asset table with a `Price EUR` column. Results depend on available Yahoo data.
