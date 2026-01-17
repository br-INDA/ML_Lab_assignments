import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file = "Lab_Session_Data.xlsx"
df = pd.read_excel(file, sheet_name="thyroid0387_UCI")
df_20 = df.iloc[:20]
numeric_df = df_20.select_dtypes(include=[np.number]).fillna(0)
binary_df = numeric_df.apply(lambda col: col.map(lambda x: 1 if x > 0 else 0))

def jaccard(v1, v2):
    f11 = f10 = f01 = 0
    for i in range(len(v1)):
        if v1[i] == 1 and v2[i] == 1:
            f11 += 1
        elif v1[i] == 1 and v2[i] == 0:
            f10 += 1
        elif v1[i] == 0 and v2[i] == 1:
            f01 += 1
    return f11 / (f11 + f10 + f01)

def smc(v1, v2):
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
    return (f11 + f00) / (f11 + f10 + f01 + f00)

def cosine(v1, v2):
    dot = 0
    mag1 = 0
    mag2 = 0
    for i in range(len(v1)):
        dot += v1[i] * v2[i]
        mag1 += v1[i] ** 2
        mag2 += v2[i] ** 2
    return dot / ((mag1 ** 0.5) * (mag2 ** 0.5))


jc_matrix = np.zeros((20, 20))
smc_matrix = np.zeros((20, 20))
cos_matrix = np.zeros((20, 20))


for i in range(20):
    for j in range(20):
        jc_matrix[i][j] = jaccard(binary_df.iloc[i].values,
                                  binary_df.iloc[j].values)

        smc_matrix[i][j] = smc(binary_df.iloc[i].values,
                               binary_df.iloc[j].values)

        cos_matrix[i][j] = cosine(numeric_df.iloc[i].values,
                                  numeric_df.iloc[j].values)


plt.imshow(jc_matrix, cmap='hot')
plt.colorbar()
plt.title("jaccard values heatmap")
plt.show()

plt.imshow(smc_matrix, cmap='hot')
plt.colorbar()
plt.title("simple Matching value heatmap")
plt.show()

plt.imshow(cos_matrix, cmap='hot')
plt.colorbar()
plt.title("cosine similarity heatmap")
plt.show()
