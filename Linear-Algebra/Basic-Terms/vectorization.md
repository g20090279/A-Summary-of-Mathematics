- Key words: vectorization, 向量化

# Definition of Vectorization

> **Definition.** The vectorization of a matrix is to convert a matrix to a vector, usually column-by-column. It is denoted by $\mathrm{vec(\cdot)}$.

For example, consider an $n$-by-$m$ matrix

$$\begin{aligned}A&=\begin{bmatrix}
   a_{11} & a_{12} & \cdots & a_{1m} \\
   a_{21} & a_{22} & \cdots & a_{2m} \\
   \vdots & \vdots & \ddots & \vdots\\
   a_{n1} & a_{n2} & \cdots & a_{nm}
\end{bmatrix}\\
&=[\boldsymbol{a}_1,\boldsymbol{a}_2,\cdots,\boldsymbol{a_m}],\end{aligned}$$

where $\boldsymbol{a}_i$ is the $i$-th column of matrix $A$, the vectorization of $A$ is

> $$\begin{aligned}\boldsymbol{a}&=\mathrm{vec}(A)=\begin{bmatrix}
\boldsymbol{a}_1 \\ \boldsymbol{a}_2 \\ \vdots \\ \boldsymbol{a}_m
\end{bmatrix}\\
&=[a_{11},a_{21},\cdots,a_{n1},a_{12},\cdots,a_{n2},\cdots,a_{1m},\cdots,a_{nm}]^T.\end{aligned}$$

# Properties of Vectorization

## Property 1

Consider two matrices $A$ and $B$ with the same size. $\alpha$ and $\beta$ are two scalars.

> $$\mathrm{vec}(\alpha A+\beta B)=\alpha \mathrm{vec}(A)+\beta\mathrm{vec}(B)\quad (P1)$$

(P1) can be referred to (Trees, 2002, Eq. (A.113)). 

## Property 2

Consider two matrices $A\in\mathbb{C}^{N\times M}$ and $B\in\mathbb{C}^{M\times P}$. The vectorization of the product of $A$ and $B$ can be written alternatively by using Kronecker Product

> $$\begin{aligned}
    \mathrm{vec}(AB)&=(I_P\otimes A)\mathrm{vec}(B),&\quad (P2.a)\\
    \mathrm{vec}(AB)&=(B^T\otimes I_N)\mathrm{vec}(A).&\quad (P2.b)
\end{aligned}$$

(P2.a) can be referred to (Trees, 2002, Eq. (A.115)) and (P2.b) can be referred to (Trees, 2002, Eq. (A.116)).

## Property 3

Consider three matrices $A\in\mathbb{C}^{N\times M}$, $B\in\mathbb{C}^{M\times P}$ and $C\in\mathbb{C}^{P\times Q}$. The vectorization of the product of these three matrices can be represented by using a Kronecker Product in the following form:

> $$\begin{aligned}
    \mathrm{vec}(ABC)&=(C^T\otimes A)\mathrm{vec}(B),&\quad(P3.a)\\
    \mathrm{vec}(ABC)&=(I_Q\otimes AB)\mathrm{vec}(C),&\quad(P3.b)\\
    \mathrm{vec}(ABC)&=(C^TB^T\otimes I_N)\mathrm{vec}(A),&\quad(P3.c)
\end{aligned}$$

(P3.a) can be referred to (Trees, 2002, Eq. (A.114)).

# Proof of The Properties

## Proof of Property 1

## Proof of Property 2

## Proof of Property 3 (P3.a)

Let write the matrices into details,

$$\begin{aligned}
   A&=\begin{bmatrix}
        a_{11} & a_{12} & \cdots & a_{1M}\\
        a_{21} & a_{22} & \cdots & a_{2M}\\
        \vdots & \vdots & \ddots & \vdots\\
        a_{N1} & a_{N2} & \cdots & a_{NM}   
   \end{bmatrix}_{N\times M}\\
   B&=\begin{bmatrix}
        b_{11} & b_{12} & \cdots & b_{1P}\\
        b_{21} & b_{22} & \cdots & b_{2P}\\
        \vdots & \vdots & \ddots & \vdots\\
        b_{M1} & b_{M2} & \cdots & b_{MP}   
   \end{bmatrix}_{M\times P}\\
   C&=\begin{bmatrix}
        c_{11} & c_{12} & \cdots & c_{1P}\\
        c_{21} & c_{22} & \cdots & c_{2P}\\
        \vdots & \vdots & \ddots & \vdots\\
        c_{P1} & c_{P2} & \cdots & c_{PQ}
   \end{bmatrix}_{P\times Q}.
\end{aligned}$$

Then the element at the $i$-th row and $j$-th column of $H$ of the product of $A$ and $B$ is

$$\left[AB\right]_{ij}=\sum_{k=1}^{M}a_{ik}b_{kj}.$$

where $i=1,2,\cdots,N$ and $j=1,2,\cdots,P$. Note that the size of $H$ is $N$ by $P$. We can denote this matrix as $H$ as

$$H=AB=\begin{bmatrix}
     h_{11} & h_{12} & \cdots & h_{1P}\\
     h_{21} & h_{22} & \cdots & h_{2P}\\
     \vdots & \vdots & \ddots & \vdots\\
     h_{N1} & h_{N2} & \cdots & h_{NP} 
\end{bmatrix}_{N\times P}$$

Then the final product of $H$ and $C$ at the $r$-th row and $s$-th column is

$$[HC]_{rs}=\sum_{l=1}^{P}h_{rl}c_{ls},$$

where $r=1,2,\cdots,N$ and $s=1,2,\cdots,Q$. Now we can replace the notation of $h$ with $a$ and $b$, we can have

$$[ABC]_{rs}=\sum_{l=1}^{P}\sum_{k=1}^{M}a_{rk}b_{kl}c_{ls},\quad (1)$$

where $r=1,2,\cdots,N$ and $s=1,2,\cdots,Q$. Finally, if we vectorize the matrix $ABC$ **columnwise**, the $t$-th element of this vector can be also indexed by $r$ and $s$

$$t=(s-1)Q+r,$$

where $t=1,2,\cdots,NQ$, and

$$[\mathrm{vec}(ABC)]_{t}=[ABC]_{rs}.$$

Now we need to study the right-hand side of the equation, to prove that we can have the same expression. First of all, we can look at the Kronecker Product and denote the result as $I$

$$\begin{aligned}I&=C^T\otimes A=\begin{bmatrix}
     c_{11}A & c_{21}A & \cdots & c_{P1}A\\
     c_{12}A & c_{22}A & \cdots & c_{P1}A\\
     \vdots & \vdots & \ddots & \vdots\\
     c_{1Q}A & c_{2Q} & \cdots & c_{PQ}
\end{bmatrix}_{NQ\times MP}\\
&=\begin{bmatrix}
     c_{11}a_{11} & \cdots & c_{11}a_{1M} & \cdots & c_{P1}a_{11} & \cdots & c_{P1}a_{1M}\\
     \vdots & \ddots & \vdots & \ddots & \vdots & \ddots & \vdots\\
     c_{11}a_{N1} & \cdots & c_{11}a_{NM} & \cdots & c_{P1}a_{N1} & \cdots & c_{P1}a_{NM}\\
     \vdots & \ddots & \vdots & \ddots & \vdots & \ddots & \vdots\\
     c_{1Q}a_{11} & \cdots & c_{1Q}a_{1M} & \cdots & c_{PQ}a_{11} & \cdots & c_{PQ}a_{1M}\\
     \vdots & \ddots & \vdots & \ddots & \vdots & \ddots & \vdots\\
     c_{1Q}a_{N1} & \cdots & c_{1Q}a_{NM} & \cdots & c_{PQ}a_{N1} & \cdots & c_{PQ}a_{NM}
\end{bmatrix}_{NQ\times MP}.
\end{aligned}$$

Now we turn to the vectorization of $B$, which results in

$$\mathrm{vec}(B)=\begin{bmatrix}
     b_{11} \\ \vdots \\ b_{M1} \\ \vdots \\ b_{1P} \\ \vdots \\ b_{MP}
\end{bmatrix}_{MP\times 1}.$$

We can see that for the product of $I$ and $A$, $IA=\mathrm{vec}(ABC)$, each element of the vector results from the product of the corresponding row of $I$ and $\mathrm{vec}(B)$. Therefore, each element of $\mathrm{vec}(ABC)$ should be a summation from $1$ to $M$ as well as another summation from $1$ to $P$. We can reuse the indices $r=1,2,\cdots,N$, $s=1,2,\cdots,Q$ and $t=1,2,\cdots,NQ$, the $t$-th element of $\mathrm{vec}(ABC)$ is

$$[\mathrm{vec}(ABC)]_{t}=[(C^T\otimes A)\mathrm{vec}(B)]_t=\sum_{l=1}^{P}\sum_{k=1}^{M}c_{ls}a_{rk}b_{kl},\quad (2)$$

where $t=(s-1)N+r$.

Comparing Eq. (1) and Eq. (2), they are same, and hence the equality (P3.a) is proved.

# References

- Trees, H. L. V. (2002). *Optimum array processing: Part IV of detection, estimation, and modulation theory*. Jhon Wiley & Sons. 
