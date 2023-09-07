- Key words: adjugate, adjugate matrix, classical adjoint, 伴随矩阵
- Last revised: Mar. 24, 2023

---

# Defition of Adjugate

> **Definition.** Consider a $n$-by-$n$ square matrix A. The *adjugate* of $A$ is the transpose of the cofactor matrix $\mathbf{C}$ of $A$,
> $$\mathrm{adj}(A)=\mathbf{C}^T.$$

Therefore, the size of $\mathrm{adj}(A)$ is also $n$-by-$n$.

# Adjugate From Laplace Expansion

The adjugate comes fom the Laplace Expansion of a determinant so that the product of $A$ and its adjugate yields a diagonal matrix whose digonal elements are the determinant of $A$,

$$\boxed{A\cdot\mathrm{adj}(A)=\mathrm{adj}(A)\cdot A=\det(A)I}$$

where $I$ is the identity matrix.

Let's have a review of Laplace Expansion of a determinant of a $n$-by-$n$ square matrix $A$. If we expand with repect to the $i$-th row, we have

$$\det(A)=\sum_{j=1}^{n}(-1)^{i+j}a_{i,j}\det(A_{i,j})=\sum_{j=1}^{n}a_{i,j}C_{i,j}=\boldsymbol{a}_i^T\mathbf{C}_{i},$$

where $\boldsymbol{a}_i=[a_{i,1},\cdots,a_{i,n}]^T$ and $\mathbf{C}_{i}=[C_{i,1},\cdots,C_{i,n}]^T$ are both vectors.

For a cofactor matrix $\mathbf{C}$, where the $i$-th row and $j$-th column element is $\left[\mathbf{C}\right]_{i,j}=C_{i,j}$, the adjugate of $A$ is

$$\left[\mathrm{adj}(A)\right]_{i,j}=C_{j,i}$$