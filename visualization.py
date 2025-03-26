import matplotlib.pyplot as plt
import pandas as pd

def plot_price_trends(data, title='Price Trend'):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue', linewidth=2)
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    plt.plot(data.index, data['SMA_50'], label='50-Day SMA', color='orange', linewidth=1.5)
    plt.plot(data.index, data['SMA_200'], label='200-Day SMA', color='green', linewidth=1.5)
    plt.title(title, fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

btc_data = pd.read_csv('BTC_USD_historical_data.csv', parse_dates=['Date'], index_col='Date')
plot_price_trends(btc_data, title='Bitcoin (BTC) Price Trend with SMA')
