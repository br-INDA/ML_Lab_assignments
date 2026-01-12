def matrix_multiplication(m1, m2):
    rows_a = len(m1)
    cols_a = len(m1[0])
    rows_b = len(m2)
    cols_b = len(m2[0])
    # Check if matrix multiplication is possible (columns of A must match rows of B)
    if cols_a != rows_b:
        return None
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
  
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

#main
matrix1 = [[-1, 1], [2, 4]]
matrix2 = [[1, -1], [6, 8]]
result = matrix_multiplication(matrix1, matrix2)
print("Product of matrices:")
print(result)
