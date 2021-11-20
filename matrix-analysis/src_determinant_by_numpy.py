import numpy as np

A = np.array([[1,4,3],[2,6,9],[8,7,5]])
d = np.linalg.det(A)

print('Matrix A:')
print(A)
print('Determinant of Matrix A:')
print(np.around(d, decimals=4))
