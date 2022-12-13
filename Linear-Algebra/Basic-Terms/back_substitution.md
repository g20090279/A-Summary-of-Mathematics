The process of solving a linear system of equations that has been transformed into row-echelon form. The last equation is solved first, then the next-to-last, etc.

Example: To solve a linear system where $x=[x_1,x_2,x_3]^T$ is the vector unknown variable

$$Ax=b,$$

where

$$A=\begin{bmatrix}1&-2&1\\0&1&6\\0&0&1\end{bmatrix},b=\begin{bmatrix}4\\-1\\2\end{bmatrix},$$

we can write the problem in a row-echelon form for its augmented matrix

$$\left[\begin{matrix}1&-2&1\\0&1&6\\0&0&1\end{matrix}\middle\vert\begin{matrix}4\\-1\\2\end{matrix}\right].$$

The equations for the system become

$$\begin{aligned}
  x-2y+z&=4\\
  y+6z&=-1\\
  z&=2   
\end{aligned}$$

The last equation says $z=2$. Substitute this into the second equation to get

$$\begin{aligned}
   y+6(2)&=-1\\
   y&=-13 
\end{aligned}$$

Now substitute $z=2$ and $y=-13$ into the first equation to get

$$\begin{aligned}
   x-2(-13)+(2)&=4\\
   x&=-24 
\end{aligned}$$

Thus the solution is $x=-24$, $y=-13$ and $z=2$.