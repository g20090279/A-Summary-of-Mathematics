- Topics: Subspaces, Column Space, Null Space
- Last Revised: Sep. 18, 2023

---

A subspace turns out to be exactly the same thing as a span, except we don’t have a particular set of spanning vectors in mind. This change in perspective is quite useful, as it is easy to produce subspaces that are not obviously spans.

# Definition (in $\mathbb{R}^n$)

A ***subspace*** of $\mathbb{R}^n$ i a subset $V$ of $\mathbb{R}^n$ satisfying:

1. ***Non-emptiness***: The zero vector is in $V$.
2. ***Closure under addition***: If $u$ and $v$ are in $V$, then $u+v$ is also in $V$. (A subspace contains the span of any vectors in it.)
3. ***Closure under scalar multiplication***: If $v$ is in $V$ and $c$ is in $\mathbb{R}$, then $cv$ is also in $V$. (The lne through any nonzero vector in $V$ is also contained in $V$.)

# Properties

- The set $\mathbb{R}^n$ is a subspace of itself.
- The set $\{0\}$ is a subspace of $\mathbb{R}^n$.

# Common Types of Subspaces

## Spans are Subspaces and Subspaces are Spans.

## Column Space and Null Space Are Two Natural Subspaces of A Matrix

The **column space** of a matrix $A\in\mathbb{R}^{m\times n}$ is the subspace of $\mathbb{R}^m$ spanned by the columns of $A$, written as $\text{Col}(A)$.

# Subsets versus Subspaces

Te subset is not necessarily a subspace. A subspace is a subset that happens to satisfy the three additional defining properties. For example, the subset unit circle

$$C=\{(x,y)\in\mathbb{R}^n\ |\ x^2+y^2=1\}$$

is not a subspace, since it meets none of te three defining properties of the subspaces.