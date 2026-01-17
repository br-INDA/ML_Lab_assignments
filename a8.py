import pandas as pd
import numpy as np

def load_data(file_path, sheet_name):
    dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
    return dataframe

def separate_columns(dataframe):
    categorical_columns = dataframe.select_dtypes(include=['object']).columns.tolist()
    numerical_columns = dataframe.select_dtypes(include=['int64', 'float64']).columns.tolist()
    return categorical_columns, numerical_columns


def has_outliers(dataframe, column_name):
    Q1 = dataframe[column_name].quantile(0.25)
    Q3 = dataframe[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = dataframe[
        (dataframe[column_name] < lower) | (dataframe[column_name] > upper)
    ]
    return not outliers.empty

def impute_missing_values(dataframe, categorical_columns, numerical_columns):
    imputation_details = []

    for column in numerical_columns:
        if dataframe[column].isnull().sum() > 0:
            if has_outliers(dataframe, column):
                replacement = dataframe[column].median()
                dataframe[column].fillna(replacement, inplace=True)
                imputation_details.append((column, "Median"))
            else:
                replacement = dataframe[column].mean()
                dataframe[column].fillna(replacement, inplace=True)
                imputation_details.append((column, "Mean"))

    for column in categorical_columns:
        if dataframe[column].isnull().sum() > 0:
            replacement = dataframe[column].mode()[0]
            dataframe[column].fillna(replacement, inplace=True)
            imputation_details.append((column, "Mode"))

    return dataframe, imputation_details


df = load_data("Lab_Session_Data.xlsx", "thyroid0387_UCI")
categorical_cols, numerical_cols = separate_columns(df)
df, details = impute_missing_values(df, categorical_cols, numerical_cols)

print("imputation summary:\n")
for column, method in details:
    print(f"{column}: filled using {method}")

print("\nmissing values after imputation are\n")
print(df.isnull().sum())


