- Topics: Power Iteration Method, 
- Last revised: 22.05.2022

---

# Background

*Power Iteration Method* is a simple and one of the oldest method for computing the eigenvector corresponding to dominant eigenvalue of a diagonalizable matrix, which with deflation was the method of choice until the 1950s (Björck, 2015). However, it is no longer competitive for most problems.

# Introduction

Consider a matrix $\mathbf{A}\in\mathbb{C}^{n\times n}$ with eigenvalues $\lambda_1,\lambda_2,\cdots,\lambda_n$ in ordered $|\lambda_1|\geq|\lambda_2|\geq\cdots|\lambda_n|$, where $\lambda_1$ is the unique maximum eigenvalue. Note that in general the eigenvalue $\lambda_i$ can be either real or complex.

The matrix $\mathbf{A}$ can be diagonalized as $\mathbf{A}=\mathbf{V}\boldsymbol{\Lambda} \mathbf{V}^{-1}$ where $\boldsymbol{\Lambda}=\mathrm{diag}(\lambda_1,\cdots,\lambda_n)$, and $\mathbf{V}=\left[\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots,\boldsymbol{v}_n\right]$ are the unit eigenvectors, i.e. $|\boldsymbol{v}_i|=1$. The name of this method, i.e. power iteration, comes from the use of the power of $A$, where

$$\mathbf{A}^k=(\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1})(\mathbf{V}\boldsymbol{\Lambda}\mathbf{V}^{-1})\cdots(\mathbf{V}\boldsymbol{\Lambda} \mathbf{V}^{-1})=\mathbf{V}\boldsymbol{\Lambda}^{k}\mathbf{V}^{-1},$$

or in another form

$$\mathbf{A}^k\mathbf{V}=\mathbf{V}\boldsymbol{\Lambda}^k,\quad\forall k\in\mathbb{N}.$$

This means that for each eigenpair $\lambda_i$ and $\boldsymbol{v}_i$, we have $\mathbf{A}^k\boldsymbol{v}_i=\lambda_i^k\boldsymbol{v}_i$. This is the fundation of the power iteration method.

Suppose we have a random (initialization) vector $\tilde{\boldsymbol{c}}=[\tilde{c}_1,\tilde{c}_2,\cdots,\tilde{c}_n]^T\in\mathbb{C}^{n}$ with uni norm $\tilde{\boldsymbol{c}}^H\tilde{\boldsymbol{c}}=1$. If we don't normalize the vector in the iteration, the vector becomes quickly too large or too small. Since at the end $\tilde{\boldsymbol{c}}$ should be the eigenvector associated with the largest eigenvalue, which means that $\tilde{\boldsymbol{c}}$ should be one of the eigenvector. Hence, we can writ it as a linear combination of the eigenvector of $\mathbf{A}$, i.e., $\boldsymbol{c}^{(0)}=\mathbf{V}\tilde{\boldsymbol{c}}=\tilde{c}_1\boldsymbol{v}_1+\cdots+\tilde{c}_n\boldsymbol{v}_n$.

$$\begin{aligned}
\boldsymbol{c}^{(k)}&=\mathbf{A}^k\boldsymbol{c}=\mathbf{A}^k\mathbf{V}\tilde{\boldsymbol{c}}=\mathbf{V}\boldsymbol{\Lambda}^k\tilde{\boldsymbol{c}}\\
&=\tilde{c}_1\lambda_1^k\boldsymbol{v}_1+\tilde{c}_2\lambda_2^k\boldsymbol{v}_2+\cdots+\tilde{c}_n\lambda_n^k\boldsymbol{v}_n\\
&=\sum_{j=1}^{n}\tilde{c}_j\lambda_{j}^{k}\boldsymbol{v}_j.
\end{aligned}$$

Note that $\boldsymbol{c}^{(k+1)}=\mathbf{A}\boldsymbol{c}^{(k)}$. Assume for now that and $\lambda_1\neq0$. Pull out $\lambda_1$ leads to

$$\boldsymbol{c}^{(k)}=\lambda_1^k\left(\sum_{j=1}^{n}\tilde{c}_j\left(\frac{\lambda_{j}}{\lambda_{1}}\right)^{k}\boldsymbol{v}_j\right).$$

Remember that $\lambda_1$ is the largest eigenvalue. For $k\rightarrow\infty$, $(\lambda_j/\lambda_1)^k$ goes to 0 except for $j=1$, and finally we have the result

$$\lim_{k\rightarrow\infty}\mathbf{A}^k\boldsymbol{c}=\lambda_1^k\tilde{c}_1\boldsymbol{v}_1.$$

Assume that $\tilde{c}_1\neq0$. The above equation indicates that for large enough $k$, such a randomly initialized vector $\boldsymbol{c}$ multiplied by $\mathbf{A}^k$ will be converged to $\boldsymbol{v}_1$, the normalized eigenvector associated to the largest eigenvalue. In other words, the unit eigenvector associated with the largest eigenvalue $\lambda_1$ can be approximated by

$$\boldsymbol{v}_1\approx\frac{\mathbf{A}^k\boldsymbol{c}}{\left\|\mathbf{A}^k\boldsymbol{c}\right\|}.$$

The convergence is linear, with rate equal to $|\lambda_2|/|\lambda_1|$. 

For the largest eigenvalue $\lambda_1$, assume that $\boldsymbol{c}^{(k)}$ is close to $\boldsymbol{v}_1$ at the $k$-th iteration. Hence, we have

$$\mathbf{A}\boldsymbol{c}^{(k)}\approx\lambda_1\boldsymbol{c}^{(k)}.$$

To obtain the approximated $\lambda_1$, multiply $\boldsymbol{c}^{(k),H}$ on both sides, i.e.

$$\boldsymbol{c}^{(k),H}\mathbf{A}\boldsymbol{c}^{(k)}\approx\lambda_1\boldsymbol{c}^{(k),H}\boldsymbol{c}^{(k)}=\lambda_1.$$

**Power Iteration Method**. 

1. Choose a random initialization $\boldsymbol{c}^{0}$.
2. Compute $\boldsymbol{c}^{k+1}=\frac{\mathbf{A}\boldsymbol{c}^{k}}{\left\|\mathbf{A}\boldsymbol{c}^{k}\right\|}$.
3. Compute $\lambda_1^{(k)}=\boldsymbol{c}^{(k),H}\boldsymbol{c}^{(k+1)}$.
4. Stop if $k>K_0$. Otherwise, repeat starting from 2.

# Advantages

- Only need to compute $\mathbf{A}\boldsymbol{c}$ in each iteration. $\mathbf{A}^k$ are never computed and the matrix $\mathbf{A}$ is not modified. Therefore, This method is suitable for large and sparse matrices.

# Drawbacks

- In each iteration, $\mathbf{A}$ is multiplied, resulting in a possible overflow, i.e. values of result become too small or too large.
  - can be solved when a normalization is executed in each iteration.
- Only returns the largest eigenvalue and eigenvector.
- Eigenvalues must be distinct to guarantee the convergence. 
- he Tconvergence rate primarily depends upon the ration of the two largest eigenvalues. If they are close, the algorithm converges slowly.

# References

Björck, A. (2015). *Numerical Methods in Matrix Computations*. Springer.