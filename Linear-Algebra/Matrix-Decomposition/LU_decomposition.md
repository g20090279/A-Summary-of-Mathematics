- Topic: LU Decomposition
- Last revised: 19.12.2022

---

# Introduction

Linear systems with form $A\boldsymbol{x}=\boldsymbol{b}$ are widely used model. Many matrix decompositions are exploited to accelerate the computation of the solution of such linear systems. The benchmark algorithm Gaussian elimination is the most efficient and accurate way to solve a linear system. However, if we need to solve serval different systems with large $A$, we would like to avoid repeating the steps of Gaussian elimination on $A$ for every different $\boldsymbol{b}$. This can be accomplished by the *LU decomposition*, which in effect records the steps of Gaussian elimination.

# Find LU decomposition

The LU decomposition is not unique. However, there is a unique LU decomposition in which the $L$ matrix has ones on the diagonal. This $L$ is called *lower unit triangular matrix*. To find the LU decomposition, we'll create two sequences of matrices $L_0,L_1,\cdots$ and $U_0,U_1,\cdots$ such that at each step $$