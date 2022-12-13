- Keywords: positive semidefinite matrix, positive definite matrix
- Update: Mar. 03, 2022

---

# Definition

Consider a square matrix $A\in\mathbf{R}^{n\times n}$ in a quadratic form

$$q(x)=x^TAx,$$

where $q(x)$ is a function $q:\mathbf{R}^n\rightarrow\mathbf{R}$ and $x\in\mathbf{R}^n$. $A$ is said to be *positive semidefinite* (PSD) if and only if $q$ is nonnegative everywhere:

$$q(x)\geq0\quad\forall x\in\mathbf{R}^n.$$

A PSD matrix $A$ can be denoted as

$$A\succeq0.$$

Note that the definition of many literatures is restricted to be a symmetric matrix, since there are many nice properties. But a PSD matrix is not necessary to be symmetric. One example that a asymmetric matrix is PSD is $\begin{bmatrix}
   2 & 0\\ 2 & 2 
\end{bmatrix}$.

Furthermore, it is said to be *positive definite* (PD, notation: $A\succ0$) if $q$ is positive, i.e., $q(x)>0$.

# Verifying a positive semidefinite matrix

To check if a matrix PSD, we can not use the definition since we can not find all $x$ to see if we have a nonnegative $q(x)$. Don't worry, there are many methods to verify the PSD property.

## Method 1: Eigenvalues are nonnegative

**Theorem.** The eigenvalues of a PSD matrix are all nonnegative.

**Proof**. It is easy to prove by using the definition. For a eigenvalue $\lambda\in\mathbb{R}$ of $A\in\mathbb{R}^{n\times n}$, and a corresponding eigenvector $x\in\mathbb{R}^{n}$, we have

$$Ax=\lambda x.$$

Multiply $x^T$ on the both sides, the equality becomes

$$x^TAx=x^T\lambda x=\lambda\|x\|_2.$$

According to the definition, if $A$ is PSD, the left-hand side is nonnegative. Since the norm (L2, or called Euclidean norm) of $x$ is nonnegative as well, the eigenvalue $\lambda$ must be nonnegative. $\blacksquare$

Therefore, we just need to find all the eigenvalues for the matrix, and check if all of them are nonnegative.

## Method 2: Sylvester's criterion for symmetric / Hermitian matrix

Since we are taking about the field of real number here, we consider only symmetric matrices (Hermitian matrix for complex numbers). 
