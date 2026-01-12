def transpose(matrix):
    transposed_matrix = []
    # Loop through columns of the original matrix
    for column in range(len(matrix[0])):
        current_row = []
        # Loop through rows of the original matrix
        for row in range(len(matrix)):
            #swap rows and columns
            current_row.append(matrix[row][column])
        transposed_matrix.append(current_row)

    return transposed_matrix

#main
original_matrix = [[1, 0, 0], [0, 5, 6],[1,8,9]]
transpose_result = transpose(original_matrix)
print("Transpose of the matrix:")
print(transpose_result)
