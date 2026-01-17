import pandas as pa
import numpy as nu
import time
import matplotlib.pyplot as plt

def load_data():
    df = pa.read_excel("Lab_Session_Data.xlsx", sheet_name="IRCTC Stock Price")
    price = df.iloc[:, 3].values   
    return df, price

def mean_variance(price):
    mean_val = nu.mean(price)
    var_val = nu.var(price)
    return mean_val, var_val

def manual_mean(data):
    total = 0
    for val in data:
        total += val
    return total / len(data)

def manual_variance(data):
    mean_val = manual_mean(data)
    total = 0
    for val in data:
        total += (val - mean_val) ** 2
    return total / len(data)

def time_function(func, data):
    start = time.time()
    func(data)
    end = time.time()
    return end - start

df, price = load_data()
mean_val, var_val = mean_variance(price)
print("Mean value of the stock price:", mean_val)
print("Variance  value of the stock price:", var_val)
print("Manual Mean:", manual_mean(price))
print("Manual Variance:", manual_variance(price))
print("NumPy Mean:", nu.mean(price))
print("NumPy Variance:", nu.var(price))
manual_time = sum(time_function(manual_mean, price) for _ in range(10)) / 10
numpy_time = sum(time_function(nu.mean, price) for _ in range(10)) / 10
print("Average Manual Mean Time:", manual_time)
print("Average NumPy Mean Time:", numpy_time)
wednesday_prices = df[df["Day"] == "Wed"]["Price"]
print("Wednesday Sample Mean:", wednesday_prices.mean())
april_prices = df[df["Month"] == "Apr"].iloc[:, 3]
print("April's Sample Mean is", april_prices.mean())
losses = list(filter(lambda x: x < 0, df["Chg%"]))
prob_loss = len(losses) / len(df)
print("probability of loss is", prob_loss)
profit_wed = df[(df["Day"] == "Wed") & (df["Chg%"] > 0)]
print("Probability of Profit on Wednesday:",
      len(profit_wed) / len(df))

plt.scatter(df["Day"], df["Chg%"])
plt.xlabel("Day of Week")
plt.ylabel("Change %")
plt.title("Scatter Plot of Chg% vs Day")
plt.show()




