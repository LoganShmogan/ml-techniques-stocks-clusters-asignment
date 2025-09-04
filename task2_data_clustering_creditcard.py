import pandas as pd

# Task 2: Data Clustering - Credit Card Data (Kaggle)
# Make sure the 'CC GENERAL.csv' file is in the same folder as this script.

df = pd.read_csv("CC GENERAL.csv")

print("Credit Card data sample:")
print(df.head())
print("Columns:", df.columns.tolist())
