import numpy as np

matrix = np.random.randint(0, 10, size=(3, 3))
transpose_matrix = np.transpose(matrix)

print("Original Matrix:")
print(matrix)

print("\nTranspose of Matrix:")
print(transpose_matrix)
