import yfinance as yf
import pandas as pd

def download_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close'].dropna()

def get_stock_pair_data(ticker1, ticker2, start_date='2020-01-01', end_date='2023-12-31'):
    a = download_stock_data(ticker1, start_date, end_date)
    b = download_stock_data(ticker2, start_date, end_date)
    df = pd.concat([a, b], axis=1)
    df.columns = [ticker1, ticker2]
    df.dropna(inplace=True)
    return df
