import pandas as pd
import numpy as np

FILE_NAME = "Lab_Session_Data.xlsx"
SHEET_NAME = "thyroid0387_UCI"

df = pd.read_excel(FILE_NAME, sheet_name=SHEET_NAME)

numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

print("Numerical attributes (need normalization):")
print(numerical_cols)

print("\nCategorical attributes (no normalization needed):")
print(categorical_cols)

df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].median())

minmax_df = df.copy()
for col in numerical_cols:
    min_val = df[col].min()
    max_val = df[col].max()
    if max_val - min_val != 0:
        minmax_df[col] = (df[col] - min_val) / (max_val - min_val)
    else:
        minmax_df[col] = 0  

zscore_df = df.copy()
for col in numerical_cols:
    mean_val = df[col].mean()
    std_val = df[col].std()
    if std_val != 0:
        zscore_df[col] = (df[col] - mean_val) / std_val
    else:
        zscore_df[col] = 0  

minmax_df.to_excel("thyroid_minmax_normalized.xlsx", index=False)
zscore_df.to_excel("thyroid_zscore_standardized.xlsx", index=False)

print("\n✅ Normalized datasets created successfully!")
print("1) thyroid_minmax_normalized.xlsx")
print("2) thyroid_zscore_standardized.xlsx")
