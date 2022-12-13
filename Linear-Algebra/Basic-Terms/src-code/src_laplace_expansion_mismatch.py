import numpy as np

A = np.array([[1,4,3],[2,6,9],[8,7,5]], dtype=int)

# calculate the adjugate
# inverse = adjugate / determinant => adjugate = inverse * determinant
adjugate_A = np.linalg.inv(A) * np.linalg.det(A)

# cofactor matrix
cofactor_A = adjugate_A.T

# print adjugate of A
print(adjugate_A)

# should be det(A)*I
print(A.dot(adjugate_A))

# should be the determinant
print(np.dot(A[1], cofactor_A[1]))

# should be 0, if the row of A and cofactor matrix don't match
print(np.dot(A[1], cofactor_A[2]))