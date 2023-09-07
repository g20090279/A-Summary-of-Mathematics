- Topics: Symmetric Matrix
- Last Revised: 23.08.2023

---

# Definition of Symmetry of a Matrix 


A matrix $A$ is said to be symmetric if $A^T=A$. 

We only consider matrix in real numbers when we talk about symmetry, while we prefer to study *hermitian* matrix in complex numbers, since symmetric matrix in complex-valued domain has no many useful properties.

# Properties of Symmetric Matrices

If $A\in\mathbb{R}^{n\times n}$ and $A^T=A$,

- The eigenvalues of $A$ are all real values.
- The eigenvectors pertaining to distinct eigenvalues are orthogonal.
- $A$ can be diagonalized.


# Appendix

## Appendix 1: Why A Symmetric Matrix Is Diagonalizable?

Consider $A\in\mathbb{R}^{n\times n}$ and $A^T=A$. We have 

$$Av=\lambda v,$$

where $\lambda$ and $v$ are respectively eigenvalue and the corresponding eigenvector.

Since $A$ is symmetric, we take conjugate transpose on both sides

$$\bar{v}^TA=\bar{\lambda}\bar{v}^T.$$

Multiply both sides $v$, we have

$$\bar{v}^TAv=\bar{\lambda}\bar{v}^Tv=\lambda\bar{v}^Tv,$$

results in $\bar{lambda}=\lambda$, showing that each eigenvalue of a symmetric matrix is real-valued.

Further we can prove that the eigenvectors corresponding to different eigenvalues are orthogonal. If the eigenvectors are put in a matrix, e.g.

$$P=[v_1,v_2,\dots,v_n].$$

Note that the eigenvalues are not necessarily distinct. We can find such a $P$ that $P$ is invertible. With an auxiliary variable $D=\text{diag}(\lambda_1,\lambda_2,\dots,\lambda_n)$, we have a more compact form

$$AP=DP,$$

resulting in

$$D=P^{-1}AP.$$

In the other words, a symmetric matrix must be 