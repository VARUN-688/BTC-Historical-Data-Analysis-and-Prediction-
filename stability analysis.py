import pandas as pd
import matplotlib.pyplot as plt

btc_data = pd.read_csv('BTC_USD_historical_data.csv', parse_dates=['Date'], index_col='Date')

btc_data['Daily Return'] = btc_data['Close'].pct_change()
btc_data['Volatility'] = btc_data['Daily Return'].rolling(window=30).std()

high_volatility = btc_data['Volatility'] > btc_data['Volatility'].quantile(0.75)
low_volatility = btc_data['Volatility'] < btc_data['Volatility'].quantile(0.25)

plt.figure(figsize=(12, 6))
plt.plot(btc_data.index, btc_data['Volatility'], label='30-Day Rolling Volatility', color='blue')
plt.fill_between(btc_data.index, btc_data['Volatility'], where=high_volatility, color='red', alpha=0.3, label='High Volatility')
plt.fill_between(btc_data.index, btc_data['Volatility'], where=low_volatility, color='green', alpha=0.3, label='Low Volatility')

plt.title('BTC Volatility with High and Low Stability Periods')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
