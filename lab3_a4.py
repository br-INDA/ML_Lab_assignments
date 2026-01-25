import numpy as np

def minkowski_distance(vector_1, vector_2, p):
    # The function computes the Minkowski distance btw two feature vectors for a given p value
    distance = np.sum(np.abs(vector_1 - vector_2) ** p) ** (1 / p)
    return distance

# mainprogram
# selecting  two feature vectors from the dataset
feature_vector_1 = X_features[0]
feature_vector_2 = X_features[1]

# the range of p values
p_values = range(1, 11)

# list to be stored in the Minkowski distances
minkowski_distances = []

# calculate the Minkowski distance for each p
for p in p_values:
    distance = minkowski_distance(feature_vector_1, feature_vector_2, p)
    minkowski_distances.append(distance)

# plotting the Minkowski distance vs p
plt.plot(p_values, minkowski_distances, marker='o')
plt.xlabel("Value of p")
plt.ylabel("Minkowski Distance")
plt.title("A4: Minkowski Distance vs p")
plt.grid(True)
plt.show()

