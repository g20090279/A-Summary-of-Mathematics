[minor] [子式] [余子式]

# Definition of Minor

In general, a minor is a determinant of a submatrix of a matrix. According to different scenarios, we have two definitions for minor.

> **Definition 1.** For an $m$-by-$n$ matrix $A$ and a scalar $r\leq\min(m,n)$, if we choose any $r$ rows and any $r$ columns, the $r$-by-$r$ intersecting elements forms a new matrix $B$, which is a submatrix from $A$. The determinant of $B$ is called a *minor* (*子式*). $r$ is also called the order of the minor. (Horn, 2013, P17)

In this case, there can be $\binom{m}{r}\times\binom{n}{r}$ $r$-th order minors.

> **Definition 2.** For an $m$-by-$m$ sqaure matrix $A$, a *minor* (*余子式*) $M_{i,j}$ is the determinant of a submatrix of $A$, $A_{i,j}$, by deleting the $i$-th row and $j$-th column, i.e.
> $$M_{i,j}=\det\left(A_{i,j}\right).$$

Therefore, a minor has such properties:
- a minor is a scalar,
- a minor is a determinant of a square submatrix.

# References

Horn, R. A., & Johnson, C. R. (2013). *Matrix Analysis (2nd ed.)*. Cambridge University Press.