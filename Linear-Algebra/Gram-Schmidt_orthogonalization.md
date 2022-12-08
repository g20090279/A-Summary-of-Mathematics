# Orthogonalization: the Gram-Schmidt Procedure

(copied from UC Berkeley)

> - Orthogonalization
> - Projection on a line
> - Gram-Schmidt procedure

A basis $(u_i)_{i=1}^n$ is said to be *orthogonal* if $u_i^Tu_j = 0$ if $i \ne j$. If in addition, $|u_i|_2 = 1$, we say that the basis is *orthonormal*.

**Example**: An orthonormal basis in $\mathbf{R}^3$. The collection of vectors ${u_1,u_2}$, with

$$u_1 = \frac{1}{\sqrt{2}} \left(\begin{array}{c} 1 \\ 1 \end{array}\right), \quad u_2 = \frac{1}{\sqrt{2}} \left(\begin{array}{c} 1 \\ -1 \end{array}\right),$$

forms an orthonormal basis of $\mathbf{R}^2$.

## What is orthogonalization?

Orthogonalization refers to a procedure that finds an orthonormal basis of the span of given vectors. 

Given vectors $a_1,\cdots,a_k \in \mathbf{R}^n$, an orthogonalization procedure computes vectors $q_1,\cdots,q_n \in \mathbf{R}^n$ such that $S:=\text{span} \left\{ a_1, \cdots, a_k \right\} = \text{span} \left\{ q_1,\cdots, q_r \right\}$ ,

where $r$ is the dimension of $S$, and

$$q_i^Tq_j = 0 \quad (i\ne j), \qquad q_i^Tq_i = 1 , \quad 1\le i,j \le r.$$

That is, the vectors $(q_1,\cdots,q_r)$ form an orthonormal basis for the span of the vectors $a_1,\cdots,a_k$.

## Basic step: projection on a line

A basic step in the procedure consists in projecting a vector on a line passing through zero. Consider the line

$$L(q) := \left\{ tq \ :\  t \in \mathbf{R} \right\} ,$$

where $q$ in $\mathbf{R}^n$ is given, and normalized ($\|q\|_2 = 1$).

The *projection* of a given point $a \in \mathbf{R}^n$ on the line is a vector $v$ located on the line, that is closest to a (in Euclidean norm). This corresponds to a simple optimization problem:

$$\min_t : \|a - tq\|_2.$$

The vector $a_{\mathrm{proj}} := t^\ast q$, where $t^\ast$ is the optimal value, is referred to as the *projection* of a on the line L(q). As seen here, the solution of this simple problem has a closed-form expression:

$$a_{\mathrm{proj}} = (q^Ta) q.$$

Note that the vector $x$ can now be written as a sum of its projection and another vector that is orthogonal to the projection:

$$a = (a-a_{\text{proj}}) + a_{\text{proj}} = (a-(q^Ta)q) + (q^Ta)q,$$

where $a-a_{\text{proj}} = a-(q^Ta)q$ and $a_{\text{proj}} = (q^Ta)q$ are orthogonal. The vector $a-a_{\text{proj}}$ can be interpreted as the result of removing the component of $a$ along $q$.

## Gram-Schmidt procedure

The Gram-Schmidt procedure is a particular orthogonalization algorithm. The basic idea is to first orthogonalize each vector w.r.t. previous ones; then normalize result to have norm one.

### Case when the vectors are independent

Let us assume that the vectors $a_1,\cdots,a_n$ are linearly independent. The GS algorithm is as follows.

**Gram-Schmidt procedure**:

1. set $\tilde{q}_1 = a_1$.
2. normalize: set $q_1 = \tilde{q}_1 / \|\tilde{q}_1\|_2$.
3. remove component of $q_1$ in $a_2$: set $\tilde{q}_2 = a_2 - (a_2^Tq_1)q_1$.
4. normalize: set $q_2 = \tilde{q}_2/\|\tilde{q}_2\|_2$.
5. remove components of $q_1,q_2$ in $a_3$: set $\tilde{q}_3 = a_3 - (a_3^Tq_1)q_1 - (a_3^Tq_2)q_2$.
6. normalize: set $q_3 = \tilde{q}_3/\|\tilde{q}_3\|_2$.
7. etc.

![GS algorithm for two vectors](.\images/Gram-Schmidt_2_vectors.png)  	

(Image 1: GS algorithm for two vectors)  	

The image of the left shows the GS procedure applied to the case of two vectors in two dimensions. We first set the first vector to be a normalized version of the first vector $a_1$. Then we remove the component of $a_2$ along the direction $q_1$. The difference is the (un-normalized) direction $\tilde{q}_2$, which becomes $q_2$ after normalization. At the end of the process, the vectors $q_1,q_2$ have both unit length and are orthogonal to each other.

The GS process is well-defined, since at each step $\tilde{q}_i \ne 0$ (otherwise this would contradict the linear independence of the a_i's).

### General case: the vectors may be dependent

It is possible to modify the algorithm to allow it to handle the case when the $a_i$'s are not linearly independent. If at step $i$, we find $\tilde{q}_i = 0$, then we directly jump at the next step.

**Modified Gram-Schmidt procedure**:

1. set $r=0$.
2. for $i=1,\cdots,n$:
    
    a. set $\tilde{q} = a_i - \sum_{j=1}^r (q_j^Ta_i)q_j$.
    
    b. if $\tilde{q} \ne 0$, $r = r+1$; $q_r = \tilde{q}/\|\tilde{q}\|_2$.

On exit, the integer $r$ is the dimension of the span of the vectors $a_1,\cdots,a_k$.
