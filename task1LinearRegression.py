
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Chatgbt fix not idea what this does
y_pred = model.predict(X_test)

# Model Creation
model = LinearRegression()

# fit model to training data
model.fit(X_train, y_train)
# Chatgbt fix not sure how this works will come back
# TODO
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs. Predicted Values")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Perfect Fit')
plt.legend()
plt.show()
# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# CHATGBT FIX - kept running into errors.. didnt know this was a thing you could do  
# Check if model trained
print("Model trained with features:", X_train.columns.tolist())

# Grab 3 rows of data from test set
sample_data = X_test.iloc[:3]

print("Real sample features:")
print(sample_data)

# Predict using trained model
real_predictions = model.predict(sample_data)

print("\nPredicted Close values for Yahoo Finance data:")
for i, pred in enumerate(real_predictions):
    print(f"Row {i+1} | Actual Close: {y_test.iloc[i]:.2f} | Predicted Close: {pred:.2f}")

# Fit r2 score 
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)