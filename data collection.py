import yfinance as yf
import pandas as pd

def fetch_crypto_data(symbol='BTC-USD', start_date='2020-01-01', end_date='2025-01-01'):
    crypto_df = yf.download(symbol, start=start_date, end=end_date)

    crypto_df.reset_index(inplace=True)
    crypto_df['Date'] = pd.to_datetime(crypto_df['Date'])
    crypto_df.set_index('Date', inplace=True)
    crypto_df.fillna(method='ffill', inplace=True)
    filename = f"{symbol.replace('-', '_')}_historical_data.csv"
    crypto_df.to_csv(filename)

    print(f"Data saved to {filename}")
    return crypto_df

# Example: Fetch Bitcoin price data
btc_data = fetch_crypto_data('BTC-USD', '2020-01-01', '2025-01-01')

# Preview the data
print(btc_data.head())
