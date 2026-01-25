import numpy as np

# Function to calculate dot product
def calculate_dot_product(vector_a, vector_b):
   
    a = np.array(vector_a)
    b = np.array(vector_b)
    
    dot_prod = 0
    for i in range(len(a)):
        dot_prod += a[i] * b[i]
    
    return dot_prod


# Function to calculate Euclidean norm (length)
def calculate_euclidean_norm(vector):
   
    vec = np.array(vector)
    
    sum_squares = 0
    for i in range(len(vec)):
        sum_squares += vec[i] ** 2
    
    return np.sqrt(sum_squares)


# MAIN PROGRAM

# Define two vectors
A = [3, 4, 5, 6]
B = [1, 2, 3, 4]

print("Vector A:", A)
print("Vector B:", B)

# DOT PRODUCT
print("\n--- DOT PRODUCT ---")
my_dot = calculate_dot_product(A, B)
numpy_dot = np.dot(A, B)

print(f"My function:    {my_dot}")
print(f"NumPy function: {numpy_dot}")
print(f"Match? {np.allclose(my_dot, numpy_dot)}")

# EUCLIDEAN NORM
print("\n--- EUCLIDEAN NORM ---")
print("\nVector A:")
my_norm_a = calculate_euclidean_norm(A)
numpy_norm_a = np.linalg.norm(A)
print(f"My function:    {my_norm_a:.4f}")
print(f"NumPy function: {numpy_norm_a:.4f}")
print(f"Match? {np.allclose(my_norm_a, numpy_norm_a)}")

print("\nVector B:")
my_norm_b = calculate_euclidean_norm(B)
numpy_norm_b = np.linalg.norm(B)
print(f"My function:    {my_norm_b:.4f}")
print(f"NumPy function: {numpy_norm_b:.4f}")
print(f"Match? {np.allclose(my_norm_b, numpy_norm_b)}")
