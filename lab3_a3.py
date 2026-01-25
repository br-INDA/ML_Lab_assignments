import matplotlib.pyplot as plt
import numpy as np
#Calculates mean and variance of a feature vector
def calculate_feature_statistics(feature_vector):
    

    mean_value = np.mean(feature_vector)
    variance_value = np.var(feature_vector)
    return mean_value, variance_value

#main program
# takes the first feature
feature_index = 0
selected_feature = X_features[:, feature_index]

mean_feature, variance_feature = calculate_feature_statistics(selected_feature)

plt.hist(selected_feature, bins=20)
plt.xlabel("Feature Value")
plt.ylabel("Frequency")
plt.title("A3: Histogram of Feature 0")
plt.show()

print("A3: Mean of feature:", mean_feature)
print("A3: Variance of feature:", variance_feature)

