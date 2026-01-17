import pandas as pd
import numpy as np


file = "Lab_Session_Data.xlsx"
df = pd.read_excel(file, sheet_name="thyroid0387_UCI")

numeric_df = df.select_dtypes(include=[np.number])
binary_df = numeric_df.fillna(0)
binary_df = binary_df.map(lambda x: 1 if x > 0 else 0)

v1 = binary_df.iloc[0].values
v2 = binary_df.iloc[1].values

f11 = f10 = f01 = f00 = 0

for i in range(len(v1)):
    if v1[i] == 1 and v2[i] == 1:
        f11 += 1
    elif v1[i] == 1 and v2[i] == 0:
        f10 += 1
    elif v1[i] == 0 and v2[i] == 1:
        f01 += 1
    elif v1[i] == 0 and v2[i] == 0:
        f00 += 1

jaccard = f11 / (f11 + f10 + f01)
smc = (f11 + f00) / (f11 + f10 + f01 + f00)

print("f11:", f11)
print("f10:", f10)
print("f01:", f01)
print("f00:", f00)

print("jaccard coefficient value is", jaccard)
print("simple matching coefficient value is", smc)
