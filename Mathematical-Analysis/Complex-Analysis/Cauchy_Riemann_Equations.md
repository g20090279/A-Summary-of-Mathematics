- Topics: Cauchy-Riemann Equations
- Last Revised: Nov. 06, 2023

---

The Cauchy-Riemann equations are a set of partial differential equations that describe the necessary and sufficient conditions for a complex-valued function to be differentiable.

# Definition of Analytic (Holomorphic) Function in Complex Analysis

This equations is relative the definition of *analytic* or *holomorphic* function in complex analysis. First of all, let's see what is the analytic function

**Definition**: Let $\mathcal{D}\subseteq\mathbb{C}$ be the domain of definition of function $f:\mathcal{D}\rightarrow\mathbb{C}$. The function $f$ is an analytic function in the domain $\mathcal{D}$ if

$$\lim_{\Delta z\rightarrow0}\frac{f(z+\Delta z)-f(z)}{\Delta z}$$

exists for all $z\in\mathcal{D}$. $\square$

Note that the analyticity of a function in complex analysis is very strict, in the sense of two dimensionality of complex number other than only one dimension in real numbers. More exactly, the limitation in the real-imaginary plane can be approached in any direction, e.g. from the real axis, or the imaginary axis.

# Derivation of Cauchy-Riemann Equations

Lets assume that the real axis is horizontal while the imaginary axis is vertical. For a complex number $z=x+iy$, where $i$ is the imaginary unit. Now, the limitation is approached horizontally, i.e. by the real part of $z$

$$\lim_{\Delta z\rightarrow0}\frac{f(z+\Delta z)-f(z)}{\Delta z}=\lim_{t\rightarrow0}\frac{f(z+t)-f(z)}{t}$$ 

where $t$ is a real number. Similarly, it can approach $z$ from the imaginary axis

$$\lim_{\Delta z\rightarrow0}\frac{f(z+\Delta z)-f(z)}{\Delta z}=\lim_{t\rightarrow0}\frac{f(z+it)-f(z)}{it}.$$

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

The results of limit approaching horizontally and vertically should be the same. Therefore, we have finally the *Cauchy-Riemann Equation*

$$\left.\frac{\partial u}{\partial x}\right|_{(x,y)}=\left.\frac{\partial v}{\partial y}\right|_{(x,y)},\quad \left.\frac{\partial u}{\partial y}\right|_{(x,y)}=-\left.\frac{\partial v}{\partial x}\right|_{(x,y)}.$$

It is convenient to employ the usual shorthand for partial derivatives

$$u_x(x,y)=v_y(x,y),\quad u_y(x,y)=-v_x(x,y),$$

which can be further simplified to

$$u_x=u_y,\quad u_y=-v_x.$$

**Remark**: The Cauchy-Riemann equations can be written in a single complex equation instead of two equations as

$$f_y=i\cdot f_x.$$

$\square$

**Theorem**: Let $f(z)=u(x,y)+iv(x,y)$ and suppose the partial derivatives $u_x,u_y,v_x$ and $v_y$ are continuous at $(x_0,y_0)$ and satisfy the Cauchy-Riemann equations there. Then $f(z)$ is differentiable at $z_0=x_0+iy_o$. $\square$

# Interpretation of Cauchy-Riemann Equations

# Applications

The Cauchy-Riemann equations have numerous applications in complex analysis, 