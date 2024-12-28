import pandas as pd

# Load the dataset (update file path if needed)
data = pd.read_csv("creditcard.csv")

# Inspect the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Save summary statistics to a file
with open("data_summary.txt", "w") as file:
    file.write(str(data.describe()))

print("Data loaded successfully and summary saved!")
