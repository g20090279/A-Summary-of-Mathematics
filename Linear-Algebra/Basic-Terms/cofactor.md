- Key words: cofactor, 代数余子式, cofactor matrix, matrix of cofactor, 余因子矩阵
- Last revised: Mar. 24, 2023

---

# Definition of Cofactor

The definition of *cofactor* (*代数余子式*) comes from Laplace Expansion. A cofactor is a signed minor.

> **Definition.** Consider an $m$-by-$n$ matrix $A$. $A_{i,j}$ is the submatrix of $A$ by deleting $i$-th row and $j$-th Column. $M_{i,j}$ is the corresponding minor, i.e., the determinant of $A_{i,j}$. The *cofactor* (*代数余子式*) is (Horn, 2013, P17)
> $$C_{i,j}=(-1)^{i+j}M_{i,j}.$$

If the minor has size $r$, we call that the cofactor of size $r$.

# Definition of Cofactor Matrix

> **Definition.** For a $m$-by-$m$ square matrix $A$, put the cofactor $C_{i,j}$ in the $i$-th row and $j$-th column of a matrix. Such a matrix $\mathbf{C}$
> $$\mathbf{C}=\begin{bmatrix}
   C_{1,1}&C_{1,2}&\cdots&C_{1,m}\\
   C_{2,1}&C_{2,2}&\cdots&C_{2,m}\\
   \vdots&\vdots&\ddots&\vdots\\
   C_{m,1}&C_{m,2}&\cdots&C_{m,m}.
\end{bmatrix}$$
> is called *cofactor matrix* (*余因子矩阵*).

# References

Horn, R. A., & Johnson, C. R. (2013). *Matrix Analysis (2nd ed.)*. Cambridge University Press.