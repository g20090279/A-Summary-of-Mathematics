- Topic: $\det X$, $\ln\det X$ and $\ln\det X^TX$
- Last revised: Jan 25, 2023

---

# Log-Determinant Function and Properties

For a *telecommunication engineer*, we need to comput the log-determinant to obtain the capactiy of the channel. The log-determinant a matrix $X$ is denoted as. $\ln\det X$.

In general, $X$ can be any square nonzero complex-value matrix, since the $w$ and $z$ of the complex logarithm $w=\ln(z)$ are defined as any nonzero complex number (Churchill, 2014, Sec. 31). However, the $X$ in the capacity is usually a positive-difnite Hermitian matrix, e.g., $X=I+HQH^H$.

> Note: a hermitian matrix $X$ that satisfy $a^HXa\geq0$ for all $a\in\mathbb{C}^n$ is said to be positive-semidefinite

First of all, the covariance matrix $Q$ is always positive semi-definite. It is easy to prove. The covariance matrix $Q$ is defined as $Q=\mathbb{E}\left[(\boldsymbol{s}-\bar{\boldsymbol{s}})(\boldsymbol{s}-\bar{\boldsymbol{s}})^H\right]$, where $\bar{\boldsymbol{s}}$ is the expectation of the random signal vector $\boldsymbol{s}$. With any complex-value vector $\boldsymbol{a}$, we have

$$\begin{aligned}
   \boldsymbol{a}^HQ\boldsymbol{a}&=\mathbb{E}\left[\boldsymbol{a}^H(\boldsymbol{s}-\bar{\boldsymbol{s}})(\boldsymbol{s}-\bar{\boldsymbol{s}})^H\boldsymbol{a}\right]\\
   &=\mathbb{E}\left[\left((\boldsymbol{s}-\bar{\boldsymbol{s}})^H\boldsymbol{a}\right)^H\left((\boldsymbol{s}-\bar{\boldsymbol{s}})^H\boldsymbol{a}\right)\right]\geq0.
\end{aligned}$$

Secondly, the overall combined channel ($HQH^H$) can always be decomposed by SVD, and the signular values should be all nonnegative, since a channel with negative gain (negative singular value) has no physical meaning. Therefore, with $I$, $X$ should be positive-definite matrix.

- $X$ has to be *square* because only square matrix has determinant.
- $X$ has to be *positive definite*.
  - $\det X=\prod_i\lambda_i$.
  - All eigenvalues of positive-definite matrix are positive.
  - $\log$ can be treated as natural logarithm instead of complex logarithm.
  - $\log\det$ is a concave function.
  - $\frac{\partial\log\det X}{\partial X}=X^{-T}$.



# References

Brown, J. W. & Churchill, R. V., (2014). Complex variables and applications, 9 Edition. McGraw-Hill Education.