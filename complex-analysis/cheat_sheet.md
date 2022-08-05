# Introduction

## Symbols and sizes of input variables and functions

The variable is denoted by the letter $z$ (for scalar, or $\boldsymbol{z}$ for vector and $\boldsymbol{Z}$ for matrix. Same rules for other letters). Letter like a or b represent constant.

|Symbol|$z$|$\boldsymbol{z}$|$\boldsymbol{Z}$|$f$|$\boldsymbol{f}$|$\boldsymbol{F}$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Size|$1\times1$|$N\times1$|$N\times Q$|$1\times1$|$M\times1$|$M\times P$|

## Classification of function

|Function type|$z,z^*\in\mathbb{C}$|$\boldsymbol{z},\boldsymbol{z}^*\in\mathbb{C}^{N\times1}$|$\boldsymbol{Z},\boldsymbol{Z}^*\in\mathbb{C}^{N\times Q}$|
|:---:|:---:|:---:|:---:|

# Some Definitions

|Name of Definition|Mathematical Description|
|:---:|:---:|
|Analytic Function (also called complex differentiable, holomorphic, regular)|The function $f$ is an analytic function if $\lim_{\Delta z\rightarrow0}\frac{f(z+\Delta z)-f(z)}{\Delta z}$ exists for all $z\in\mathcal{D}$, where $\mathcal{D}$ is a subset of $\mathbb{C}$ and the domain of the function.|
|Formal Derivation / Wirtinger Derivatives | Let $z=x+iy$, where $x,y\in\mathbb{R}$.<br/> $\frac{\partial}{\partial z}f(z,z^{\ast})=\frac{1}{2}\left(\frac{\partial}{\partial x}f-i\frac{\partial}{\partial y}f\right)$ <br/> $\frac{\partial}{\partial z^\ast}f(z,z^\ast)=\frac{1}{2}\left(\frac{\partial}{\partial x}f+i\frac{\partial}{\partial y}f\right)$ <br /> The variables $z$ and $z^\ast$ are treated as independent variables.|

# Procedure for Finding Complex Differentials

Consider a complex matrix function $\boldsymbol{F}:\mathbb{C}^{N\times Q}\times\mathbb{C}^{N\times Q}\rightarrow\mathbb{C}^{M\times P}$ with two input complex-valued matrix variables $\boldsymbol{Z}_0\in\mathbb{C}^{N\times Q}$ and $\boldsymbol{Z}_1\in\mathbb{C}^{N\times Q}$, the difference of a infinitesimal increment is

$$\begin{aligned}
    \boldsymbol{F}(&\boldsymbol{Z}_0+d\boldsymbol{Z}_0,\boldsymbol{Z}_1+d\boldsymbol{Z}_1)-\boldsymbol{F}(\boldsymbol{Z}_0,\boldsymbol{Z}_1)\\
    &=\text{First-order}(d\boldsymbol{Z}_0,d\boldsymbol{Z}_1)+\text{Higher-order}(d\boldsymbol{Z}_0,d\boldsymbol{Z}_1).
\end{aligned}$$

The First-order() term depends on the first order of $d\boldsymbol{Z}_0$ or $d\boldsymbol{Z}_1$. The differential is then given by the **first-order term**.

# Basic complex differential properties

|Properties|Comment|
|:---:|:---:|
|$d\boldsymbol{A}=\boldsymbol{0}_{M\times P}$|$\boldsymbol{A}\in\mathbb{C}^{M\times P}$ is a constant matrix that independent of $\boldsymbol{Z}$ or $\boldsymbol{Z}^{*}$|
|$d(\boldsymbol{AZB})=\boldsymbol{A}(d\boldsymbol{Z})\boldsymbol{B}$|$\boldsymbol{A}$ and $\boldsymbol{B}$ are constants|
|$d(a\boldsymbol{Z})=ad\boldsymbol{Z}$||
|$d(\boldsymbol{Z}_0+\boldsymbol{Z}_1)=d\boldsymbol{Z}_0+d\boldsymbol{Z}_1$||
|$d\left(\text{Tr}\left\{\boldsymbol{Z}\right\}\right)=\text{Tr}\left\{d\boldsymbol{Z}\right\}$||
|$d(\boldsymbol{Z}_0\boldsymbol{Z}_1)=(d\boldsymbol{Z}_0)\boldsymbol{Z}_1+\boldsymbol{Z}_0(d\boldsymbol{Z}_1)$||
|$d(\boldsymbol{Z}_0\otimes\boldsymbol{Z}_1)=(d\boldsymbol{Z}_0)\otimes\boldsymbol{Z}_1+\boldsymbol{Z}_0\otimes(d\boldsymbol{Z}_1)$|Kronecker product|
|$d(\boldsymbol{Z}_0\odot\boldsymbol{Z}_1)=(d\boldsymbol{Z}_0)\odot\boldsymbol{Z}_1+\boldsymbol{Z}_0\odot(d\boldsymbol{Z}_1)$|Hadamard product|
|$d\boldsymbol{Z}^{-1}=-\boldsymbol{Z}^{-1}(d\boldsymbol{Z})\boldsymbol{Z}^{-1}$|matrix inverse|
|$d\ \text{reshape}(\boldsymbol{Z})=\text{reshape}(d\boldsymbol{Z})$|reshape|
|$d\boldsymbol{Z}^\ast=(d\boldsymbol{Z})^\ast$|conjugate|
|$d\boldsymbol{Z}^{H}=(d\boldsymbol{Z})^H$|complex conjugate|
|$d\det(\boldsymbol{Z})=\text{Tr}\left\{\boldsymbol{C}^T(\boldsymbol{Z})d\boldsymbol{Z}\right\}$|where $\boldsymbol{C}(\boldsymbol{Z})$ is a $N$-size square matrix containing cofactors. determinant and trace|