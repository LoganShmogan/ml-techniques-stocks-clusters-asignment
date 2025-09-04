import pandas as pd

# Task 3: Data Classification - Breast Cancer Dataset (UCI)

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"

# Dataset does not have headers, so we add them manually
columns = [
    "id", "clump_thickness", "uniformity_cell_size", "uniformity_cell_shape",
    "marginal_adhesion", "single_epithelial_cell_size", "bare_nuclei",
    "bland_chromatin", "normal_nucleoli", "mitoses", "class"
]

df = pd.read_csv(url, names=columns)

print("Breast Cancer data sample:")
print(df.head())
print("Columns:", df.columns.tolist())
