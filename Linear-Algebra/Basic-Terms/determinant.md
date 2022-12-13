[determinant / 行列式] [Laplace Expansion] [minor]

# Introduction and Definition

Ofen it is useful to use one single number to characterize a multivariate phenomenon. Determinant is one example of this.

Consider a square matrix $A$ with size $n\times n$. $A$ can be a real matrix $A\in\mathbb{R}^{n\times n}$ or a complex matrix $A\in\mathbb{C}^{n\times n}$.

> **Definition:** The determinant is a function of a square matrix $A$, whose output is a scalar value.

The determinant is usually denoted as $\mathrm{det}A$, or $\mathrm{det}(A)$, or $|A|$.

For a real matrix, the determinant is a real scalar. For a complex matrix, the determinant can be a complex scalar.

# How to Calculate Determinant?

## Method 1: An Iterative Approach: Laplace Expansion

First of all, let's define

- $a_{i,j}$: the $i$-th row and $j$-th column element of matrix $A$,
- $A_{i,j}$: the submatrix of $A$ obtained by deleting the $i$-th row and $j$-th column, i.e. the row and column where $a_{i,j}$ is located, 
- $\det(A_{i,j})$, a determinant of a ($r$-by-$r$) submatrix is called a *minor* (of size $r$) [Horn 2013, P17]. In this case, $r=n-1$.
- where $i,j\in[1,2,\cdots,n]$.
- The determinant of a scalar (1-by-1 matrix) is its own value, i.e. $\det([1])=1$.

### Example,

$$A=\begin{bmatrix}1&4&3\\2&\boxed{6}&9\\8&7&5\end{bmatrix},\quad a_{2,2}=5,\quad A_{2,2}=\begin{bmatrix}1&3\\8&5\end{bmatrix}.$$

> **Laplace Expansion** of $i$-th row
> $$\det(A)=\sum_{j=1}^{n}(-1)^{i+j}a_{i,j}\det(A_{i,j})$$
> **Laplace Expansion** of $j$-th column
> $$\det(A)=\sum_{i=1}^{n}(-1)^{i+j}a_{i,j}\det(A_{i,j})$$

### Example:

The determinant of A is $\det(A)=113$.

This result can be obtained by program [[Python with `numpy`](src_determinant_by_numpy.py)] or [[Matlab with `det`](src_determinant_by_det.m)].

#### Expanse by 1st row

For $i=1$, we have

$$j=1:\quad A=\begin{bmatrix}\boxed{1}&4&3\\2&6&9\\8&7&5\end{bmatrix},a_{1,1}=1,A_{1,1}=\begin{bmatrix}6&9\\7&5\end{bmatrix},$$

$$j=2:\quad A=\begin{bmatrix}1&\boxed{4}&3\\2&6&9\\8&7&5\end{bmatrix},a_{1,2}=4,A_{1,2}=\begin{bmatrix}2&9\\8&5\end{bmatrix},$$

$$j=3:\quad A=\begin{bmatrix}1&4&\boxed{3}\\2&6&9\\8&7&5\end{bmatrix},a_{1,3}=3,A_{1,3}=\begin{bmatrix}2&6\\8&7\end{bmatrix}.$$

The minors (determinant of $A_{i,j}$) can be again obtained by further Laplace Expansion with respect to the first row:

$$\det\left(\begin{bmatrix}6&9\\7&5\end{bmatrix}\right)=(-1)^{1+1}\cdot6\cdot5+(-1)^{1+2}\cdot9\cdot7=30-63=-33,$$

$$\det\left(\begin{bmatrix}2&9\\8&5\end{bmatrix}\right)=(-1)^{1+1}\cdot2\cdot5+(-1)^{1+2}\cdot9\cdot8=10-72=-62,$$

$$\det\left(\begin{bmatrix}2&6\\8&7\end{bmatrix}\right)=(-1)^{1+1}\cdot2\cdot7+(-1)^{1+2}\cdot6\cdot8=14-48=-34.$$

Put these into the Laplace Expansion, we have

$$\begin{aligned}\det(A)=&\sum_{j=1}^{n}(-1)^{i+j}a_{i,j}\det(A_{i,j})\\
=&(-1)^{1+1}\cdot1\cdot\det\left(\begin{bmatrix}6&9\\7&5\end{bmatrix}\right)+(-1)^{1+2}\cdot4\cdot\det\left(\begin{bmatrix}2&9\\8&5\end{bmatrix}\right)\\
&+(-1)^{1+3}\cdot3\cdot\det\left(\begin{bmatrix}2&6\\8&7\end{bmatrix}\right)\\
=&-33+248-102=113.\end{aligned}$$

## Method 2: Laplace Expansion: Simplified Calculation Up to 3-by-3 Matrix

### 1-by-1 Matrix

$$\det([a_{11}])=a_{11}.$$

### 2-by-2 Matrix

$$\det\left(\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}\right)=a_{11}a_{22}-a_{12}a_{21}.$$

That is, the determinant of a 2-by-2 matrix equals the product of main diagonal minus the product of counterdiagonal.

### 3-by-3 Matrix

$$\begin{aligned}\det\left(\begin{bmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{bmatrix}\right)&=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a{31}a_{21}a_{32}\\
&-a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}-a_{13}a_{22}a_{31}.\end{aligned}$$

## Method 3: Product of Eigenvalues

The determinant of a matrix is the product of its eigenvalues.

> Assume $\lambda_1,\lambda_2,\cdots,\lambda_n$ are the eigenvalues of the $n$-by-$n$ matrix A.
> $$\det(A)=\prod_{i=1}^{n}\lambda_i.$$

# Properties of Determinant

The determinant of a square matrix obey a large number of important identities.

## Determinant of an identity matrix is 1.

$$\det(I)=1.$$

## Determinant of an upper triangular or a lower triangular matrix is the product of the main diagonal.

$$\det\left(\begin{bmatrix}a_{11}&a_{12}&a_{13}\\0&a_{22}&a_{23}\\0&0&a_{33}\end{bmatrix}\right)=a_{11}a_{22}a_{33}.$$

$$\det\left(\begin{bmatrix}a_{11}&0&0\\a_{21}&a_{22}&0\\a_{31}&a_{32}&a_{33}\end{bmatrix}\right)=a_{11}a_{22}a_{33}.$$

## Determinants of its transpose and itself are the same.

$$\det(A)=\det(A^T).$$

## Multiplicative function

$$\det(AB)=\det(A)\det(B),$$

where $A,B$ are square matrices of the same dimension.

We can notice that although the commutative property of matrix multiplication doesn't hold, i.e. $AB\neq BA$, their determinats are the same $\det(AB)=\det(A)\det(B)=\det(BA)=\det(B)\det(A)$. This may be proved using elementary operations that row-reduce both $A$ and $B$.

## Weinstein-Aronszajn Determinant Identity

$$\det(1+AB)=\det(1+BA),$$

where $A$ is an $n\times m$ matrix and $B$ is an $m\times n$ matrix.

This can be proved by applying multiplicativity with $A=\begin{bmatrix}I_n&-A\\B&I_m\end{bmatrix}$ and $B=\begin{bmatrix}I_n&A\\0&I_m\end{bmatrix}$.

> This identity, which coverts an $n\times n$ determinant into an $m\times m$ determinant, is very useful in random matrix theory, particularly in regimes in which $m$ is much smaller than $n$. [(Terry Tao)](https://terrytao.wordpress.com/2013/01/13/matrix-identities-as-derivatives-of-determinant-identities/)

## Determinant by applying Schur complement

If $A$ is invertible,

$$\det\left(\begin{bmatrix}A&B\\C&D\end{bmatrix}\right)=\det(A)\det(D-CA^{-1}B).$$

If $D$ is invertible,

$$\det\left(\begin{bmatrix}A&B\\C&D\end{bmatrix}\right)=\det(D)\det(A-BD^{-1}C).$$

# References

Horn, R. A., & Johnson, C. R. (2013). *Matrix Analysis (2nd ed.)*. Cambridge University Press.
