# Define two 2x2 matrices A and B
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Matrix Addition
addition_result = []
for i in range(2):  # rows
    row = []
    for j in range(2):  # columns
        row.append(A[i][j] + B[i][j])
    addition_result.append(row)

print("Matrix Addition Result:")
for row in addition_result:
    print(row)

# Matrix Subtraction
subtraction_result = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(A[i][j] - B[i][j])
    subtraction_result.append(row)

print("\nMatrix Subtraction Result:")
for row in subtraction_result:
    print(row)

# Matrix Transpose (of matrix A)
transpose_result = []
for i in range(2):  # columns
    row = []
    for j in range(2):  # rows
        row.append(A[j][i])
    transpose_result.append(row)

print("\nTranspose of Matrix A:")
for row in transpose_result:
    print(row)
