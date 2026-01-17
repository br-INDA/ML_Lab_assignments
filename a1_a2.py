import pandas as pd
import numpy as np

def load_data():
    df = pd.read_excel("Lab_Session_Data.xlsx", sheet_name=0)
    x = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].values
    y = df["Payment (Rs)"].values
    return x,y 

def pseudo_inv(X, y):
    X_pinv = np.linalg.pinv(X)
    cost = X_pinv @ y
    return cost

def classify_customers(y):
    labels = np.where(y > 200, "rich", "poor")
    return labels

x, y = load_data()
rank = np.linalg.matrix_rank(x)
cost = pseudo_inv(x, y)
print("feature matrix x:\n", x)
print("\noutput vector y:\n", y)
print("\nrank of the feature matrix:", rank)
print("\nestimate cost of the products:")
print("Candies (Rs per unit):", cost[0])
print("Mangoes (Rs per kg):", cost[1])
print("Milk Packets (Rs per packet):", cost[2])
labels = classify_customers(y)
print("Customer classified based on  there payment:")
print(labels)





