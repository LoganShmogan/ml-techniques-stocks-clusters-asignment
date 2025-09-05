import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

# Split dataset: 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training features shape:", X_train.shape)
print("Testing features shape:", X_test.shape)
print("Training target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)


# Multivariate linear regression model on training data

# Model Creation
model = LinearRegression()

# fit model to training data
model.fit(X_train, y_train)

# Print model
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
