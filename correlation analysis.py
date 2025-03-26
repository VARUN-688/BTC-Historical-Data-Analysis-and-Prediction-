import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

btc_data = pd.read_csv('BTC_USD_historical_data.csv', parse_dates=['Date'], index_col='Date')

correlation_matrix = btc_data[['Close', 'Open', 'High', 'Low', 'Volume']].corr()

plt.figure(figsize=(7, 5))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('BTC Close Price Correlation with Other Features')
plt.show()