# The QR Decomposition of a Matrix

(copied from UCBerkeley)

> - Basic idea
> - Case when the matrix has linearly independent columns 
> - General case
> - Full QR decomposition

## Basic idea

The basic goal of the QR decomposition is to factor a matrix as a product of two matrices (traditionally called Q,R, hence the name of this factorization). Each matrix has a simple structure which can be further exploited in dealing with, say, linear equations.

The QR decomposition is nothing else than the **Gram-Schmidt orthogonalization process** applied to the columns of the matrix, and with the result expressed in matrix form. It is relatively easy to code up QR decomposition based on Gram-Schmidt process. However, the QR algorithm using Gram-Schmidt process can become unstable and hence there are a couple of other more stable algorithms exploited and being used in cases in practice, such as **Givens Rotation**, **Householder reflection** and so on.

Consider a $m \times n$ matrix $A = (a_1,\cdots,a_n)$, with each $a_i\in\mathbf{R}^m$ a column of $A$.

## Case when $A$ is full column rank

Assume first that the $a_i$'s (the columns of $A$) are linearly independent. Each step of the G-S process can be written as

$$a_i = (a_i^Tq_1)q_1+ \cdots + (a_{i}^Tq_{i-1})q_{i-1} + \|\tilde{q}_i\|_2 q_i,\quad i=1,\cdots,n.$$

(Review from Gram-Schmidt orthogonalization process: $\tilde{q} = a_i - \sum_{j=1}^r (q_j^Ta_i)q_j$)

We write this as

$$a_i = r_{i,1}q_1+ \cdots + r_{i,i-1}q_{i-1} + r_{i,i} q_i,\quad i=1,\cdots,n,$$

where $r_{i,j} = (a_i^Tq_j),\quad (1\le j\le i-1)$ and $r_{i,i} = \|\tilde{q}_{i,i}\|_2$.

Since the $q_i$'s are unit-length and normalized, the matrix $Q = (q_1,\cdots,q_n)$ satisfies $Q^TQ = I_n$. The QR decomposition of a $m \times n$ matrix $A$ thus allows to write the matrix in factored form:

$$A = QR, \quad Q = \begin{bmatrix} q_1 & \cdots & q_n \end{bmatrix} , \quad R = \begin{bmatrix} r_{11} & r_{12} & \cdots & r_{1n} \\ 0 & r_{22} & & r_{2n} \\ \vdots & & \ddots & \vdots \\ 0 & & 0 & r_{nn} \end{bmatrix}$$

where $Q$ is a $m \times n$ matrix with $Q^TQ = I_n$, and $R$ is $n \times n$, upper-triangular.

**Matlab syntax**

```matlab
>> [Q,R] = qr(A,0); % A is a mxn matrix, Q is mxn orthogonal, R is nxn upper triangular
```

**Example**: QR decomposition of a 4x6 matrix

$$A = \begin{bmatrix} 0.488894&0.888396&0.325191&0.319207 \\ 1.03469&-1.14707&-0.754928&0.312859 \\ 0.726885&-1.06887&1.3703&-0.86488 \\ -0.303441&-0.809499&-1.71152&-0.0300513 \\ 0.293871&-2.94428&-0.102242&-0.164879 \\ -0.787283&1.43838&-0.241447&0.627707 \end{bmatrix}.$$

This matrix is full column rank. Indeed, the matlab command 

```matlab
[Q,R]=qr(A,0)
```

yields a $6 \times 4$ $Q$ and a $4 \times 4$ $R$:

$$A=QR$$

$$Q = \begin{bmatrix} 0.301109&0.460748&-0.0940935&0.24499 \\ 0.637266&0.0433642&-0.558601&0.251199 \\ 0.447688&-0.0504968&0.519798&-0.41105 \\ -0.186889&-0.365412&-0.617955&-0.489793 \\ 0.180995&-0.79363&0.163942&0.492111 \\ -0.484886&0.141088&-0.0132838&0.475232 \end{bmatrix}$$

$$R = \begin{bmatrix} 1.62364&-2.02107&0.648726&-0.420299 \\ 0&3.24897&0.720385&0.434711 \\ 0&0&2.14747&-0.67116 \\ 0&0&0&0.744188 \end{bmatrix}$$

This shows that $A$ is full column rank since $R$ is invertible.

The command

```matlab
[Q,R]=qr(A)
```

actually produces the full QR decomposition, with $Q$ now a $6 \times 6$ orthogonal matrix:

$$Q = \begin{bmatrix} 0.301109&0.460748&-0.0940935&0.24499&0.692493&-0.385519 \\ 0.637266&0.0433642&-0.558601&0.251199&-0.253083&0.390928 \\ 0.447688&-0.0504968&0.519798&-0.41105&0.332021&0.49763 \\ -0.186889&-0.365412&-0.617955&-0.489793&0.452645&0.0699514 \\ 0.180995&-0.79363&0.163942&0.492111&0.213643&-0.15066 \\ -0.484886&0.141088&-0.0132838&0.475232&0.309248&0.650633 \end{bmatrix},$$

$$R = \begin{bmatrix} 1.62364&-2.02107&0.648726&-0.420299 \\ 0&3.24897&0.720385&0.434711 \\ 0&0&2.14747&-0.67116 \\ 0&0&0&0.744188 \\ 0&0&0&0 \\ 0&0&0&0 \end{bmatrix}.$$

We can see what happens when the input is not full column rank: for example let's consider the matrix

$$A = \begin{bmatrix} 1.09327&1.10927&-0.863653&1.32288 \\ -1.21412&-1.1135&-0.00684933&-2.43508 \\ -0.769666&0.371379&-0.225584&-1.76492 \\ -1.08906&0.0325575&0.552527&-1.6256 \\ 1.54421&0.0859311&-1.49159&1.59683 \end{bmatrix}$$

($A$ is not full column rank, as it was constructed so that the last column is a combination of the first and the third.)

The (full) QR decomposition now yields:

$$R=\begin{bmatrix}2.61388&0.909015&-1.40302&3.82473 \\ 0&1.33807&0.0979073&0.0979073 \\ 0&0&1.16142&1.16142 \\ 0&0&0&0.00000 \\ 0&0&0&0 \end{bmatrix}$$

We observe that the last triangular element is virtually zero, and the last column is seen to be a linear combination of the first and the third. This shows that the rank of $R$ (itself equal to the rank of $A$) is effectively $3$.

## Case when the columns are not independent

When the columns of $A$ are not independent, at some step of the G-S procedure we encounter a zero vector $\tilde{q}_j$, which means $a_{j}$ is a linear combination of $a_{j-1},\cdots,a_1$. The modified Gram-Schmidt procedure then simply skips to the next vector and continues.

In matrix form, we obtain $A = QR$, with $Q \in \mathbf{R}^{m \times r}$, $r = \text{\bf{Rank}}(A)$, and $R$ has an upper staircase form, for example:

$$R = \begin{bmatrix} \ast & \ast & \ast & \ast & \ast & \ast \\ 0 & 0 & \ast & \ast & \ast & \ast \\ 0 & 0 & 0 & 0 & \ast & \ast \end{bmatrix}.$$

(This is simply an upper triangular matrix with some rows deleted. It is still upper triangular.)

We can permute the columns of R to bring forward the first non-zero elements in each row:

$$R = \begin{bmatrix} R_1 & R_2 \end{bmatrix}P^T, \quad \begin{bmatrix} R_1 | R_2\end{bmatrix}:= \left[ \begin{matrix} \ast & \ast & \ast \\ 0 & \ast & 0 \\ 0 & 0 & \ast \end{matrix} \left| \begin{matrix}\ast & \ast & \ast \\ \ast & \ast & \ast \\  0 & 0 & \ast \end{matrix}\right.\right],$$

where $P$ is a permutation matrix (that is, its columns are the unit vectors in some order), whose effect is to permute columns. (Since $P$ is orthogonal, $P^{-1} = P^T$.) Now, $R_1$ is square, upper triangular, and invertible, since none of its diagonal elements is zero.

The QR decomposition can be written

$$AP = Q \begin{bmatrix} R_1 & R_2\end{bmatrix},$$

where

1. $Q \in \mathbf{R}^{m \times r}, Q^TQ=I_r$;
2. $r$ is the rank of $A$;
3. $R_1$ is $r \times r$ upper triangular, invertible matrix;
4. $R_2$ is a $r \times (n -r)$ matrix;
5. $P$ is a $m \times m$ permutation matrix.

**Matlab syntax**

```matlab
>> [Q,R,inds] = qr(A,0);  % here inds is a permutation vector such that A(:,inds) = Q*R
```

## Full QR decomposition

The full QR decomposition allows to write $A = QR$ where $Q in \mathbf{R}^{m \times m}$ is square and orthogonal ($Q^TQ = QQ^T = I_m$). In other words, the columns of $Q$ are an orthonormal basis for the whole output space $\mathbf{R}^m$, not just for the range of $A$.

We obtain the full decomposition by appending an $m \times m$ identity matrix to the columns of $A: A \rightarrow [A,I_m]$. The QR decomposition of the augmented matrix allows to write

$$AP = QR = \begin{bmatrix} Q_1 & Q_2 \end{bmatrix} \begin{bmatrix} R_1 & R_2 \\ 0 & 0 \end{bmatrix},$$

where the columns of the $m \times m$ matrix $Q = [Q_1,Q_2]$ are orthogonal, and $R_1$ is upper triangular and invertible. (As before, $P$ is a permutation matrix.) In the G-S procedure, the columns of $Q_1$ are obtained from those of $A$, while the columns of $Q_2$ come from the extra columns added to $A$.

The full QR decomposition reveals the rank of $A$: we simply look at the elements on the diagonal of $R$ that are not zero, that is, the size of $R_1$.

**Matlab syntax**

```matlab
>> [Q,R] = qr(A); % A is a mxn matrix, Q is mxm orthogonal, R is mxn upper triangular
```