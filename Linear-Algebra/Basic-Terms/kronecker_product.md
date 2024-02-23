[Kronecker Product] [克罗内克积]

The Kronecker product is an operation between two matrices of **arbitrary size**, resulting in a new matrix. It is usually denoted as $\otimes$.

# Definition of Kronecker Product

Given an $n\times m$ matrix $A_{n\times m}$ and another matrix $B_{p\times q}$ with size $p\times q$

$$A=\begin{bmatrix}
   a_{1,1} & \cdots & a_{1,m} \\
   \vdots & \ddots & \ddots \\
   a_{n,1} & \cdots & a_{n,m}
\end{bmatrix}_{n\times m},\quad B=\begin{bmatrix}
   b_{1,1} & \cdots &b_{1,q} \\
   \vdots,  \ddots & \vdots \\
   b_{p,1} & \cdots & b_{p,q}
\end{bmatrix}_{p\times q},$$

the Kronecker product $A\otimes B$ is a $np\times mq$ matrix with the structure

> $$A\otimes B=\begin{bmatrix}
    a_{1,1}B & \cdots & a_{1,m} \\
    \vdots & \ddots & \vdots \\
    a_{n,1}B & \cdots & a_{n,m}B
\end{bmatrix}_{np\times mq}.$$

The size of the Kronecker product matrix is expected to be very large.

# Properties of Kronecker Product

## Property 1: Bilinearity
$$(\alpha A)\otimes B=A\otimes(\alpha B)=\alpha(A\otimes B).\quad\mathrm{(P1)}$$

This property can be referred to (Trees, 2002, Eq. (A.84)).

## Property 2: Associativity
$$\begin{aligned}
    A\otimes(B+C)&=A\otimes B+A\otimes C,&\quad\mathrm{(P2.a)}\\
    (B+C)\otimes A&=B\otimes A+C\otimes A,&\quad\mathrm{(P2.b)}\\
    (A\otimes B)\otimes C&=A\otimes(B\otimes C).&\quad\mathrm{(P2.c)}
\end{aligned}$$

Eq. (P2.a), Eq. (P2.b) and Eq. (P2.c) can be respectively referred to (Trees, 2002, Eq. (A.87)), (Trees, 2002, Eq. (A.86)) and (Trees, 2002, Eq. (A.88)).

## Property 3: Non-commutative (in general)
$$A\otimes B\neq B\otimes A.\quad\mathrm{(P3)}$$

## Property 4: Transpose/Inversion/Hermitian distributes over the Kronecker product (*not* invert order)

$$\begin{aligned}
(A\otimes B)^T&=A^T\otimes B^T,&\quad\mathrm{(P4.a)}\\
(A\otimes B)^{-1}&=A^{-1}\otimes B^{-1},&\quad\mathrm{(P4.b)}\\
(A\otimes B)^{H}&=A^H\otimes B^H.&\quad\mathrm{(P4.c)}
\end{aligned}$$

For Eq. (P4.b) it is assumed that $A$ and $B$ are squared matrix with full rank, i.e. inversion matrices exist.

Eq. (P4.b) and Eq. (P4.c) can be respectively referred to (Trees, 2002, Eq. (A.90)) (Trees, 2002, Eq. (A.85)).

## Property 5: Matrix multiplication, when dimensions are appropriate

$$(A\otimes B)(C\otimes D)=AC\otimes BD.\quad\mathrm{(P5.a)}$$

If $A_1,A_2,\cdots,A_p$ are $M\times M$ and $B_1,B_2,\cdots,B_p$ are $N\times N$, then

$$(A_1\otimes B_1)(A_2\otimes B_2)\cdots(A_p\otimes B_p)=(A_1A_2\cdots A_p)\otimes(B_1B_2\cdots B_p).\quad\mathrm{(P5.b)}$$
  
## Property 6: The trace of a Kronecker product
$$\mathrm{trace}(A\otimes B)=\mathrm{trace}(A)\cdot\mathrm{trace}(B).$$

