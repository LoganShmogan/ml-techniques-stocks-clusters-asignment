import pandas as pd

# Task 4: Principal Component Analysis - Wine Dataset (UCI)

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"

columns = [
    "class", "alcohol", "malic_acid", "ash", "alcalinity_of_ash",
    "magnesium", "total_phenols", "flavanoids", "nonflavanoid_phenols",
    "proanthocyanins", "color_intensity", "hue",
    "od280/od315_of_diluted_wines", "proline"
]

df = pd.read_csv(url, names=columns)

print("Wine data sample:")
print(df.head())
print("Columns:", df.columns.tolist())
