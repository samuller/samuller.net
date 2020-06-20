---
layout: post
title:  "Matrices"
categories: math
header: mathematics
---

A matrix is a two dimensional series of numbers:

$$
\mathbf{A}_{m\times n} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \ldots & a_{mn}\\
\end{bmatrix} = [a_{ij}] \in \mathbb{R}^{m\times n}
$$

## Notation

Matrices are often indicated by using an upper-case letter printed in boldface, e.g. $\mathbf{A}$, while the corresponding lower-case letter with two subscript indices represent the entries in the matrix, e.g. $a_{ij}$ (for an entry located in row $i$ and column $j$).

The matrix dimension (size) is written as $m\times n$ where $m$ is the number of rows and $n$ the number of columns (i.e. row $\times$ columns)

## Types by form

* **Rectangular matrix**: Any matrix with a size of $m\times n$.
* **Square matrix**: Any matrix with a size of $n\times n$ (i.e. $m = n$).

## Types by content

All the following matrices are square:

**Zero matrix**: Whole matrix only contains zeros. Matrix is called $\mathbf{0}$.

Example:
$$
\begin{bmatrix}
0 & 0 & 0\\
0 & 0 & 0\\
0 & 0 & 0\\
\end{bmatrix}
$$

**Diagonal matrix**: Contains zeros, except on the main diagonal.

Example:
$$
\begin{bmatrix}
2 & 0 & 0\\
0 & 8 & 0\\
0 & 0 & 3\\
\end{bmatrix}
$$

**Identity matrix**: Is a diagonal matrix that only has ones on the main diagonal. Matrix is call $\mathbf{I}$.

Example:
$$
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\\
\end{bmatrix}
$$

**Scalar matrix**: Is the product of a constant with the identity matrix.

Example:
$$
\begin{bmatrix}
5 & 0 & 0\\
0 & 5 & 0\\
0 & 0 & 5\\
\end{bmatrix}
$$

**Lower triangular matrix**: All values above the main diagonal are zero.

Example:
$$
\begin{bmatrix}
5 & 0 & 0 & 0\\
1 & 3 & 0 & 0\\
4 & 3 & 9 & 0\\
8 & 2 & 7 & 6\\
\end{bmatrix}
$$

**Upper triangular matrix**: All values below the main diagonal are zero

Example:
$$
\begin{bmatrix}
4 & 8 & 7 & 6\\
0 & 9 & 2 & 3\\
0 & 0 & 1 & 5\\
0 & 0 & 0 & 3\\
\end{bmatrix}
$$

**Triangular matrix**: Is either an upper or lower triangular matrix.

## Types for calculations

**Transponent matrix**: The transponent of a matrix $\mathbf{A}$ is the mirror image of the matrix with main diagonal as the symmetry axis and is written as $\mathbf{A}^{T}$.

**Symmetric matrix**: A matrix $\mathbf{A}$ is symmetrical if $\mathbf{A} = \mathbf{A}^T$.

**Inverse matrix**: The inverse of the matrix $\mathbf{A}$ is written as $\mathbf{A}^{-1}$.

**Orthogonal matrix**: If $\mathbf{A}^{-1} = \mathbf{A}^{T}$ then $\mathbf{A}$ is an orthogonal matrix.

## Rules

With matrices $\mathbf{A}\_{m\times n}$ and $\mathbf{B}\_{m\times n}$ (i.e. same sizes) the following applies:

$k\cdot \mathbf{A} = [k\cdot a_{ij}]_{m\times n} \qquad \\{k \in \mathbb{R}\\}$

$1\cdot\mathbf{A} = \mathbf{A}$

$\mathbf{A}+\mathbf{B} = [a_{ij}+b_{ij}]_{m\times n}$

$\mathbf{A}+\mathbf{B} = \mathbf{B}+\mathbf{A}$

$\mathbf{A}+(\mathbf{B}+\mathbf{C}) = (\mathbf{A}+\mathbf{B})+\mathbf{C}$
$(k_1k_2)\mathbf{A} = k_1(k_2\mathbf{A})$

$k_1(\mathbf{A}+\mathbf{B}) = k_1\mathbf{A} + k_1\mathbf{B}$

$(k_1+k_2)\mathbf{A} = k_1\mathbf{A} + k_1\mathbf{A}$

Unlike scalar multiplication ($k\cdot \mathbf{A}$), matrix multiplication requires matrices with the same *inner dimension*, i.e. with $\mathbf{A}\_{m\times p}$ and $\mathbf{B}\_{p\times n}$ the following applies:

$\displaystyle \mathbf{A}\cdot \mathbf{B} = \mathbf{C}\_{m\times n} = [c\_{rk}] = \sum^p\_{i=1}a\_{ri}b\_{ik}$

$\mathbf{A}\cdot\mathbf{B} \not\equiv \mathbf{B}\cdot\mathbf{A}$ (the order of the product is important - matrix multiplication is not *commutative*)

With matrices $\mathbf{A}\_{n\times n}$, $\mathbf{B}\_{n\times n}$ and $\mathbf{X}_{n\times n}$ the following applies:

If $\displaystyle \mathbf{A}\cdot \mathbf{X} = \mathbf{B}$ then $\displaystyle \mathbf{X} = \mathbf{A}^{-1}\cdot\mathbf{B}$
