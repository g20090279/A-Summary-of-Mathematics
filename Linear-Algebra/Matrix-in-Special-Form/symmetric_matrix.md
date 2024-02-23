- Topics: Symmetric Matrix
- Last Revised: Oct. 05, 2023

---

# Definition of Symmetry of a Matrix 


A matrix $A$ is said to be symmetric if $A^T=A$. 

We only consider matrix in *real numbers* when we talk about symmetry, while we prefer to study *hermitian* matrix in complex numbers, since symmetric matrix in complex-valued domain has no many useful properties.

# Properties of Symmetric Matrices

If $A\in\mathbb{R}^{n\times n}$ and $A^T=A$, the following statements are true:

- The eigenvalues of $A$ are all real values (*Proof 1*).
- The eigenvectors pertaining to distinct eigenvalues are orthogonal.
- **(Spectral Theorem)** Every symmetric matrix $A$ has an orthonormal eigenbasis, which means $A$ can be diagonalized.
- A symmetric positive definite matrix has a unique symmetric positive square root.
  
  Since $A$ is symmetric, A can be diagonalized to $A=QDQ^T$, where $Q$ is orthogonal and $D$ is a diagonal matrix. Since $A$ is positive definite matrix, the diagonal matrix in $D$ are all positive. The square root of $A$ is the $A^{1/2}$ which satisfies $A^{1/2}A^{1/2}=A$, giving that $A^{1/2}=QD^{1/2}Q^T$, since $A^{1/2}A^{1/2}=QD^{1/2}Q^TQD^{1/2}Q^T=QDQ^T=A$.

- The sum of two symmetric matrices is symmetric.

# Proof

## Proof 1

Asume $Av=\lambda v$ and $Aw=\mu w$. If $\lambda\neq\mu$, the the relation $\lambda\langle v,w\rangle=\langle\lambda v,w\rangle=\langle Av,w\rangle=\langle v,A^Tw\rangle=\langle v,\mu w\rangle=\mu\langle v,w\rangle$ is only possible if $\langle vw\rangle=0.\quad\square$

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