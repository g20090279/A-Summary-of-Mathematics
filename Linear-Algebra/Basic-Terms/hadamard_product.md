[Hadamard Product] [哈达玛积]

The Hadamard Product is the product of matrices with **same size**. It is denoted as $\circ$ or $\odot$. Here we will use $\circ$ to denote the Hadamard Product.

# Definition of Hadamard Product

Given two matrices $A$ and $B$ with **same size**, $n$ by $m$, 

$$A=\begin{bmatrix}
    a_{11} & \cdots & a_{1m}\\
    \vdots & \ddots & \vdots \\
    a_{n1} & \cdots & a_{nm}
\end{bmatrix}_{n\times m},\quad B=\begin{bmatrix}
    b_{11} & \cdots & b_{1m}\\
    \vdots & \ddots & \vdots\\
    b_{n1} & \cdots & b_{nm}
\end{bmatrix}_{n\times m},$$

the Hadamard Product of $A$ and $B$ is

> $$A\circ B=\begin{bmatrix}
    a_{11}b_{11} & \cdots & a_{1m}b_{1m}\\
    \vdots & \ddots & \vdots\\
    a_{n1}b_{n1} & \cdots & a_{nm}b_{nm}
\end{bmatrix}.$$

Therefore, each element of the Hadamard Product is the product of each element on the same position of each matrix,

$$[A\circ B]_{ij}=[A]_{ij}[B]_{ij},$$

where $[\cdot]_{ij}$ returns the element at the $i$-th row and $j$-th column.

# Properties of Hadamard Product

## Commutative (Trees, 2002, A.72)

> $$A\circ B=B\circ A.$$

## Associative (Trees, 2002, A.73)

> $$A\circ(B\circ C)=(A\circ B)\circ C.$$

## Distributive ()

> $$A\circ(B+C)=A\circ B+A\circ C.$$

# Properties of Mixed Production

## Kronecker- and Hadamard- Product

> $$(A\otimes B)\circ(C\otimes D)=(A\circ C)\otimes(B\circ D).$$

# References

Trees, H. L. V. (2002). *Optimum array processing: Part IV of detection, estimation, and modulation theory*. Jhon Wiley & Sons. 