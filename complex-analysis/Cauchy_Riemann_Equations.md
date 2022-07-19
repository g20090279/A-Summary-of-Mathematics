[Cauchy-Riemann Equations]

# Definition of Analytic Function in Complex Analysis

This equations is relative the definition of *analytic* function in complex analysis. First of all, let's see what is the analytic function

**Definition**. Let $D\subseteq\mathbb{C}$ be the domain of definition of function $f:D\rightarrow\mathbb{C}$. The function $f$ is an analytic function in the domain $D$ if

$$\lim_{\Delta z\rightarrow0}\frac{f(z+\Delta z)-f(z)}{\Delta z}$$

exists for all $z\in\D$. $\square$

Note that the analyticity of a function in complex analysis is very strict, in the sense of two dimensionality of complex number other than only one dimension in real numbers. More exactly, the limitation in the real-imaginary plane can be approached in any direction, e.g. from the real axis, or the imaginary axis.

# Derivation of Cauchy-Riemann Equations

Lets assume that the real axis is horizontal while the imaginary axis is vertical. For a complex number $z=x+iy$, where $i$ is the imaginary unit. Now, the limitation is approached horitzontally, i.e. by the real part of $z$

$$\lim_{\Delta z\rightarrow0}\frac{f(z+\Delta z)-f(z)}{\Delta z}=\lim_{t\rightarrow0}\frac{f(z+t)-f(z)}{t}$$ 

where $t$ is a real number. Similarly, it can approach $z$ from the imaginary axis

$$\lim_{\Delta z\rightarrow0}\frac{f(z+\Delta z)-f(z)}{\Delta z}=\lim_{t\arrightarrow0}\frac{f(z+it)-f(z)}{it}.$$

Now, considering the function with respect to its real part and imaginary part

$$f(z(x,y))=u(x,y)+iv(x,y),$$

the horizontal limit becomes

$$\begin{aligned}
\lim_{t\rightarrow0}\frac{f(z+t)-f(z)}{t}&=\lim_{t\rightarrow0}\frac{u(x+t,y)+iv(x+t,y)-u(x,y)-iv(x,y)}{t}\\
&=\lim_{t\rightarrow0}\frac{u(x+t,y)-u(x,y)}{t}+\lim_{t\rightarrow0}\frac{iv(x+t,y)-iv(x,y)}{t}\\
&=\left.\frac{\partial u}{\partial x}\right|_{(x,y)}+i\left.\frac{\partial v}{\partial x}\right|_{(x,y)}.
\end{aligned}$$

On the other hand, the vertical limit becomes

$$\begin{aligned}
\lim_{t\rightarrow0}\frac{f(z+it)-f(z)}{it}&=\lim_{t\rightarrow0}\frac{u(x,y+t)+iv(x,y+t)-u(x,y)-iv(x,y)}{it}\\
&=-i\lim_{t\rightarrow0}\frac{u(x,y+t)-u(x,y)}{t}-i\lim_{t\rightarrow0}\frac{iv(x,y+t)-iv(x,y)}{t}\\
&=\lim_{t\rightarrow0}\frac{v(x,y+t)-v(x,y)}{t}-i\lim_{t\rightarrow0}\frac{u(x,y+t)-u(x,y)}{t}\\
&=\left.\frac{\partial v}{\partial y}\right|_{(x,y)}-i\left.\frac{\partial u}{\partial y}\right|_{(x,y)}.
\end{aligned}$$

The results of limit approaching horizontally and vertially should be the same. Therefore, we have finally the Cauchy-Riemann Equation

$$\left.\frac{\partial u}{\partial x}\right|_{(x,y)}=\left.\frac{\partial v}{\partial y}\right|_{(x,y)},\quad \left.\frac{\partial u}{\partial y}\right|_{(x,y)}=-\left.\frac{\partial v}{\partial x}\right|_{(x,y)}.$$

It is convenient to emply the usual shorthand for partial derivatives

$$u_x(x,y)=v_y(x,y),\quad u_y(x,y)=-v_x(x,y),$$

which can be further implified to

$$u_x=u_y,\quad u_y=-v_x.$$

# Cauchy-Riemann Equation Determines the Analyticity of a Function

$$Theorem$$. Lef $f:D\rightarrow\mathbb{C}$ be a continuous function. Then $f$ is holomorphic if and only if the partial derivatives of $u$ and $v$ exist and satisfy the Cauchy-Riemann equations. $\square$.
