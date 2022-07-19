import numpy as np

# create a matrix
M = np.array([[1,2,1],[0,1,0],[1,0,1]])
print('The original matrix is: \n', M, '\n')

# compute eigenvalues and eigenvectors
Lambda, U = np.linalg.eig(M)
sort_perm = Lambda.argsort()[::-1]
Lambda = np.sort(Lambda)[::-1]
U = U[:, sort_perm]
print('--- Eigenvalue Decomposition ---')
print('The eigenvalue matrix is:\n', Lambda)
print('The eigenvector matrix is:\n', U, '\n')

# power iteration method

# 1. obtain initialzation vector
print('--- Power Iteration Method ---')
u0 = np.random.rand(3)
print('The initialization vector is: ', u0)
u0_norm = u0 / np.linalg.norm(u0)
print('The normalized initialization vector is:', u0_norm) 

# 2. power of the matrix
print('For each iteration, the MSE of largest-eigenvalue associated eigenvector and the power iteration approximation is:')
for i in range(10):
  u0 = M.dot(u0_norm)
  u0_norm = u0 / np.linalg.norm(u0)
  diff = np.linalg.norm(u0_norm - U[:,0])
  print('Iteration ',i,': MSE = ',diff)

   
