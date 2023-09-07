- Key words: Definite, Semidefinite, Positive (Semi-)Definite, Negative (Semi-)Definite
- Last revised: Jan 25, 2023

---

# Summary



# Positive Definite Matrix

For a *hermitian* matrix $A\in\mathbb{C}^{n\times n}$ in a quadratic form

$$q(x)=x^HAx,$$

where $q(\cdot)$ is a function $q:\mathbb{C}^n\rightarrow\mathbb{R}$ and $x\in\mathbb{C}^n$. $A$ is said to be *positive definite* (PD) if and only if $q$ is nonnegative everywhere:

$$q(x)>0\quad\forall x\in\mathbb{C}^n.$$

A PSD matrix $A$ can be denoted as $A\succ0.$ $\square$

## Properties

If $A,B\succ0$ and $t>0$

- $A+B\succ0$ and $tA\succeq0$.
- The eigenvalues $\lambda_i>0$ (Proof, pdm-p2).
- $\text{Tr}(A)>0$ and $\det(A)>0$.
- $[A]_{i,i}>0$.


# Proof

## pdm-p2

Assume $\lambda$ is an eigenvalue of a PD matrix $A\in\mathbb{C}^{n\times n}$. For any vector $x\in\mathbb{C}^{n}$, we have $\lambda x=Ax$. Then, with the definite of positive definite, we have

$$x^H(\lambda x)=\lambda\|x\|_2^2=x^HAx>0,$$

resulting in $\lambda>0$.