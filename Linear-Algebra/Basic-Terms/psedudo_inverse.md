[Pseudo-Inverse / 伪逆矩阵] [Moore-Penrose Inverse]

A square and inverible matrix has its inverse. For a nonsquare matrix with different number of rows and column has no inverse. However, we can calculate the pseudo-inverse of a nonsquare matrix, which has the similar property of the inverse, i.e. the product of its pseudo-inverse (or inverse for square matrix) and itself is an identity matrix.

# Definition of Pseudo-Inverse of A Matrix

Consider a matrix $\mathbf{A}$ of size $m\times n$. The pseudo-inverse of $\mathbf{A}$ is usually denoted by a superscript $\dagger$, i.e. $\mathbf{A}^{\dagger}$.

## If $\mathbf{A}$ is full column rank

Meaning $\text{rank}(\mathbf{A})=n\leq m$. That is 

- $\mathbf{A}$ is a tall matrix.
- $\mathbf{A}^{T}\mathbf{A}$ is not singular.
- $\mathbf{A}^{\dagger}$ is a left inverse of $\mathbf{A}$, i.e. $\mathbf{A}^{\dagger}\mathbf{A}=\mathbf{I}_n$.
- $\mathbf{A}^{\dagger}=(\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^{T}$.

## If $\mathbf{A}$ is full row rank

Meaning $\text{rank}(\mathbf{A})=m<n$. That is

- $\mathbf{A}$ is a flat matrix.
- $\mathbf{A}\mathbf{A}^{T}$ is not singular.
- $\mathbf{A}^{\dagger}$ is a right inverse of $\mathbf{A}$, i.e. $\mathbf{A}\mathbf{A}^{\dagger}=\mathbf{I}_m$.
- $\mathbf{A}^{\dagger}=\mathbf{A}^{T}(\mathbf{A}\mathbf{A}^T)^{-1}$.

## If $\mathbf{A}$ is square, invertilbe

Its inverse is $\mathbf{A}^{\dagger}=\mathbf{A}^{-1}$.

# Expressed From Singular Value Decomposition (SVD)

The pseudo-inverse generalizes the inverse of a square matrix. It can also be described with the SVD.

The SVD of a matrix $\mathbf{A}$ with size $m\times n$ is

$$\mathbf{A}=\mathbf{U}\begin{bmatrix}
\mathbf{S} & \mathbf{0}\\
\mathbf{0} & \mathbf{0}
\end{bmatrix}\mathbf{V}^T.$$

The pseudo-inverse of $\mathbf{A}$ is the $n\times m$ matrix defined as

$$\mathbf{A}^{\dagger}=\mathbf{V}\begin{bmatrix}
\mathbf{S}^{-1} & \mathbf{0}\\
\mathbf{0} & \mathbf{0}
\end{bmatrix}\mathbf{U}^T.$$

*Proof*. It is too easy to prove. $\square$

# Application

The solution to the least-squares problem

$$\min_{x}\|\mathbf{A}\boldsymbol{x}-\boldsymbol{y}\|$$

with minimum norm is $\boldsymbol{x}^{\text{opt}}=\mathbf{A}^{\dagger}\boldsymbol{y}$.