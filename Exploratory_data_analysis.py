import pandas as pd

file_path = "/Users/dheerajpv/Documents/Intern/Drug pricing/dataset.csv"
df = pd.read_csv(file_path)

print("Columns:", df.columns)
print("Shape:", df.shape)

print(df.describe())

print(df.isnull().sum())

