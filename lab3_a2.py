import numpy as np

# Loading the feature vectors 
X_features = np.load("X_telugu_embeddings.npy")

# Createing binary class labels,same length as the "X_features"
y_labels = np.array(
    [0] * (len(X_features) // 2) +
    [1] * (len(X_features) - len(X_features) // 2)
)

print("dataset loaded")
print("total number of samples:", len(X_features))
print("class 0 samples:", np.sum(y_labels == 0))
print("class 1 samples:", np.sum(y_labels == 1))

#used for a2

#A2
import numpy as np
# Calculates mean vector for given data matrix.    
def calculate_mean(data_matrix):
    return np.mean(data_matrix, axis=0)

# Calculates variance vector for given data matrix.
def calculate_variance(data_matrix):
    return np.var(data_matrix, axis=0)

# Calculates standard deviation vector for given data matrix.
def calculate_standard_deviation(data_matrix):
    return np.std(data_matrix, axis=0)

# Calculates euclidean distance between two class centroids.
def calculate_centroid_distance(centroid_class_1, centroid_class_2):
    return np.linalg.norm(centroid_class_1 - centroid_class_2)

# main program

# separateing the data by class
class_0_data = X_features[y_labels == 0]
class_1_data = X_features[y_labels == 1]

# centroid
centroid_class_0 = calculate_mean(class_0_data)
centroid_class_1 = calculate_mean(class_1_data)

# spread
std_class_0 = calculate_standard_deviation(class_0_data)
std_class_1 = calculate_standard_deviation(class_1_data)

# inter-class distance
inter_class_distance = calculate_centroid_distance(
    centroid_class_0, centroid_class_1
)

print("A2: Inter-class distance:", inter_class_distance)
print("A2: Mean spread (Class 0):", np.mean(std_class_0))
print("A2: Mean spread (Class 1):", np.mean(std_class_1))
