import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

btc_data = pd.read_csv('BTC_USD_historical_data.csv', parse_dates=['Date'], index_col='Date')

fig = go.Figure(data=[go.Candlestick(
    x=btc_data.index,
    open=btc_data['Open'],
    high=btc_data['High'],
    low=btc_data['Low'],
    close=btc_data['Close']
)])
fig.update_layout(title='BTC Candlestick Chart', xaxis_title='Date', yaxis_title='Price (USD)')
fig.show()

heatmap_fig = px.imshow(
    btc_data[['Open','High','Low','Close','Volume']].corr(),
    color_continuous_scale='RdBu_r',
    title='BTC Feature Correlation Heatmap'
)
heatmap_fig.show()
