[Singularity] [Nonsingularity]

A matrix is *nonsingular* if it produces the output 0 only for the input 0. Otherwise, it is *singular*.

- If $A\in M_{m,n}(\mathbb{F})$ and $m<n$, $A$ is necessarily singular.
- For a square matrix $A\in M_n(\mathbb{F})$, the following are equivalents (Horn, 2013)
  - $A$ is nonsingular.
  - $A$ is invertible, i.e. $A^{-1}$ exists.
  - $\mathrm{rank} A=n$.
  - The rows of $A$ are linearly independent.
  - The columns of $A$ are linearly independent.
  - $\det A\neq0$.
  
# References

- Horn R. A. & Johnson C. R. (2013). *Matrix analysis* (2nd ed.). Cambridge University Press.