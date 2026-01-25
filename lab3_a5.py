from scipy.spatial.distance import minkowski as scipy_minkowski
def minkowski_distance(vector_1, vector_2, p):
    # The function computes the Minkowski distance btw two feature vectors for a given p value
    distance = np.sum(np.abs(vector_1 - vector_2) ** p) ** (1 / p)
    return distance

# mainprogram

# using the same feature vectors as in A4
feature_vector_1 = X_features[0]
feature_vector_2 = X_features[1]

# selecting a p value for comparison
p_value = 3

# minkowski distance found useing the custom function
custom_minkowski_distance = minkowski_distance(
    feature_vector_1,
    feature_vector_2,
    p_value
)

# minkowski distance found  using the SciPy function
scipy_minkowski_distance = scipy_minkowski(
    feature_vector_1,
    feature_vector_2,
    p_value
)

# displaying the results
print(" Custom Minkowski Distance (p = 3):", custom_minkowski_distance)
print(" SciPy Minkowski Distance (p = 3):", scipy_minkowski_distance)
