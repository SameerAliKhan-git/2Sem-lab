# 01. Write a program to find the product and sum of two matrices [A]nxp and [B]pxr using Numpy.


import numpy as np

# Example sizes
n, p, r = 3, 2, 4

# Create random matrices A[nxp] and B[pxr]
A = np.random.randint(1, 10, size=(n, p))
B = np.random.randint(1, 10, size=(p, r))

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Matrix Sum (Only possible if shapes match)
if A.shape == B.shape:
    matrix_sum = A + B
    print("\nSum of A and B:")
    print(matrix_sum)
else:
    print("\nSum not possible: Matrices have different shapes.")

# Matrix Product
product = np.dot(A, B)
print("\nProduct of A and B:")
print(product)
