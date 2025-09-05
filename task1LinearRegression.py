import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Get stock data
ticker = yf.Ticker("AAPL")  # you can pick another stock, e.g. "MSFT"
df = ticker.history(period="5y")
print(df.head())

# Define Features (X) and Target (y)
X = df[["Open", "High", "Low", "Volume"]]
y = df["Close"]

# Print features to console
print("Features (X) sample:")
print(X.head())
print("\nTarget (y) sample:")
print(y.head())

# Plot a scatter graph Open VS Close (AAPL)
plt.scatter(df["Open"], df["Close"], alpha=0.5)
plt.xlabel("Open Price")
plt.ylabel("Close Price")
plt.title("Scatter Plot: Open vs Close (AAPL)")
plt.show()

# Combine X and y into one DataFrame
corr = df[["Open", "High", "Low", "Volume", "Close"]].corr()

print("Correlation matrix:")
print(corr["Close"])


