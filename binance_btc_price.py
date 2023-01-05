'''
gotta admit that gpt3 is amazing:

me: 
help me write python script for retrieving bitcoin prices from binance 
and show the result as plot

AI: Sure! Here is a simple example of how you can retrieve bitcoin 
prices from Binance and plot the results using Python:
'''

import requests
import pandas as pd
import matplotlib.pyplot as plt

# Set the URL for the Binance API endpoint
url = "https://api.binance.com/api/v3/klines"

# Set the parameters for the API request
# In this example, we are retrieving the BTC/USDT price data for the past 30 days
params = {
    "symbol": "BTCUSDT",  # Set the symbol to BTC/USDT
    "interval": "1d",  # Set the interval to 1 day
    "limit": 30  # Set the limit to 30 (i.e. the past 30 days)
}

# Send the request to the Binance API and store the response
response = requests.get(url, params=params)

# Convert the response data to a Pandas DataFrame
df = pd.DataFrame(response.json())

# Extract the close prices and convert them to a list
close_prices = df[4].astype(float).tolist()

# Calculate the moving average of the close prices
moving_average = df[4].astype(float).rolling(window=5).mean().tolist()

# Set the support and resistance levels
support_level = 7000
resistance_level = 8000

# Plot the close prices and moving average
plt.plot(close_prices)
plt.plot(moving_average)

# Add the support and resistance levels to the plot
plt.axhline(y=support_level, linestyle='--', color='green')
plt.axhline(y=resistance_level, linestyle='--', color='red')

plt.show()
