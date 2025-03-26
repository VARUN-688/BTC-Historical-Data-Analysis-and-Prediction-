import pandas as pd

# Read CSV, skip duplicate header row, and parse dates with specified format
btc_data = pd.read_csv(
    'BTC_USD_historical_data.csv',
    header=1,  # Skip the extra header
    names=["Date", "Open", "High", "Low", "Close", "Volume"],
    parse_dates=["Date"],
    date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d', errors='coerce'),
    index_col="Date"
)

# Drop any rows with missing dates
btc_data.dropna(subset=["Open"], inplace=True)

# Display the first few rows
print(btc_data.head())
