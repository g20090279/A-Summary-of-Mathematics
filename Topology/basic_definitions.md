- Topics: Basic Definitions in Manifold
- Last Revised: Sep. 07, 2023

---

# Definitions in Sets

- **(Open Set)** A set $\mathcal{U}$ in $\mathbb{R}^n$ is said to be *open* if for every $p$ in $\mathcal{U}$, there is an open ball $B(p,r)$ with center $p$ and radius $r$ such that $B(p,r)\subset\mathcal{U}$. Properties:
  - The union of an arbitrary collection of open set is open.
  - The intersection of infinitely many open sets need not be open.
  - The intersection of finite open sets is open.

# Definitions of Differentiable Mapping

## In Euclidean Space

- **($C^{k}$)** Let $p=(p^1,\dots,p^n)$ be a point in an open set $\mathcal{U}$ in $\mathbb{R}^n$, and $k$ be a nonnegative integer. A real-valued function $f:U\rightarrow\mathbb{R}$ is said to be $C^{k}$ at $p\in \mathcal{U}$ if its partial derivatives
  $$\frac{\partial^{j}f}{\partial x^{i_1}\dots\partial x^{i_j}}$$
  of all orders $j\leq k$ exist and are continuous at $p$ (Tu 2011, Def. 1.1).
- **($C^{\infty}$ / Smooth)** The function $f:U\rightarrow\mathbb{R}$ is $C^{\infty}$ at $p$ if it is $C^{k}$ for all $k\geq0$.

## On A Manifold

- **(Coordinate Representation of $F$)** Let $F$ be a function from a manifold $\mathcal{M}_1$ of dimension $n_1$ into another manifold $\mathcal{M}_2$ of dimension $n_2$. Let $x$ be a point of $\mathcal{M}_1$ and thus $F(x)$ be a point of $\mathcal{M}_2$. Choosing charts $\phi_1$ around $x$ and $\phi_2$ around $F(x)$. The function $F$ around $x$ can be "read through the charts", yielding the function
  $$\hat{F}=\phi_2\circ F\circ\phi_1^{-1}:\mathbb{R}^{d_1}\rightarrow\mathbb{R}^{d_2},$$
  called *coordinate representation of $F$*. ($\hat{F}$ is the equivalent function from one chart in one manifold to another chart in another manifold.) If $\hat{F}$ is of class $C^{\infty}$ at the chart $\phi_1(x)$, $F$ is differentiable or smooth (Absil 2008, Sec. 3.2). A figure for illustration can be found in Fig. 6.3 in (Tu, 2011).
  - The definition of the smoothness of a map $F:\mathcal{M}_1\rightarrow\mathcal{M}_2$ at a point is independent of the choice of charts.
- **(Diffeomorphism)** A *diffeomorphism* os manifolds is a bijective $C^{\infty}$ map $F:N\rightarrow M$ whose inverse $F^{-1}$ is also $C^{\infty}$ (Tu 2011, Sec. 6.3).

# Definitions in Topology

- **(Homeomorphism)** A continuous bijection function $f:X\rightarrow Y$ whose inverse is also continuous is called a *homeomorphism* (Tu 2011, Prop. A.35).
- **(Second Countable)** A topological space is second countable if it has a countable basis (Tu, 2011).
- **(Neighborhood)** A neighborhood of a point $x\in X$ is a subset of $X$ that includes an open set containing $x$ (Absil 2008, A2).
- **(Topology)** (A topology on a set $S$ is an abstraction of the notion of open sets in $\mathbb{R}^n$) A *topology* on a set $S$ is a collection $\mathcal{T}$ of subsets of $S$ containing both the empty set $\emptyset$ and the set $S$ such that $\mathcal{T}$ is closed under arbitrary unions and finite intersections; i.e., if $U_{\alpha}\in\mathcal{T}$ for all $\alpha$ in an index set $A$, then $\bigcup_{\alpha\in A}U_{\alpha}\in\mathcal{T}$ and if  $U_1,\dots,U_n\in\mathcal{T}$, then $\bigcap_{i=1}^{n}U_i\in\mathcal{T}$ (Tu 2011, Def. A.1).
- **(Topological Space)**. (The idea behind the definition of a topological space is to discard all those properties of $\mathbb{R}^n$) The pair $(S,\mathcal{T})$ is called a *topological space*.
- **(Euclidean Space)**. A *Euclidean space* is a finite-dimensional real inner-product space, denoted by $\mathbb{R}^n$. There are many structures in this space, such as a metric, coordinates, an inner product, and an orientation, which are extraneous to its topology (Tu 2011, A.1).

# Definitions in Manifold

- **(Locally Euclidean of Dimension $n$)** A topological space $\mathcal{M}$ is *locally Euclidean of dimension $n$* if every point $p$ in $\mathcal{M}$ has a neighborhood $\mathcal{U}$ such that there is a homeomorphism $\phi$ from $\mathcal{U}$ onto an open subset of $\mathbb{R}^n$ (Tu 2011, Def. 5.1).
- **(Chart)**
  1. Let $\mathcal{M}$ be a set. A bijection $\phi$ of a subset $\mathcal{U}$ of $\mathcal{M}$ onto an open subset of $\mathbb{R}^n$ is called a $n$-dimensional *chart of the set $\mathcal{M}$*, denoted by $(\mathcal{U},\phi)$ (Absil 2008, Sec. 3.1.1).
  2. The pair $(\mathcal{U,\phi:\mathcal{U}\rightarrow\mathbb{R}^n})$ (Tu 2011, Def. 5.1).
- **(Coordinate)** Given a chart $(\mathcal{U},\phi)$ and $x\in\mathcal{U}$, the elements of $\phi(x)\in\mathbb{R}^d$ are called the *coordinates* of $x$ in the chart $(\mathcal{U},\phi)$ (Tu 2008, Sec. 3.1.1).
- **(Coordinate Neighborhood / Coordinate Open Set)** $\mathcal{U}$ in the chart $(\mathcal{U},\phi)$ is a *coordinate neighborhood* or a *coordinate open set* (Tu 2011, Def. 5.1).
- **(Coordinate Map / Coordinate System)** $\phi$ in the chart $(\mathcal{U},\phi)$ is a *coordinate map* or a *coordinate system* on $\mathcal{U}$ (Tu 2011, Def. 5.1).
- **(Parameterization)** The inverse map $\phi^{-1}$ is a *parameterization* of $\mathcal{U}$.
- **(Atlas)** A ($C^\infty$) *atlas of $\mathcal{M}$ into $\mathbb{R}^n$* is a collection of charts $(\mathcal{U}_{\alpha},\phi_{\alpha})$ of the set $\mathcal{M}$ such that  
- **(Topological Manifold)**
   A *topological manifold* is a Hausdorff, second countable, locally Euclidean space. It is said to be of *dimension $n$* if it is locally Euclidean of dimension $n$ (Tu 2011, Def. 5.2). Examples are
   - The Euclidean space $\mathbb{R}^n$ with an identity map.
   - A cusp $y=x^{2/3}$.
   - A cross is not a topological manifold.
- **(Smooth Manifold)**
  1. A *smooth* or $C^{\infty}$ *manifold* is a topological manifold $\mathcal{M}$ together with a maximal atlas.
  2. A (n-dimensional) manifold is a couple $(\mathcal{M},\mathcal{A}^+)$, where $\mathcal{M}$ is a set and $\mathcal{A}^+$ is a maximal atlas of $\mathcal{M}$ into $\mathbb{R}^n$ (Tu 2011, Sec. 3.1.1).
- **(Differentiable Structure)** A maximal atlas of set $\mathcal{M}$ is called a *differentiable structure* on $\mathcal{M}$.
- **(Transition Functions / Transition Maps / Coordinate Transformations)** For two charts $(\mathcal{U},\phi:\mathcal{U}\rightarrow\mathbb{R}^n)$ and $(\mathcal{V},\psi:\mathcal{V}\rightarrow\mathbb{R}^n)$ of a topological manifold, these two maps
  $$\phi\circ\psi^{-1}:\psi(\mathcal{U}\cap\mathcal{V})\rightarrow\phi(\mathcal{U}\cap\mathcal{V}),\quad\psi\circ\phi^{-1}:\phi(\mathcal{U}\cap\mathcal{V})\rightarrow\psi(\mathcal{U}\cap\mathcal{V})$$
  are called the *transition functions*, *transition maps*, or *coordinate transformations*.
- **(Compatible Charts)** If two charts of a topological manifold