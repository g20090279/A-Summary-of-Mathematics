- Topic: Cheat Sheet of Complex Derivative
- Last revised: Jan. 23, 2023

Table of Content
1. Symbols and Variables   
1.1 Variables and Their Size
1.2 Basic Operators
2. Some Definitions
3. Some Theorems
---

# Introduction

One of the reasons for using complex numbers is the *fundamental theorem of algebra*:

> A polynomial of degree n has exactly the n complex roots.

The significant difference of the complex derivative of a complex analytic function compared to the differentiation of real calculus is that the infinity has two directions, the real axis and the imaginary axis. This is a very strong condition!

# Symbols and Variables

## Variables and Their Size

The variable is denoted by the letter $z$ (for scalar, or $\boldsymbol{z}$ for vector and $\boldsymbol{Z}$ for matrix. Same rules for other letters). Letter like $a$ or $b$ represent constant. Function is denoted by $f$.

|Symbol|$z$|$\boldsymbol{z}$|$\boldsymbol{Z}$|$f$|$\boldsymbol{f}$|$\boldsymbol{F}$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Size|$1\times1$|$N\times1$|$N\times Q$|$1\times1$|$M\times1$|$M\times P$|

$\mathbb{R}$ and $\mathbb{C}$ denote respectively the real number and complex number set. $\boldsymbol{A}\in\mathbb{C}^{N\times Q}$ means that the matrix $A$ contains complex numbers and has size $N\times Q$.

$i$ represents usually the *imaginary unit*, or *imaginary number*. Engineers typically use $j$ instead of $i$. Here we follow the mathematical custom by using $i$ as imaginary unit. $d$ represents derivative. $\partial$ is the partial derivative. $(\cdot)^*$ is the conjugate of a complex number, vector or matrix. $(\cdot)^T$ and $(\cdots)^H$ return transpose and Hermitian (conjugate transpose) respectively. $(\boldsymbol{A})^{-1}$ is the inverse matrix of a square matrix $\boldsymbol{A}$, i.e. $\boldsymbol{AA}^{-1}=\boldsymbol{A}^{-1}\boldsymbol{A}=\boldsymbol{I}$. $\text{Tr}\{\boldsymbol{A}\}$ and $\det(\boldsymbol{A})$ return the trace and the determinant of a square matrix $\boldsymbol{A}$. The adjoint of a matrix $\boldsymbol{A}\in\mathbb{C}^{N\times N}$ is denoted by $\text{adj}(\boldsymbol{A})$, i.e. $\text{adj}(\boldsymbol{A})=\det(\boldsymbol{A})\boldsymbol{A}^{-1}$.

## Basic Properties of Linear Algebra

|Equality|Comment|
|:---:|:---:|
| *The properties of **matrix inverse*** | |
| $(\boldsymbol{AB})^{-1}=\boldsymbol{B}^{-1}\boldsymbol{A}^{-1}$ | |
| $(\boldsymbol{ABC}...)^{-1}=...\boldsymbol{C}^{-1}\boldsymbol{B}^{-1}\boldsymbol{A}^{-1}$ | |
| $\left(\boldsymbol{A}^T\right)^{-1}$ | |
| *The properties of **matrix transpose*** | |
| $(\boldsymbol{A}+\boldsymbol{B})^T=\boldsymbol{A}^T+\boldsymbol{B}^T$| |
| $(\boldsymbol{AB})^{T}=\boldsymbol{B}^{T}\boldsymbol{A}^{T}$| |
| $(\boldsymbol{ABC}...)^T=...\boldsymbol{C}^{-T}\boldsymbol{B}^{T}\boldsymbol{A}^{T}$| |
| *The properties of **hermitian (complex conjugate)*** | |
| $\left(\boldsymbol A^H\right)^{-1}=\left(\boldsymbol{A}^{-1}\right)^H$ | |
| $(\boldsymbol{A}+\boldsymbol{B})^H=\boldsymbol{A}^H+\boldsymbol{B}^H$ | |
| $(\boldsymbol{AB})^H=\boldsymbol{B}^H\boldsymbol{A}^H$ | |
| $(\boldsymbol{ABC}...)^H=...\boldsymbol{C}^H\boldsymbol{B}^H\boldsymbol{A}^H$ | |
| *The properties of **Trace*** | Trace is only defined for a square matrix. |
| $\text{Tr}\lbrace\boldsymbol{A}\rbrace=\sum_i A_{ii}$ | |
| $\text{Tr}\lbrace\boldsymbol{A}\rbrace=\sum_i\lambda_i,\quad\lambda_i=\text{eig}(\boldsymbol{A})$ | |
| $\text{Tr}\lbrace\boldsymbol{A}^T\rbrace=\text{Tr}\lbrace\boldsymbol{A}\rbrace$ | $\boldsymbol{A}\in\mathbb{C}^{N\times N}$ |
| $\text{Tr}\lbrace\boldsymbol{AB}\rbrace=\text{Tr}\lbrace\boldsymbol{BA}\rbrace$ | $\boldsymbol{A}\in\mathbb{C}^{N\times Q}$ and $\boldsymbol{B}\in\mathbb{C}^{Q\times N}$ |
| $\text{Tr}(\boldsymbol{A}+\boldsymbol{B})=\text{Tr}(\boldsymbol{A})+\text{Tr}(\boldsymbol{B})$ | |
| $\text{Tr}(\boldsymbol{ABC})=\text{Tr}(\boldsymbol{BCA})=\text{Tr}(\boldsymbol{CAB})$ | |
| $\boldsymbol{a}^T\boldsymbol{a}=\text{Tr}(\boldsymbol{aa}^T)$ | |
| $\text{Tr}\lbrace\boldsymbol{A}^T\boldsymbol{B}\rbrace=\text{vec}^T(\boldsymbol{A})\text{vec}(\boldsymbol{B})$ | Connection between trace and vectorization |
| *The definition of **Determinant*** | Let $\boldsymbol{A}$ be an $n\times n$ matrix. |
| $\det(\boldsymbol{A})=\prod_{i}\lambda_i$ | $\lambda_i=\text{eig}(\boldsymbol{A})$ is the eigenvalue of matrix $\boldsymbol{A}$. |
| $\det(c\boldsymbol{A})=c^N\det(\boldsymbol{A})$ | if $\boldsymbol{A}=\mathbb{C}^{N\times N}$ |
| $\det(\boldsymbol{A}^T)=\det(\boldsymbol{A})$ | |
| $\det(\boldsymbol{AB})=\det(\boldsymbol{A})\det(\boldsymbol{B})$ |
| $\det(\boldsymbol{A}^{-1})=1/\det(\boldsymbol{A})$ | |
| $\det(\boldsymbol{A}^N)=\det(\boldsymbol{A})^N$ | |
| $\det(\boldsymbol{I}+\boldsymbol{uv}^T)=1+\boldsymbol{u}^T\boldsymbol{v}$ | |
| $\det(\boldsymbol{I+AB})=\det(\boldsymbol{I+BA})$ | Sylvester's Determiant Theorem |

# Some Definitions

***Table:** Some Definitions.*

| Index | Name of Definition | Mathematical Description |
| :--- | :--- | :--- |
| 1 | Complex Scalar | $z=x+iy\in\mathbb{C}$, where the *real part* is $\mathfrak{R}(z)$ and the *imaginary part* is $\mathfrak{I}(z)=y$. |
| 2 | Real Part | $\mathfrak{R}(z)=x=\frac{z+z^\ast}{2}$ |
| 3 | Imaginary Part| $\mathfrak{I}(z)=y=\frac{z-z^\ast}{2i}$ |
| 4 | Complex Differentials | (complex scalar as example) <br> $dz=dx+idy$, $dz^\ast=dx-idy$<br/>which lead to<br/>$dx=\frac{dz+dz^\ast}{2}$, $dy=\frac{dz-dz^\ast}{2i}$, $dz^\ast=(dz)^\ast$<br/>When $\boldsymbol{Z}$ is a matrix, $\boldsymbol{X}$ and $\boldsymbol{Y}$ are of same size, e.g. $N\times Q$.| 
| 5 | Analytic Function (asa. Complex Differentiable, Holomorphic, Regular) | The function $f$ is an analytic function if $\lim_{\Delta z\rightarrow0}\frac{f(z+\Delta z)-f(z)}{\Delta z}$ exists for all $z\in\mathcal{D}$, where the domain $\mathcal{D}$ is a subset of $\mathbb{C}$. Analytic function examples: $z^n$, $e^z$, $\ln(z)$, $\sin(z)$, $\cos(z)$. Not analytic function examples: $z^\ast$, $\mathfrak{R}(z)$, $\mathfrak{I}(z)$, any nonconstant purely real-valued function such as $\|z\|$. Nonholomorphic functions can all be written in the form $f(z,z^*)$. |
| 5.1 | Cauchy-Riemann Equation | (Complex scalar as an example) If $f=u(x,y)+iv(x,y)$ is complex-differentiable (analytic) at $z=x+iy$, then by approaching from real and imaginary axes, we have equations: $\begin{cases}\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y} \\ \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}.\end{cases}$. This implies $\frac{\partial}{\partial z^\ast}f=0$ for Wirtinger Derivative. |
| 6 | True Derivative |$df=\frac{\partial f}{\partial x}dx+\frac{\partial f}{\partial y}dy$ <br/> Notice: This is the basic assumption: real part and imaginary part are independent|
| 7 | Formal* Derivative / Wirtinger Derivative / $\mathbb{CR}$-Derivative | Let $z=x+iy$, where $x,y\in\mathbb{R}$. From 2, 3 and 6 in this table, we have $\mathbb{R}$-Derivative of $f(z)\overset{\Delta}{=}\frac{\partial}{\partial z}f\lvert_{z^\ast=\text{const}}=\frac{1}{2}\left(\frac{\partial}{\partial x}f-i\frac{\partial}{\partial y}f\right)$ <br/> Conjugate $\mathbb{R}$-Derivative of $f(z)\overset{\Delta}{=}\frac{\partial}{\partial z^\ast}f\lvert_{z=\text{const}}=\frac{1}{2}\left(\frac{\partial}{\partial x}f+i\frac{\partial}{\partial y}f\right)$. <br /> The variables $z$ and $z^\ast$ are treated as independent variables. (Formulated by replacing $dx$ and $dy$ in basic assumption with complex differentials.) <br/> Notice: $\frac{\partial}{\partial z}f\ne\frac{\partial}{\partial \mathfrak{R}(z)}f+i\frac{\partial}{\partial\mathfrak{I}(z)}f$. <br> * These statements are formal (形式上的) (compared to the true derivative) because one cannot truly vary $z=x+iy$ while keeping $z^\ast=x-iy$ constant, and vice versa. |
| 8 | Procedure on Finding Complex Differentials | Consider a complex matrix function $\boldsymbol{F}:\mathbb{C}^{N\times Q}\times\mathbb{C}^{N\times Q}\rightarrow\mathbb{C}^{M\times P}$ with two input complex-valued matrix variables $\boldsymbol{Z}_0\in\mathbb{C}^{N\times Q}$ and $\boldsymbol{Z}_1\in\mathbb{C}^{N\times Q}$, the difference of a infinitesimal increment is $\begin{aligned}\boldsymbol{F}(&\boldsymbol{Z}_0+d\boldsymbol{Z}_0,\boldsymbol{Z}_1+d\boldsymbol{Z}_1)-\boldsymbol{F}(\boldsymbol{Z}_0,\boldsymbol{Z}_1)\\ &=\text{First-order}(d\boldsymbol{Z}_0,d\boldsymbol{Z}_1)+\text{Higher-order}(d\boldsymbol{Z}_0,d\boldsymbol{Z}_1).\end{aligned}$ The First-order( ) term depends on the first order of $d\boldsymbol{Z}_0$ or $d\boldsymbol{Z}_1$. The differential is then given by the *first-order term*. |
| 9 | Derivative wrt. Complex Matrices (most general definition of the derivative) | $\boldsymbol{F}:\mathbb{C}^{N\times Q}\times\mathbb{C}^{N\times Q}\rightarrow\mathbb{C}^{M\times P}$, the derivative of $\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast)$ with respect to $\boldsymbol{Z}\in\mathbf{C}^{N\times Q}$ is denoted by $\mathcal{D}_{\boldsymbol{Z}}\boldsymbol{F}$, and that with respect to $\boldsymbol{Z}^{\ast}\in\mathbb{C}^{N\times Q}$ is denoted by $\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{F}$. The size of both these derivatives is $MP\times NQ$. <br/> Then, $d\ \text{vec}(\boldsymbol{F})=(\mathcal{D}_{\boldsymbol{Z}}\boldsymbol{F})d\ \text{vec}(\boldsymbol{Z})+(\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{F})d\ \text{vec}(\boldsymbol{Z}^\ast)$. <br/> The two derivatives are called the *Jacobian matrices* of $\boldsymbol{F}$ with respect to $\boldsymbol{Z}$ or $\boldsymbol{Z}^\ast$. <br/> (Note that the derivatives here have predefined forms. Sometimes the derivatives here are different from the common partial derivative expression. A summary of $\mathcal{D}_{\boldsymbol{Z}}\boldsymbol{F}$ and $\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{F}$ with scalar, vector, or matrix $\boldsymbol{Z}$ or $\boldsymbol{F}$ is given in Appendix.) |
| 10 |Formal Derivatives of Vector Functions w.r.t. Vectors|$\boldsymbol{f}:\mathbb{C}^{N\times1}\times\mathbb{C}^{N\times1}\rightarrow\mathbb{C}^{M\times1}$. The derivatives of a *vector* function wrt. two *row vector* variables $\boldsymbol{z}^T$ and $\boldsymbol{z}^H$ are matrices sized as $M\times N$<br/>$\frac{\partial}{\partial\boldsymbol{z}^T}\boldsymbol{f}(\boldsymbol{z},\boldsymbol{z}^\ast)=\begin{bmatrix}\frac{\partial}{\partial z_0}f_0 & \cdots & \frac{\partial}{\partial z_{N-1}}f_0\\\\\vdots & &\vdots\\\\\frac{\partial}{\partial z_0}f_{M-1} & \cdots & \frac{\partial}{\partial z_{N-1}}f_{M-1}\end{bmatrix}$ <br/> and <br/> $\frac{\partial}{\partial\boldsymbol{z}^H}\boldsymbol{f}(\boldsymbol{z},\boldsymbol{z}^\ast)=\begin{bmatrix}\frac{\partial}{\partial z_0^\ast}f_0 & \cdots & \frac{\partial}{\partial z_{N-1}^\ast}f_0 \\\\ \vdots &&\vdots \\\\ \frac{\partial}{\partial z_0^\ast}f_{M-1} & \cdots & \frac{\partial}{\partial z_{N-1}^\ast}f_{M-1} \end{bmatrix}.$<br/> Note that $\frac{\partial}{\partial\boldsymbol{z}^T}\boldsymbol{f}=\mathcal{D}_{\boldsymbol{z}}\boldsymbol{f}$ and $\frac{\partial}{\partial\boldsymbol{z}^H}\boldsymbol{f}=\mathcal{D}_{\boldsymbol{z}^*}\boldsymbol{f}$. <br/>Use 10, the derivtives in 9 are <br/>$\mathcal{D}_{\boldsymbol{Z}}\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\frac{\partial\text{vec}(\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast))}{\partial\text{vec}^T(\boldsymbol{Z})}$, <br/>$\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\frac{\partial\text{vec}(\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast))}{\partial\text{vec}^T(\boldsymbol{Z}^\ast)}$.|
| 11 | Formal Derivative of Matrix Functions w.r.t. Scalars |$\boldsymbol{F}:\mathbb{C}^{N\times Q}\times\mathbb{C}^{N\times Q}\rightarrow\mathbb{C}^{M\times P}$. The derivative of $\boldsymbol{F}$ w.r.t. the scalar $z\in\mathbb{C}$ is <br/> $\frac{\partial\boldsymbol{F}}{\partial z}=\begin{bmatrix}\frac{\partial f_{0,0}}{\partial z} & \cdots & \frac{\partial f_{0,P-1}}{\partial z}\\\\\vdots&\ddots&\vdots\\\\\frac{\partial f_{M-1,0}}{\partial z}&\cdots&\frac{\partial f_{M-1,P-1}}{\partial z}\end{bmatrix}$, <br/> which has size $M\times P$.|
| 12 | Procedure for finding the derivative of the complex matrix function $\boldsymbol{F}$ with respect to the complex matrices $\boldsymbol{Z}$ and $\boldsymbol{Z}^\ast$ | Three-step procedure:<br/>1. Comput the differential $d\ \text{vec}(\boldsymbol{\boldsymbol{F}})$<br/> 2. Manipulate the expression into the form given by 9 in this table. <br/> 3. The matrices $\mathcal{D}_{\boldsymbol{Z}}(\boldsymbol{Z},\boldsymbol{Z}^\ast)$ and $\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast)$ can now be read out by using 9. |
| 12 | Complex Gradient Vector | If $f$ is a real-value function* of a complex vector $\boldsymbol{z}$, then the complex gradient vector is given by $\nabla f(\boldsymbol{z})=2\frac{df(\boldsymbol{z})}{d\boldsymbol{z}^\ast}=\frac{\partial f(\boldsymbol{z})}{\partial\mathfrak{R}(\boldsymbol{z})}+i\frac{\partial f(\boldsymbol{z})}{\partial\mathfrak{I}(\boldsymbol{z})}$. <br> *A real value function is not holomorphic. |
| 13 | Complex Gradient Matrix | If $f$ is a real-value function of a complex matrix $Z$, then the complex gradient matrix is given by $\nabla f(\boldsymbol{Z})=2\frac{df(\boldsymbol{Z})}{d\boldsymbol{Z}^\ast}=\frac{\partial f(\boldsymbol{Z})}{\partial\mathfrak{R}(\boldsymbol{Z})}+i\frac{\partial f(\boldsymbol{Z})}{\partial\mathfrak{I}(\boldsymbol{Z})}$. |

## Identification Table and Examples for the Derivative

Check the definition of derivative with respect to a matrix. The following table summarizes from the simplest case to the most-general case. $\boldsymbol{z},\boldsymbol{z}^\ast\in\mathbb{C}^{N\times 1}$ and $\boldsymbol{Z},\boldsymbol{Z}^\ast\in\mathbb{C}^{N\times Q}$, and $\boldsymbol{f}:\rightarrow\mathbb{C}^{M\times1}$, $\boldsymbol{F}:\rightarrow\mathbb{C}^{M\times P}$.

***Table:** Identification table.*

|Function type|Differential|Derivative w.r.t. $z$, $\boldsymbol{z}$ or $\boldsymbol{Z}$|Derivative w.r.t. $z^\ast$, $\boldsymbol{z}^\ast$ or $\boldsymbol{Z}^\ast$|Size of derivatives|
|:---:|:---:|:---:|:---:|:---:|
|$f(z,z^\ast)$|$df=a_0dz+a_1dz^*$|$\mathcal{D}_zf(z,z^\ast)=a_0$|$\mathcal{D}_{z^\ast}f(z,z^\ast)=a_1$|$1\times1$|
|$f(\boldsymbol{z},\boldsymbol{z}^\ast)$|$df=\boldsymbol{a}_0d\boldsymbol{z}+\boldsymbol{a}_1\boldsymbol{z}^\ast$|$\mathcal{D}_{\boldsymbol{z}}f(\boldsymbol{z},\boldsymbol{z}^\ast)=\boldsymbol{a}_0$|$\mathcal{D}_{\boldsymbol{z}^\ast}f(\boldsymbol{z},\boldsymbol{z}^\ast)=\boldsymbol{a}_1$|$1\times N$|
|$f(\boldsymbol{Z},\boldsymbol{Z}^\ast)$|$df=\text{vec}^T(\boldsymbol{A}_0)d\ \text{vec}(\boldsymbol{Z})+\text{vec}^T(\boldsymbol{A}_1)d\ \text{vec}(\boldsymbol{Z}^\ast)$|$\mathcal{D}_{\boldsymbol{Z}}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\text{vec}^T(\boldsymbol{A}_0)$|$\mathcal{D}_{\boldsymbol{Z}^\ast}(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\text{vec}^T(\boldsymbol{A}_1)$|$1\times NQ$|
|$f(\boldsymbol{Z},\boldsymbol{Z}^\ast)$|$df=\text{Tr}\{\mathbf{A}_0^Td\boldsymbol{Z}+\boldsymbol{A}_1^Td\boldsymbol{Z}^\ast\}$|$\frac{\partial}{\partial\boldsymbol{Z}}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\boldsymbol{A}_0$|$\frac{\partial}{\partial\boldsymbol{Z}^\ast}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\boldsymbol{A}_1$|$N\times Q$|
|$\boldsymbol{f}(z,z^\ast)$|$d\boldsymbol{f}=\boldsymbol{b}_0dz+\boldsymbol{b}_1dz^\ast$|$\mathcal{D}_{z}\boldsymbol{f}(z,z^\ast)=\boldsymbol{b}_0$|$\mathcal{D}_{z^\ast}\boldsymbol{f}(z,z^\ast)=\boldsymbol{b}_1$|$M\times1$|
|$\boldsymbol{f}(\boldsymbol{z},\boldsymbol{z}^\ast)$|$d\boldsymbol{f}=\boldsymbol{B}_0d\boldsymbol{z}+\boldsymbol{B}_1d\boldsymbol{z}^\ast$|$\mathcal{D}_{\boldsymbol{z}}\boldsymbol{f}(\boldsymbol{z},\boldsymbol{z}^\ast)=\boldsymbol{B}_0$|$\mathcal{D}_{\boldsymbol{z}^\ast}\boldsymbol{f}(\boldsymbol{z},\boldsymbol{z}^\ast)=\boldsymbol{B}_1$|$M\times N$|
|$\boldsymbol{f}(\boldsymbol{Z},\boldsymbol{Z}^\ast)$|$d\boldsymbol{f}=\boldsymbol{\beta}_0d\text{vec}(\boldsymbol{Z})+\boldsymbol{\beta}_1d\text{vec}(\boldsymbol{Z}^\ast)$|$\mathcal{D}_{\boldsymbol{Z}}\boldsymbol{f}(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\boldsymbol{\beta}_0$|$\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{f}(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\boldsymbol{\beta}_1$|$M\times NQ$|
|$\boldsymbol{F}(z,z^\ast)$|$d\text{vec}(\boldsymbol{F})=\boldsymbol{c}_0dz+\boldsymbol{c}_1dz^\ast$|$\mathcal{D}_{z}\boldsymbol{F}(z,z^\ast)=\boldsymbol{c}_0$|$\mathcal{D}_{z^\ast}\boldsymbol{F}(z,z^\ast)=\boldsymbol{c}_1$|$MP\times1$|
|$\boldsymbol{F}(\boldsymbol{z},\boldsymbol{z}^\ast)$|$d\text{vec}(\boldsymbol{F})=\boldsymbol{C}_0d\boldsymbol{z}+\boldsymbol{C}_1d\boldsymbol{z}^\ast$|$\mathcal{D}_{\boldsymbol{z}}\boldsymbol{F}(\boldsymbol{z},\boldsymbol{z}^\ast)=\boldsymbol{C}_0$|$\mathcal{D}_{\boldsymbol{z}^\ast}\boldsymbol{F}(\boldsymbol{z},\boldsymbol{z}^\ast)=\boldsymbol{C}_1$|$MP\times N$|
|$\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast)$|$d\text{vec}(\boldsymbol{F})=\boldsymbol{\zeta}_0d\boldsymbol{Z}+\boldsymbol{\zeta}_1d\boldsymbol{Z}^\ast$|$\mathcal{D}_{\boldsymbol{Z}}\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\boldsymbol{\zeta}_0$|$\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\boldsymbol{\zeta}_1$|$MP\times NQ$|

# Some Theorems

## Chian Rules

| Index | Name | Expression | Reference |
| :--- | :--- | :--- | :--- |
|1 | Chain Rule | Let $(\mathcal{S}_0,\mathcal{S}_1)\subseteq\mathbb{C}^{N\times Q}\times\mathbb{C}^{N\times Q}$ and $\boldsymbol{F}:\mathcal{S}_0\times\mathcal{S}_1\rightarrow\mathbb{C}^{M\times P}$ be differentiable. Define the differentiable composite function $\boldsymbol{H}:\mathcal{S}_0\times\mathcal{S}_1\rightarrow\mathbb{C}^{R\times S}$ by <br/> $\boldsymbol{H}(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\boldsymbol{G}(\boldsymbol{F}(\boldsymbol{Z},\boldsymbol{Z}^\ast),\boldsymbol{F}^\ast(\boldsymbol{Z},\boldsymbol{Z}^\ast))$ <br/> with derivatives <br/> $\mathcal{D}_{\boldsymbol{Z}}\boldsymbol{H}=(\mathcal{D}_{\boldsymbol{F}}\boldsymbol{G})(\mathcal{D}_{\boldsymbol{Z}}\boldsymbol{F})+(\mathcal{D}_{\boldsymbol{F}^\ast}\boldsymbol{G})(\mathcal{D}_{\boldsymbol{Z}}\boldsymbol{F}^\ast)$, <br/> $\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{H}=(\mathcal{D}_{\boldsymbol{F}}\boldsymbol{G})(\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{F})+(\mathcal{D}_{\boldsymbol{F}^\ast}\boldsymbol{G})(\mathcal{D}_{\boldsymbol{Z}^\ast}\boldsymbol{F}^\ast)$. | |

## Scalar Real-Value Function

The problems encountered by engineers are mostly related to scalar real-value functions, with which we can compare the magnitude, ordering, and hence find the maximum or minimum.

| Index | Name | Expression | Reference |
| :--- | :--- | :--- | :--- |
| 1 | **!!! Scalar Real-Valued Function**: 3 Equivalent Ways to Identify Stationary Point  | $f:\mathbb{C}^{N\times Q}\times\mathbb{C}^{N\times Q}\rightarrow\mathbb{R}$. A stationary point of the function $f(\boldsymbol{Z},\boldsymbol{Z}^\ast)=g(\boldsymbol{X},\boldsymbol{Y})$, where $g:\mathbb{R}^{N\times Q}\times\mathbb{R}^{N\times Q}\rightarrow\mathbb{R}$ and $\boldsymbol{Z}=\boldsymbol{X}+i\boldsymbol{Y}$ is then found by one of the following three equivalent conditions: <br/> 1. $\mathcal{D}_{\boldsymbol{X}}g(\boldsymbol{X},\boldsymbol{Y})=\boldsymbol{0}_{1\times NQ}$ and $\mathcal{D}_{\boldsymbol{Y}}g(\boldsymbol{X},\boldsymbol{Y})=\boldsymbol{0}_{1\times NQ}$, <br/> 2. $\mathcal{D}_{\boldsymbol{Z}}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\boldsymbol{0}_{1\times NQ}$, <br/> 3. $\mathcal{D}_{\boldsymbol{Z}^\ast}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)=\boldsymbol{0}_{1\times NQ}$. <br/> Note: They are all "long" *row vector*, since $df$ is a scalar! <br/> (A stationary point can be a local minimum, a local maximum, or a saddle point.) | (Hjorungnes 2011, Theorem 3.2) |
| 2 | Scalar Real-Valued Function: Derivative | $f:\mathbb{C}^{N\times Q}\times\mathbb{C}^{N\times Q}\rightarrow\mathbb{R}$, then $\mathcal{D}_{\boldsymbol{Z}^\ast}f=\left(\mathcal{D}_{\boldsymbol{Z}}f\right)^\ast$. <br/> This theorem leads to <br/> $df=2\mathfrak{R}\lbrace(\mathcal{D}_{\boldsymbol{Z}}f)d\ \text{vec}(\boldsymbol{Z})\rbrace$. <br/> Note: With Definition 9, for $f\in\mathbb{R}$, we can write $df=(\mathcal{D}_{\boldsymbol{Z}}f)d\ \text{vec}(\boldsymbol{Z})+(\mathcal{D}_{\boldsymbol{Z}^\ast}f)d\ \text{vec}(\boldsymbol{Z}^\ast)$. | (Hjorungnes 2011, Theorem 3.3) |
| <a name='T4'>3<a> | Scalar Real-Valued Function: Descend Direction. | $f:\mathbb{C}^{N\times Q}\times\mathbb{C}^{N\times Q}\rightarrow\mathbb{R}$. The directions where the function $f$ has the maximum and minimum rate of change with respect to $\text{vec}(\boldsymbol{Z})$ are given by $\left[\mathcal{D}_{\boldsymbol{Z}^\ast}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)\right]^T$ and $-\left[\mathcal{D}_{\boldsymbol{Z}^\ast}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)\right]^T$, respectively. <br/> **Note that it is w.r.t. $Z$ conjugate!** (Proof in [Proof of T4](#proof-of-t4)) | (Hjorungnes 2011, Theorem 3.4) |

Example MIMO Channel

# Basic Complex Differential Properties

Take the matrix form $\boldsymbol{Z}$ as example.

***Table:** Basic complex differential properties.*

|Properties|Comment|
|:---:|:---:|
|$d\boldsymbol{A}=\boldsymbol{0}_{M\times P}$|$\boldsymbol{A}\in\mathbb{C}^{M\times P}$ is a constant matrix that independent of $\boldsymbol{Z}$ or $\boldsymbol{Z}^{*}$|
|$d(\boldsymbol{AZB})=\boldsymbol{A}(d\boldsymbol{Z})\boldsymbol{B}$|$\boldsymbol{A}$ and $\boldsymbol{B}$ are constants|
|$d(a\boldsymbol{Z})=a\ d\boldsymbol{Z}$||
|$d(\boldsymbol{Z}_0+\boldsymbol{Z}_1)=d\boldsymbol{Z}_0+d\boldsymbol{Z}_1$||
|$d\left(\text{Tr}\lbrace\boldsymbol{Z}\rbrace\right)=\text{Tr}\lbrace d\boldsymbol{Z}\rbrace$||
|$d(\boldsymbol{Z}_0\boldsymbol{Z}_1)=(d\boldsymbol{Z}_0)\boldsymbol{Z}_1+\boldsymbol{Z}_0(d\boldsymbol{Z}_1)$||
|$d(\boldsymbol{Z}_0\otimes\boldsymbol{Z}_1)=(d\boldsymbol{Z}_0)\otimes\boldsymbol{Z}_1+\boldsymbol{Z}_0\otimes(d\boldsymbol{Z}_1)$|Kronecker product|
|$d(\boldsymbol{Z}_0\odot\boldsymbol{Z}_1)=(d\boldsymbol{Z}_0)\odot\boldsymbol{Z}_1+\boldsymbol{Z}_0\odot(d\boldsymbol{Z}_1)$|Hadamard product|
|$d\boldsymbol{Z}^{-1}=-\boldsymbol{Z}^{-1}(d\boldsymbol{Z})\boldsymbol{Z}^{-1}$|matrix inverse|
|$d\ \text{reshape}(\boldsymbol{Z})=\text{reshape}(d\boldsymbol{Z})$|reshape|
|$d\boldsymbol{Z}^\ast=(d\boldsymbol{Z})^\ast$|conjugate|
|$d\boldsymbol{Z}^{H}=(d\boldsymbol{Z})^H$|complex conjugate|
|$d\det(\boldsymbol{Z})=\text{Tr}\lbrace\boldsymbol{C}^T(\boldsymbol{Z})d\boldsymbol{Z}\rbrace=\det(\boldsymbol{Z})\text{Tr}\{\boldsymbol{Z}^{-1}d\boldsymbol{Z}\}$|where $\boldsymbol{C}(\boldsymbol{Z})$ is a $N$-size square matrix containing cofactors. determinant and trace|
| $d\ln(\det(\boldsymbol{Z}))=\text{Tr}\{Z^{-1}d\boldsymbol{Z}\}$ |

# Advanced Complex Differential Equations

| Equations | Comments |
|:---:|:---:|
|$\frac{\partial}{\partial X}\ln\det X$||

# Complex-Valued Derivatives of Scalar Functions

## Complex-Valued Derivatives of $f(z,z^\ast)$

## Complex-Valued Derivatives of $f(\boldsymbol{z},\boldsymbol{z}^\ast)$

***Table**: Complex-valued derivatives of functions of the type* $f(\boldsymbol{z},\boldsymbol{z}^\ast)$

|$f(\boldsymbol{z},\boldsymbol{z}^\ast)$|Differential $df$|$\mathcal{D}_{\boldsymbol{z}}f(\boldsymbol{z},\boldsymbol{z}^\ast)$|$\mathcal{D}_{\boldsymbol{z}^\ast}f(\boldsymbol{z},\boldsymbol{z}^\ast)$|
|:---:|:---:|:---:|:---:|
|$\boldsymbol{a}^T\boldsymbol{z}=\boldsymbol{z}^T\boldsymbol{a}$|$\boldsymbol{a}^Td\boldsymbol{z}$|$\boldsymbol{a}^T$|$\boldsymbol{0}_{1\times N}$|
|$\boldsymbol{a}^T\boldsymbol{z}^\ast=\boldsymbol{z}^H\boldsymbol{a}$|$\boldsymbol{a}^Td\boldsymbol{z}^\ast$|$\boldsymbol{0}_{1\times N}$|$\boldsymbol{a}^T$|
|$\boldsymbol{z}^T\boldsymbol{Az}$|$\boldsymbol{z}^T\left(\boldsymbol{A}+\boldsymbol{A}^T\right)d\boldsymbol{z}$|$\boldsymbol{z}^T\left(\boldsymbol{A}+\boldsymbol{A}^T\right)$|$\boldsymbol{0}_{1\times N}$|
|$\boldsymbol{z}^H\boldsymbol{Az}$|$\boldsymbol{z}^H\boldsymbol{A}d\boldsymbol{z}+\boldsymbol{z}^T\boldsymbol{A}^Td\boldsymbol{z}$|$\boldsymbol{z}^H\boldsymbol{A}$|$\boldsymbol{z}^T\boldsymbol{A}^T$|
|$\boldsymbol{z}^T\boldsymbol{Az}^{\ast}$|$\boldsymbol{z}^H\left(\boldsymbol{A}+\boldsymbol{A}^T\right)d\boldsymbol{z}^{\ast}$|$\boldsymbol{0}_{1\times N}$|$\boldsymbol{z}^H\left(\boldsymbol{A}+\boldsymbol{A}^T\right)$|

## Complex-Valued Derivatives of $f(\boldsymbol{Z},\boldsymbol{Z}^*)$

### Definition 1: use the general form of formal derivative

$$df=\text{vec}^T(\boldsymbol{A}_0)d\text{vec}(\boldsymbol{Z})+\text{vec}^T(\boldsymbol{A}_1)d\text{vec}(\boldsymbol{Z}^\ast),$$

where $\boldsymbol{A}_0,\boldsymbol{A}_1,\boldsymbol{Z}\in\mathbb{C}^{N\times Q}$. Note that the derivatives $\mathcal{D}_{\boldsymbol{Z}}f=\text{vec}^T(\boldsymbol{A}_0)$ and $\mathcal{D}_{\boldsymbol{Z}^\ast}f=\text{vec}^T(\boldsymbol{A}_1)$ are $1\times NQ$ row vectors.

### Definition 2: an alternative to Definition 1

For this type, it is common to arrange the formal derivatives in an alternative way than in the expressions $\mathcal{D}_{\boldsymbol{Z}}f(\boldsymbol{Z},\boldsymbol{Z}^*)$ and $\mathcal{D}_{\boldsymbol{Z}^\ast}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)$ where $\boldsymbol{Z}\in\mathbb{C}^{N\times Q}$:

$$\begin{aligned}
    \frac{\partial}{\partial\boldsymbol{Z}}f=&\begin{bmatrix}
        \frac{\partial}{\partial z_{0,0}}f & \cdots & \frac{\partial}{\partial z_{0,Q-1}}f\\
        \vdots & \ddots & \vdots \\
        \frac{\partial}{\partial z_{N-1,0}}f & \cdots & \frac{\partial}{\partial z_{N-1,Q-1}}f\\
    \end{bmatrix},\\
     \frac{\partial}{\partial\boldsymbol{Z}^\ast}f=&\begin{bmatrix}
        \frac{\partial}{\partial z_{0,0}^\ast}f & \cdots & \frac{\partial}{\partial z_{0,Q-1}^\ast}f\\
        \vdots & \ddots & \vdots \\
        \frac{\partial}{\partial z_{N-1,0}^\ast}f & \cdots & \frac{\partial}{\partial z_{N-1,Q-1}^\ast}f\\
    \end{bmatrix}.\\
\end{aligned}$$

$\frac{\partial}{\partial\boldsymbol{Z}}f$ and $\frac{\partial}{\partial\boldsymbol{Z}^\ast}f$ are matrix of size $N\times Q$ and called the *gradient* of $f$ with respect to $\boldsymbol{Z}$ and $\boldsymbol{Z}^\ast$. Some lituratures use the following notation

$$\begin{aligned}
  \nabla_{\boldsymbol{Z}^\ast}f&\overset{\Delta}{=}\frac{\partial}{\partial\boldsymbol{Z}}f,\\ 
  \nabla_{\boldsymbol{Z}}f&\overset{\Delta}{=}\frac{\partial}{\partial\boldsymbol{Z}^\ast}f.\\
\end{aligned}$$

Note that for a scalar real-valued function, the gradient (the direction of deepest descent) is with respect to the conjugate. 

### Connection between definition 1 and definition 2

From the basic property of trace, we have

$$\begin{align} df & =\text{vec}^T(\boldsymbol{A}_0)d\text{vec}(\boldsymbol{Z})+\text{vec}^T(\boldsymbol{A}_1)d\text{vec}(\boldsymbol{Z}^\ast) \\\\ &=\text{Tr}\lbrace\boldsymbol{A}_0^Td\boldsymbol{Z}+\boldsymbol{A}_1^Td\boldsymbol{Z}^\ast\rbrace, \end{align}$$

which links the formal derivative of size $1\times NQ$

$$\begin{align}\mathcal{D}_{\boldsymbol{Z}}f & =\text{vec}^T(\boldsymbol{A}_{0}) \\\\ \mathcal{D}_{\boldsymbol{Z}^{\ast}}f & =\text{vec}^T(\boldsymbol{A}_{1})\end{align}$$

to the gradients of $f$ with respect to $\boldsymbol{Z}$ and $\boldsymbol{Z}^\ast$ of size $N\times Q$

$$\begin{align}
   \frac{\partial}{\partial\boldsymbol{Z}}f&=\boldsymbol{A}_0\\ 
   \frac{\partial}{\partial\boldsymbol{Z}^\ast}f&=\boldsymbol{A}_1
\end{align}$$

by the connection

$$\begin{align}
   \mathcal{D}_{\boldsymbol{Z}}f(\boldsymbol{Z},\boldsymbol{Z}^*)&=\text{vec}^T\left(\frac{\partial}{\partial\boldsymbol{Z}}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)\right)\\ 
   \mathcal{D}_{\boldsymbol{Z}^\ast}f(\boldsymbol{Z},\boldsymbol{Z}^{\ast})&=\text{vec}^T\left(\frac{\partial}{\partial\boldsymbol{Z}^\ast}f(\boldsymbol{Z},\boldsymbol{Z}^\ast)\right)\\ 
\end{align}$$

### Table: Complex-valued derivatives of functions of the type* $f(\boldsymbol{Z},\boldsymbol{Z}^\ast)$. 

Note:

1. Assume the matrices have suitable dimension for the matrix multiplication).
2. Trace is only defined for a square matrix.

|$f(\boldsymbol{Z},\boldsymbol{Z}^\ast)$|$\frac{\partial}{\partial\boldsymbol{Z}}f$|$\frac{\partial}{\partial\boldsymbol{Z}^\ast}f$|
|:---:|:---:|:---:|
| $\text{Tr}\{\boldsymbol{Z}\}$ | $\boldsymbol{I}_N$ | $\boldsymbol{0}_{N\times N}$ |
| $\text{Tr}\{\boldsymbol{Z}^{*}\}$ | $\boldsymbol{0}_{N\times N}$| $\boldsymbol{I}_N$ |
| $\text{Tr}\{\boldsymbol{AZ}\}$ | $\boldsymbol{A}^T$ | $\boldsymbol{0}_{N\times Q}$ |
| $\text{Tr}\{\boldsymbol{ZA}_0\boldsymbol{Z}^T\boldsymbol{A}_1\}$ | $\boldsymbol{A}^T_1\boldsymbol{ZA}_0^T+\boldsymbol{A}_1\boldsymbol{ZA}_0$ | $\boldsymbol{0}_{N\times Q}$ |
| $\text{Tr}\{\boldsymbol{ZA}_0\boldsymbol{Z}\boldsymbol{A}_1\}$ | $\boldsymbol{A}^T_1\boldsymbol{Z}^T\boldsymbol{A}_0^T+\boldsymbol{A}_0^T\boldsymbol{Z}^T\boldsymbol{A}_1^T$ | $\boldsymbol{0}_{N\times Q}$ |
| $\text{Tr}\{\boldsymbol{ZA}_0\boldsymbol{Z}^H\boldsymbol{A}_1\}$ | $\boldsymbol{A}^T_1\boldsymbol{Z}^\ast\boldsymbol{A}_0^T$ | $\boldsymbol{A}_1\boldsymbol{Z}\boldsymbol{A}_0$ |
| $\text{Tr}\{\boldsymbol{ZA}_0\boldsymbol{Z}^\ast\boldsymbol{A}_1\}$ | $\boldsymbol{A}^T_1\boldsymbol{Z}^H\boldsymbol{A}_0^T$ | $\boldsymbol{A}_0^T\boldsymbol{Z}^T\boldsymbol{A}_1^T$ |
| $\text{Tr}\{\boldsymbol{AZ}^{-1}\}$ | $-\left(\boldsymbol{Z}^T\right)^{-1}\boldsymbol{A}^T\left(\boldsymbol{Z}^T\right)^{-1}$ | $\boldsymbol{0}_{N\times N}$ |
| $\text{Tr}\{\boldsymbol{Z}^p\}$ | $p\left(\boldsymbol{Z}^T\right)^{p-1}$ | $\boldsymbol{0}_{N\times N}$ |
| $\det(\boldsymbol{Z})$ | $\det(\boldsymbol{Z})\left(\boldsymbol{Z}^T\right)^{-1}$ | $\boldsymbol{0}_{N\times N}$ |
| $\det(\boldsymbol{A}_0\boldsymbol{ZA}_1)$ | $\det(\boldsymbol{A}_0\boldsymbol{ZA}_1)\boldsymbol{A}_0^T\left(\boldsymbol{A}_1^T\boldsymbol{Z}^T\boldsymbol{A}_0^T\right)^{-1}\boldsymbol{A}_1^T$ | $\boldsymbol{0}_{N\times Q}$ |
| $\det\left(\boldsymbol{Z}^2\right)$ | $2\det^2(\boldsymbol{Z})\left(\boldsymbol{Z}^T\right)^{-1}$ | $\boldsymbol{0}_{N\times N}$ |
| $\det\left(\boldsymbol{ZZ}^T\right)$ | $2\det\left(\boldsymbol{ZZ}^T\right)\left(\boldsymbol{ZZ}^T\right)^{-1}\boldsymbol{Z}$ | $\boldsymbol{0}_{N\times Q}$ |
| $\det\left(\boldsymbol{ZZ}^\ast\right)$ | $\det\left(\boldsymbol{ZZ}^\ast\right)\left(\boldsymbol{Z}^H\boldsymbol{Z}^T\right)^{-1}\boldsymbol{Z}^H$ | $\det\left(\boldsymbol{ZZ}^\ast\right)\boldsymbol{Z}^T\left(\boldsymbol{Z}^H\boldsymbol{Z}^T\right)^{-1}$ |
| $\det\left(\boldsymbol{ZZ}^H\right)$ | $\det\left(\boldsymbol{ZZ}^H\right)\left(\boldsymbol{Z}^\ast\boldsymbol{Z}^T\right)^{-1}\boldsymbol{Z}^\ast$ | $\det\left(\boldsymbol{ZZ}^H\right)\boldsymbol{Z}^T\left(\boldsymbol{Z}\boldsymbol{Z}^H\right)^{-1}\boldsymbol{Z}$ |
| $\det\left(\boldsymbol{Z}^p\right)$ | $p\det^p(\boldsymbol{Z})\left(\boldsymbol{Z}^T\right)^{-1}$ | $\boldsymbol{0}_{N\times N}$ |
| $\lambda(\boldsymbol{Z})$ | $\frac{\boldsymbol{v_0}^{\ast}\boldsymbol{u}_0^T}{\boldsymbol{v}_0^H\boldsymbol{u}_0}$ | $\boldsymbol{N\times N}$ |
| $\lambda^\ast(\boldsymbol{Z})$ | $\boldsymbol{N\times N}$ | $\frac{\boldsymbol{v_0}\boldsymbol{u}_0^H}{\boldsymbol{v}_0^T\boldsymbol{u}_0^{\ast}}$ |

# Appendix: Proof

## Proof of T4

[back](#T4)

First of all, we prove $\mathcal{D}_{\boldsymbol{Z}^\ast}f=\left(\mathcal{D}_{\boldsymbol{Z}}f\right)^\ast$. Since $f$ is a real scalar function, we can have from the definition

$$
\begin{aligned}
   df&=(\mathcal{D}_{\boldsymbol{Z}}f)d\text{vec}(\boldsymbol{Z})+(\mathcal{D}_{\boldsymbol{Z}^\ast}f)d\text{vec}(\boldsymbol{Z}^\ast),\\
   df&=df^\ast=(\mathcal{D}_{\boldsymbol{Z}^\ast}f)^{\ast}d\text{vec}(\boldsymbol{Z})+(\mathcal{D}_{\boldsymbol{Z}}f)^{\ast}d\text{vec}(\boldsymbol{Z}^\ast),\\
\end{aligned}
$$

It is obvious to obtain the result by comparing these two equations. By further transforming the first equation by replacing the $\mathcal{D}_{\boldsymbol{Z}^\ast}f$ by $(\mathcal{D}_{\boldsymbol{Z}}f)^\ast$, we have

$$
df=2\mathfrak{R}\lbrace(\mathcal{D}_{\boldsymbol{Z}}f)d\ \text{vec}(\boldsymbol{Z})\rbrace=2\mathfrak{R}\lbrace(\mathcal{D}_{\boldsymbol{Z}^\ast}f)^{\ast}d\ \text{vec}(\boldsymbol{Z})\rbrace.
$$

Inside the $\mathfrak{R}(\cdot)$ function is a row vector multiplied by a column vector, which is can be written as a Euclidean inner product of two column vectors, i.e.

$$\boldsymbol{a}_0^H\boldsymbol{a}_1=\langle\boldsymbol{a}_0,\boldsymbol{a}_1\rangle.$$

Taking the $\mathfrak{R}(\cdot)$ function on both sides, we can write it as

$$\mathfrak{R}\lbrace\boldsymbol{a}_0^H\boldsymbol{a}_1\rbrace=\left\langle\begin{bmatrix}
  \mathfrak{R}\lbrace\boldsymbol{a}_0\rbrace \\
  \mathfrak{I}\lbrace\boldsymbol{a}_0\rbrace
\end{bmatrix},\begin{bmatrix}
  \mathfrak{R}\lbrace\boldsymbol{a}_1\rbrace \\
  \mathfrak{I}\lbrace\boldsymbol{a}_1\rbrace
\end{bmatrix}\right\rangle.$$

Therefore, the differential of $f$ becomes

$$df=2\left\langle\begin{bmatrix}
  \mathfrak{R}\lbrace(\mathcal{D}_{\boldsymbol{Z}^\ast}f)^T\rbrace \\
  \mathfrak{I}\lbrace(\mathcal{D}_{\boldsymbol{Z}^\ast}f)^T\rbrace 
\end{bmatrix},\begin{bmatrix}
  \mathfrak{R}\lbrace d\text{vec}(\boldsymbol{Z})\rbrace \\
  \mathfrak{I}\lbrace d\text{vec}(\boldsymbol{Z})\rbrace 
\end{bmatrix}\right\rangle.$$

According to the *Cauchy-Schwartz inequality*, the maximum inner product of vector $\boldsymbol{a}_0$ and $\boldsymbol{a}_1$ is achieved when they are at the same direction, i.e. $\boldsymbol{a}_0=k\boldsymbol{a}_1$, where $k$ is a constant. On the contrary, the minimum is achieved when they are at the opposite direction. Hence, the maximum value of $df$ occurs when $d\text{vec}(\boldsymbol{Z})=\alpha(\mathcal{D}_{\boldsymbol{Z}^\ast}f)^T$ for $\alpha>0$, and the minimum when $d\text{vec}(\boldsymbol{Z})=-\beta(\mathcal{D}_{\boldsymbol{Z}^\ast}f)^T$ for $\beta>0$.

It is worth to note that the inner product for complex vectors works only for Hermitian but not transpose, i.e., for $\boldsymbol{a},\boldsymbol{b}\in\mathbb{C}^{N\times 1}$,

$$<\boldsymbol{a},\boldsymbol{b}>=\boldsymbol{a}^H\boldsymbol{b}\neq\boldsymbol{a}^T\boldsymbol{b}.$$

# Appendix: Example

## Example: Derivate of Scalar Real-Valued Function Related to MIMO Channel

Consider a MIMO system with $N_t$ transmit antennas and $N_r$ receive antennas. $\boldsymbol{H}\in\mathbb{C}^{N_r\times N_t}$ denotes the static MIMO channel. With white zero-mean complex circularly symmetric Gaussian additive noise $\boldsymbol{n}\in\mathbb{C}^{N_r\times1}$, i.e. $\mathbb{E}[\boldsymbol{n}\boldsymbol{n}^H]=\boldsymbol{I}_{N_r}$, the relation between channel output signal $\boldsymbol{y}\in\mathbb{C}^{N_r\times 1}$ and the transmit signal $\boldsymbol{x}\in\mathbb{C}^{N_t\times1}$ is

$$\boldsymbol{y=Hx+n}.$$

The capacity of this MIMO channel was derived in (Telatar 1995) as

$$C=\ln\left(\det\left(I_{N_r}+\boldsymbol{HQH}^H\right)\right),$$

where $\boldsymbol{Q}=\mathbb{E}[\boldsymbol{xx}^H]$ is the covariance matrix of $\boldsymbol{x}$. Find the gradient of the capacity with respect to $\boldsymbol{H}$.

First of all, we can calculate the derivative of $C$

$$\begin{aligned}
  dC\overset{(a)}{=}&\text{Tr}\left\{\left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^{H}\right)^{-1}d\ \left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^H\right)\right\} \\
  =&\text{Tr}\left\{\left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^{H}\right)^{-1}\left(\boldsymbol{0}+d\ \left(\boldsymbol{HQH}^H\right)\right)\right\}\\
  \overset{(b)}{=}&\text{Tr}\left\{\left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^{H}\right)^{-1}(d\ \boldsymbol{H})\boldsymbol{QH}^H\right\}\\
  &+\text{Tr}\left\{\left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^{H}\right)^{-1}\boldsymbol{HQ}\left(d\ \boldsymbol{H}^H\right)\right\}\\
  \overset{(c)}{=}&\text{Tr}\left\{\boldsymbol{QH}^H\left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^{H}\right)^{-1}(d\ \boldsymbol{H})\right\}\\
  &+\text{Tr}\left\{\boldsymbol{Q}^T\boldsymbol{H}^T\left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^{H}\right)^{-T}\left(d\ \boldsymbol{H}^\ast\right)\right\}.
\end{aligned}$$

Let's explain the derivation above first. (a) is based on $d\ \ln\det(\boldsymbol{Z})=\text{Tr}\left\{\boldsymbol{Z}^{-1}d\boldsymbol{Z}\right\}$ (Hjorunges 2011, Proposition 3.14). (b) is due to the basic complex differential property $d\boldsymbol{Z}_0\boldsymbol{Z}_1=(d\boldsymbol{Z}_0\boldsymbol{Z}_1+\boldsymbol{Z}_0d\boldsymbol{Z}_1)$ (Hjorungnes 2011, Proposition 3.5)， which can be derived from the "procedure for finding complex differentials" in Section 3.2.1. (c) can be proved by the properties of trace function, $\text{Tr}\{\boldsymbol{AB}\}=\text{Tr}\{\boldsymbol{BA}\}$ and $\text{Tr}\{\boldsymbol{A}^T\}=\text{Tr}\{\boldsymbol{A}\}$.

Note that for a scalar real-valued function, the gradient is defined as the partial derivative with respect to the conjugate (Hjorungnes 2011, Eq. (4.48))

$$\nabla_{\boldsymbol{H}} C=\frac{\partial}{\partial\boldsymbol{H}^*}C=\left(\boldsymbol{Q}^T\boldsymbol{H}^T\left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^{H}\right)^{-T}\right)^T=\left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^{H}\right)^{-1}\boldsymbol{HQ}.$$

There are another equivalent expressions of $\nabla_{\boldsymbol{H}}C$. For example, according to the Sylvester's determinant identity, the capacity can be rewritten as

$$C=\ln\left(\det\left(\boldsymbol{I}_{N_r}+\boldsymbol{H}^H\boldsymbol{HQ}\right)\right)$$, resulting in the gradient

$$\nabla_{\boldsymbol{H}}C=\frac{\partial}{\partial\boldsymbol{H}^\ast}f=\boldsymbol{HQ}\left(\boldsymbol{I}_{M_r}+\boldsymbol{HQH}^{H}\right)^{-1}.$$

# References

