- Topic: The QR Decomposition of a Matrix
- Last revised: 16.12.2022
- (Copied from UCBerkeley)

---

> - Basic Idea
> - Case 1: $A$ has full column rank 
>   - Prof of the uniqueness of QR decomposition
>   - Matlab syntax
>   - Example: QR decomposition of a 4x6 matrix
> - General case
> - Full QR decomposition

# Basic Idea

The basic goal of the QR decomposition is to factor a matrix as a product of two matrices (traditionally called $Q$, $R$, hence the name of this factorization). Each matrix has a simple structure which can be further exploited in dealing with, say, linear equations. To solve a linear system

$$Ax=b,$$

we need to obtain the inverse of $A$, i.e., $x=A^{-1}b$, which is computationally demanding. If we can decompose $A=QR$, which makes the equation be $QRx=b$, we can further transform it to $Rx=Q^Tb$, where $Q$ is an orthogonal matrix, so that we can avoid matrix inversion. The upper triangular matrix $R$ enable *back-substitution operation* to finally calculate $x$.

The QR decomposition is nothing else than the *Gram-Schmidt orthogonalization process* applied to the columns of the matrix, and with the result expressed in matrix form. In this sense, *QR decomposition of any matrix always exists*. It is relatively easy to code up QR decomposition based on Gram-Schmidt process. However, the QR algorithm using Gram-Schmidt process can become unstable and hence there are a couple of other more stable algorithms exploited and being used in cases in practice, such as *Givens Rotation*, *Householder reflection* and so on.

Consider a $m \times n$ matrix $A = [\boldsymbol{a}_1,\cdots,\boldsymbol{a}_n]$, with each $\boldsymbol{a}_i\in\mathbb{R}^m$ a column of $A$. Note that the QR decomposition is introduced to a real matrix in the following context. It can also be applied to a complex-number matrix. The only difference in the expression is that the $Q$ is a unitary matrix, i.e., $Q^HQ=I$, where $Q^H$ is the conjugate transpose of $Q$.

# Case 1: Full column rank $m\ge n$

Assume first that the $\boldsymbol{a}_i$'s (the columns of $A$) are linearly independent. Each step of the G-S process can be written as

$$\boldsymbol{a}_i = (\boldsymbol{a}_i^T\boldsymbol{q}_1)\boldsymbol{q}_1+ \cdots + (\boldsymbol{a}_{i}^T\boldsymbol{q}_{i-1})\boldsymbol{q}_{i-1} + \|\tilde{\boldsymbol{q}}_i\|_2 \boldsymbol{q}_i,\quad i=1,\cdots,n.$$

(Review from Gram-Schmidt orthogonalization process: $\tilde{\boldsymbol{q}} = \boldsymbol{a}_i - \sum_{j=1}^r (\boldsymbol{a}_j^T\boldsymbol{a}_i)\boldsymbol{q}_j$)

We write this as

$$\boldsymbol{a}_i = r_{i,1}\boldsymbol{q}_1+ \cdots + r_{i,i-1}\boldsymbol{q}_{i-1} + r_{i,i} \boldsymbol{q}_i,\quad i=1,\cdots,n,$$

where $r_{i,j} = (\boldsymbol{a}_i^T\boldsymbol{q}_j),\quad (1\le j\le i-1)$ and $r_{i,i} = \|\tilde{\boldsymbol{q}}_{i,i}\|_2$.

Since the $\boldsymbol{q}_i$'s are unit-length and normalized, the matrix $Q = (\boldsymbol{q}_1,\cdots,\boldsymbol{q}_n)$ satisfies $Q^TQ = I_n$. The QR decomposition of a $m \times n$ matrix $A$ thus allows to write the matrix in factored form:

$$A = QR, \quad Q = \begin{bmatrix} \boldsymbol{q}_1 & \cdots & \boldsymbol{q}_n \end{bmatrix} , \quad R = \begin{bmatrix} r_{11} & r_{12} & \cdots & r_{1n} \\ 0 & r_{22} & & r_{2n} \\ \vdots & & \ddots & \vdots \\ 0 & & 0 & r_{nn} \end{bmatrix}$$

where $Q$ is a $m \times n$ matrix with $Q^TQ = I_n$, and $R$ is $n \times n$, upper-triangular. Since $Q$ is not square but a tall matrix, this form of decomposition is called *Reduced QR Decomposition*. The columns of $Q$ form an orthonormal basis for he column space of $A$.

There is another form of decomposition, *Full QR Decomposition*, where $Q$ is square and $R$ is tall

$$[\boldsymbol{q}_1,\cdots,\boldsymbol{q}_n,\boldsymbol{q}_{n+1},\cdots,\boldsymbol{q}_m]_{m\times m}\begin{bmatrix}
   r_11 & \cdots & r_{1n}\\
   0 & \ddots & \vdots\\
   0 & 0 & r_{nn}\\
   0 & \cdots & 0\\
   \vdots & \ddots & \vdots\\
   0 & \cdots & 0 
\end{bmatrix}_{m\times n}=A.$$

The $m$ columns of $Q$ form an orthonormal basis for all $\mathbb{F}^{m}$.

## Matlab syntax

```matlab
>> [Q,R] = qr(A,0); % A is a mxn matrix, Q is mxn orthogonal, R is nxn upper triangular
```

## Example: QR decomposition of a $6\times4$ matrix

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

# Case 2: Rank-deficient matrix

Consider $r = \text{\bf{Rank}}(A)$ with $r\le\min(m,n)$. We can obtain $A = QR$, with $Q \in \mathbb{R}^{m \times r}$ and $R\in\mathbb{R}^{r\times n}$. This is the reduced form of QR decomposition. Similarly, the rank-deficient matrix $A$ can also be docomposed into $A=QR$ with $Q\in\mathbb{R}^{m\times m}$ and $R\in\mathbb{R}^{m\times n}$. The last $m-r$ rows of $R$ are zeros. 

## Matlab syntax

```matlab
>> % generate rank-deficient matrix with rank r
>> m = 7;
>> n = 5;
>> r = 3;

>> A = rand(m,n);

>> [U,S,V] = eig(A);

>> % create rank-deficient matrix
>> B = U(:,1:r)*S(1:r,:)*V(:,1:r)';

>> [Q,R] = qr(B,0);

>> C = Q(:,1:r)*R(1:r,:); % C = B
```

# Other approaches

The above introduction of QR decomposition is based on Gram-Schmidt orthogonalization process. However, the more common approach to QR decomposition is employing Household reflections rather than utilizing Gram-Schmidt process.

# Notes

## Note 1: How Unique is QR?

Here we consider only the special case of full rank.

### Square matrix, $m=n$

Assume $A=Q_1R_1=Q_2R_2$. Left-multiplying $Q_2^T$ and right-multiplying $R_1^{-1}$ yields

$$Q_2^TQ_1R_1R_1^{-1}=Q_2^TQ_2R_2R_1^{-1}.$$

The left-hand side becomes $Q_2^TQ_1$. The multiplication of two unitary matrices is still unitary. The right-hand side is $R_2R_1^{-1}$. For the right-hand side, an inverse upper triangular matrix, $R_1^{-1}$, is still upper triangular. Moreover, the product of two upper triangular matrices $R_2R_1^{-1}$ is also upper triangular matrix. Therefore, $Q_2^TQ_1$ is both a upper triangular unitary matrix and a unitary matrix, which can only be an identity matrix whose diagonal entries are all positive or negative one. Hence, $Q_2^TQ_1=\pm I$. If we require the diagonal entries of $R$ to be positive, $Q_1=Q_2$, indicating that QR decomposition is unique.

### Underdetermined matrix, $m<n$

If $A=Q_1[R_1,N_1]=Q_2[R_2,N_2]$ are two QR decompositions of a full rank, $m\times n$ matrix $A$ with $m<n$, where $Q_1,Q_2\in\mathbb{C}^{m\times m}$, $R_1,R_2\in\mathbb{C}^{m\times n}$ and $N_1,N_2\in\mathbb{C}^{m\times(n-m)}$, then similarly, there exists a square diagonal matrix $S$ fulfilling that 

$$Q_2=Q_1S,\quad R_2=SR_1,\quad N_2=SN_1.$$

If we constrain the diagonal entries of $R$ to be positive, the decomposition is unique.

### Overdetermined matrix, $m>n$

If $A=[Q_1,U_1]\begin{bmatrix}R_1 \\0\end{bmatrix}=[Q_2,U_2]\begin{bmatrix}R_2\\0\end{bmatrix}$ are two QR decompositions of a full rank, $m\times n$ matrix $A$ with $m>n$, then

$$Q_2=Q_1S,\quad R_2=SR_1,\quad U_2=U_1T,$$

for some square diagonal matrix $S$ with entries $\pm1$ and square orthogonal $T$. If we require the diagonal entries of R to be positive, then $Q$ and $R$ are unique.

## Note 2: QR decomposition of a unitary matrix

**Proposition 1**: Consider $A$ is a $n\times n$ unitary square matrix, i.e. $A^HA=AA^H=I$. Decompose $A$ into a unitary matrix $Q$ and a upper triangular matrix $R$

$$A=QR,$$

where $R=\textbf{diag}\left(e^{j\theta_1},\cdots,e^{j\theta_n}\right)$.

**Proof**. Since $Q$ is an unitary matrix, we have $R=Q^HA$. Then, $R^HR=A^HQQ^HA=A^HA=I$. Since $R$ now is a unitary matrix as well as an upper triangular matrix, it is thus a diagonal matrix (not necessary an identity matrix). Since $R^HR=I$, the power of each diagonal entry is 1. We can then model $R=\textbf{diag}\left(\left[e^{j\theta_1},\cdots,e^{j\theta_n}\right]\right)$.