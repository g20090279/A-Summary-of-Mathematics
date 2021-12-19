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

- Bilinearity
$$(\alpha A)\otimes B=A\otimes(\alpha B)=\alpha(A\otimes B).$$
- Associativity
$$\begin{aligned}
    A\otimes(B+C)&=A\otimes B+A\otimes C,\\
    (B+C)\otimes A&=B\otimes A+C\otimes A,\\
    (A\otimes B)\otimes C&=A\otimes(B\otimes C).
\end{aligned}$$
- Non-commutative (in general)
$$A\otimes B\neq B\otimes A.$$
- Transpose distributes over the Kronecker product (*not* invert order)
$$(A\otimes B)^T=A^T\otimes B^T.$$
- Matrix multiplication, when dimensions are appropriate
$$(A\otimes B)(C\otimes D)=(AC\otimes) BD.$$
- If A and B are square and full rank (*not* invert order)
$$(A\otimes B)^{-1}=A^{-1}\otimes B^{-1}.$$
- The trace of a Kronecker product
$$\mathrm{trace}(A\otimes B)=\mathrm{trace}(A)\cdot\mathrm{trace}(B).$$

