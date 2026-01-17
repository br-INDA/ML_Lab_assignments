import pandas as pd
import numpy as np

def load_data(file_path, sheet_name):
    dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
    return dataframe

def get_datatypes(dataframe):
    return dataframe.dtypes

def separate_columns(dataframe):
    categorical_columns = dataframe.select_dtypes(include=['object']).columns.tolist()
    numerical_columns = dataframe.select_dtypes(include=['int64', 'float64']).columns.tolist()
    return categorical_columns, numerical_columns


def data_range(dataframe, numerical_columns):
    ranges = {}
    for column in numerical_columns:
        ranges[column] = (dataframe[column].min(), dataframe[column].max())
    return ranges


def missing_values(dataframe):
    return dataframe.isnull().sum()

def detect_outliers(dataframe, numerical_columns):
    outlier_count = {}
    for column in numerical_columns:
        Q1 = dataframe[column].quantile(0.25)
        Q3 = dataframe[column].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = dataframe[
            (dataframe[column] < lower) | (dataframe[column] > upper)
        ]
        outlier_count[column] = outliers.shape[0]
    return outlier_count

def calculate_mean_variance(dataframe, numerical_columns):
    statistics = {}
    for column in numerical_columns:
        statistics[column] = (dataframe[column].mean(), dataframe[column].var())
    return statistics

df = load_data("Lab_Session_Data.xlsx", "thyroid0387_UCI")
datatypes = get_datatypes(df)
categorical_cols, numerical_cols = separate_columns(df)
ranges = data_range(df, numerical_cols)
missing = missing_values(df)
outliers = detect_outliers(df, numerical_cols)
stats = calculate_mean_variance(df, numerical_cols)
print("attribute data types:\n")
print(datatypes)
print("\ncategorical attributes:")
print(categorical_cols)
print("\nnumerical attributes:")
print(numerical_cols)
print("\ndata range (min, max):")
for key, value in ranges.items():
    print(f"{key}: {value}")
print("\nmissing values as per the attributes:")
print(missing)

print("\noutline count per numerical attribute:")
for key, value in outliers.items():
    print(f"{key}: {value}")

print("\nmean and variance:")
for key, value in stats.items():
    print(f"{key}: mean = {value[0]}, variance = {value[1]}")



