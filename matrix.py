import numpy as np

# Fall 1: 2x2 Matrix × 2x3 Matrix
matrix1_1 = np.zeros((2, 2))
matrix1_2 = np.zeros((2, 3))
result1 = np.dot(matrix1_1, matrix1_2)
print("Ergebnis 1:")
print(result1)
print()

# Fall 2: 3x1 Matrix × 1x3 Matrix
matrix2_1 = np.zeros((3, 1))
matrix2_2 = np.zeros((1, 3))
result2 = np.dot(matrix2_1, matrix2_2)
print("Ergebnis 2:")
print(result2)
print()

# Fall 3: 1x3 Matrix × 3x1 Matrix
matrix3_1 = np.zeros((1, 3))
matrix3_2 = np.zeros((3, 1))
result3 = np.dot(matrix3_1, matrix3_2)
print("Ergebnis 3:")
print(result3)