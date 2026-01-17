import pandas as pd
import numpy as np


def load_data(file_path, sheet_name):
    dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
    return dataframe

def get_numerical_columns(dataframe):
    return dataframe.select_dtypes(include=['int64', 'float64']).columns.tolist()

def min_max_normalization(dataframe, numerical_columns):
    normalized_df = dataframe.copy()
    for column in numerical_columns:
        min_val = dataframe[column].min()
        max_val = dataframe[column].max()
        normalized_df[column] = (dataframe[column] - min_val) / (max_val - min_val)
    return normalized_df


def z_score_standardization(dataframe, numerical_columns):
    standardized_df = dataframe.copy()
    for column in numerical_columns:
        mean_val = dataframe[column].mean()
        std_val = dataframe[column].std()
        standardized_df[column] = (dataframe[column] - mean_val) / std_val
    return standardized_df


df = load_data("Lab_Session_Data.xlsx", "thyroid0387_UCI")
numerical_cols = get_numerical_columns(df)
min_max_df = min_max_normalization(df, numerical_cols)
z_score_df = z_score_standardization(df, numerical_cols)
print("Min-Max Normalized Data (first 5 rows):\n")
print(min_max_df[numerical_cols].head())
print("\nZ-score Standardized Data (first 5 rows):\n")
print(z_score_df[numerical_cols].head())




