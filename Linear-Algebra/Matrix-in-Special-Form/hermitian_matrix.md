- Topic: Hermitian Matrix
- Last revised: Mar. 24, 2023

---

# Definition

A square matrix $A\in\mathbb{C}^{n\times n}$ is Hermitian if

$$(A^*)^T=A.$$

The Hermitian matrix of $A$ is denoted as $A^H=(A^*)^T$.

# Properties

## A Special of Hermitian Matrix

One way to generate Hermitian matrix is to firstly generate a random tall matrix $M$, and then to generate a Hermitian matrix $A=M^HM$ (or $A=MM^H$ where $M is a fat matrix$). This can make sure that $A$ has full rank. Otherwise, we don't need to care $A=M^HM$ or $A+MM^H$.

In this case, $A$ has some special properties. If we decompose $M$ by SVD, the singular values, we have $M=U\Sigma V^H$. Then,

$$A=M^HM=V\Sigma U^HU\Sigma V^H=V\Sigma^2V^H.$$

This means that all the eigenvalues of $A$ are nonnegative. Note that a Hermitian matrix with nonnegative eigenvalues is called a positive semidefinite matrix.

Furthermore, $A$ to the power of one half is

$$A^{1/2}=V\Sigma V^H,$$

since $A^{1/2}A^{1/2}=A$. We can further observe that $A^{1/2}$ is also Hermitian.