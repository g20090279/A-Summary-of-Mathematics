[Eigenvalue] [特征值] [Eigenvector] [特征向量]

# What are "Eigenvalue" and "Eigenvector"

What we are talking about here is the matrix, which can be seen as a linear transformation of a vector from one dimension to another dimension. According to the definition in Horn's book "Matrix Analysis" (Horn, 2013), the eigenvalue and eigenvector are limited in complex number field, while the matrix can be any matrix space in any field. The definition of a field can be referred to the chapter "0.1 Vector spaces" in the book.

**Definition**. Let $\mathbf{A}\in \mathbf{M}_n$, i.e. a square matrix space of any field. If a scalar $\lambda$ and a nonzero vector $\boldsymbol{x}$ satisfy the equation

$$\mathbf{A}\boldsymbol{x}=\lambda\boldsymbol{x},\quad\boldsymbol{x}\in\mathbb{C}^n,\boldsymbol{x}\neq0,\lambda\in\mathbb{C}$$

we called $\lambda$ an eigenvalue of $\mathbf{A}$ and $\boldsymbol{x}$ is an eigenvector of $\mathbf{A}$ associated with $\lambda$. The pair $\lambda,\boldsymbol{x}$ is an eigenpair of $\mathbf{A}$. $\square$

# Properties on Special Types of Matrix

- *Symmetric (for real) / Hermitian (for complex) Matrices*: The eigenvalues and eigenvectors of real symmetric matrices or complex Hermitian matrices are real.
  **Proof**. Assume $\lambda$ and $\boldsymbol{v}$ are the eigenpair of a symmetric matrix $\mathbf{A}=\mathbf{A}^T$, and $\boldsymbol{v}^H$, we have
  
  $$\boldsymbol{v}^H\mathbf{A}\boldsymbol{v}=\lambda\boldsymbol{v}^H\boldsymbol{v}.$$

  The left-hand side can be rewritten as

  $$\boldsymbol{v}^H\mathbf{A}\boldsymbol{v}=(\mathbf{A}\boldsymbol{v})^H\boldsymbol{v}=\bar{\lambda}\boldsymbol{v}^H\boldsymbol{v}$$.

  Therefore, we have

  $$\bar{\lambda}=\lambda,$$

  showing that $\lambda$ is real. $\square$

# References

- Horn R. A. & Johnson C. R. (2013). *Matrix analysis* (2nd ed.). Cambridge University Press.