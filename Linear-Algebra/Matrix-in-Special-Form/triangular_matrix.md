- Topic: Triangular Matrix
- Last revised: 12.12.2022

---

# Definition of a triangular matrix

A triangular is a special form of the square matrix. A matrix of the form

$$L=\begin{bmatrix}
   l_{1,1}&&&&0\\
   l_{2,1}&l_{2,2}&&&\\
   l_{3,1}&l_{3,2}&\ddots&&\\
   \vdots&\vdots&\ddots&\ddots&\\
   l_{n,1}&l_{n,2}&\cdots&l_{n,n-1}&l_{n,n} 
\end{bmatrix}$$

is called *lower triangular matrix* or *left triangular matrix*. Similarly, a matrix of the form

$$U=\begin{bmatrix}
   u_{1,1}&u_{1,2}&u_{1,3}&\cdots&u_{1,n}\\
   &u_{2,2}&u_{2,3}&\cdots&u_{2,n}\\
   &&\ddots&\ddots&\vdots\\
   &&&\ddots&u_{n-1,n}\\
   0&&&&u_{n,n}
\end{bmatrix}$$

is called *upper triangular matrix* or *right triangular matrix*.

This special form in a linear system of a form $$Ax=b$$ can make the problem very easy to solve. If $A$ is an upper triangular matrix, an iterative process called *forward substitution* is used. If $A$ is a lower triangular matrix then *backward substitution*.

# Properties of a triangular matrix

- The transpose of an upper triangular matrix is a lower triangular matrix and vice versa.
- A matrix which is both symmetric and triangular is diagonal.
- A matrix which is both unitary and triangular is an identity matrix.
- The eigenvalues of a triangular matrix are exactly its diagonal entries.
- The sum of two upper (lower) triangular matrices is upper (lower) triangular.
- The product of two upper (lower) triangular matrices is upper (lower) triangular.
- The inverse of an upper (lower) triangular matrix, if it exists, is upper (lower) triangular.