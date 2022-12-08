[Parition of A Matrix / 矩阵的分割] [Submatrix / 子矩阵] [Block Matrix / 方块矩阵]

# Parition of A Matrix

> A *parition* of a set $\mathbb{S}$ is a collection of subsets of $\mathbb{S}$ such that each element of $\mathbb{S}$ is a member of one and only one of the subsets. (Horn 2013, C0.7)

One example is the *sequential partition* of ${1,2,\cdots,n}$, for example, with 3 partitions, $\alpha_1={1,\cdots,i_1}$, $\alpha_2={i_1+1,\cdots,i_2}$ and $\alpha_3={i_2_1,\cdots,n}$.

> **Definition**. A *partition* of a matrix is a decomposition of the matrix into submatrices such that each entry of the original matrix is in one and only one of the submatrices. (Horn 2013, C0.7)

Paritioning a matrix is useful in practical use. One simple example of partitioning a matrix $\mathbf{B}\in\mathbf{M}_n(\mathbf{F})$ into a group of column-vectors $\mathbf{B}=[\boldsymbol{b}_1,\cdots,\boldsymbol{b}_n]$ so that the multiplication of two matrices $\mathbf{A}$ and $\mathbf{B}$ can be written as

$$\mathbf{AB}=\mathbf{A}[\boldsymbol{b}_1,\cdots,\boldsymbol{b}_n]=[\mathbf{A}\boldsymbol{b}_1,\cdots,\mathbf{A}\boldsymbol{b}_n].$$

# Submatrices
