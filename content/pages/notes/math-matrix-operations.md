---
layout: post
title:  "Matrix operations"
categories: math
header: mathematics
---

## Transponent

If
$$
\mathbf{A} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \ldots & a_{mn}\\
\end{bmatrix}_{m\times n}
$$
then
$$
\mathbf{A}^T = \begin{bmatrix}
a_{11} & a_{21} & \cdots & a_{m1}\\
a_{12} & a_{22} & \cdots & a_{m2}\\
\vdots & \vdots & \ddots & \vdots\\
a_{1n} & a_{2n} & \ldots & a_{mn}\\
\end{bmatrix}_{m\times n}
$$

The transposed matrix $\mathbf{A}^T$ is a mirror image of $\mathbf{A}$ where the symmetry-axis is the main diagonal. Transposing is thus an operation where the columns of a matrix are swapped with its rows and has no effect on the values on the main diagonal.

### Transponent rules

$(\mathbf{A}^T)^T = \mathbf{A}$

$(\mathbf{A}+\mathbf{B})^T = \mathbf{A}^T + \textbf{B}^T$

$(\mathbf{A}\mathbf{B})^T = \mathbf{B}^T\mathbf{A}^T$

$(k\mathbf{A})^T = k\mathbf{A}^T$

## Cofactors

$$
\mathbf{A} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & a_{rk} & \vdots\\
a_{m1} & a_{m2} & \ldots & a_{mn}\\
\end{bmatrix}
$$

Every element in a matrix has a *cofactor*. The cofactor for $a_{rk}$ (at row $r$ and column $k$ in $\mathbf{A}$) is called $C_{rk}.$ The cofactor is determined with the following calculation:

$$C_{rk} = (-1)^{r+k}\cdot \mathbf{M}_{rk}$$

where $\mathbf{M}_{rk}$ is the determinant of a matrix which is the same as the matrix $\mathbf{A}$, but with row $r$ and column $k$ removed (giving it one less row and column dimensions).

Cofactors are generally necessary to calculate a few properties of matrices, but also have themselves the interesting property that if the elements of one row are respectively multiplied with the cofactors of another row, and then summed together, the total is zero. Thus $a_{i1}\cdot C_{k1}+a_{i2}\cdot C_{k2}+\ldots +a_{in}\cdot C_{kn} = 0$ where $i \neq k$.

## Determinant

The determinant is a numerical value that can only be calculated for square matrices. The notation for the determinant is $\operatorname{det}\mathbf{A}$ or $\|\mathbf{A}\|$. The determinant has an order of $n$ if $\mathbf{A}$ has a dimension of $n\times n$. The determinant for lower orders as follows:

For $\mathbf{A}_{1\times1} = [a\_{11}]$ the $\operatorname{det}\mathbf{A} = \|a\_{11}\|=a\_{11}$

For
$$
\mathbf{A}_{2\times2} =
\begin{bmatrix}
a_{11} & a_{12}\\
a_{21} & a_{22}\\
\end{bmatrix}
$$ the
$$
\operatorname{det}\mathbf{A} = \begin{vmatrix}
a_{11} & a_{12}\\
a_{21} & a_{22}\\
\end{vmatrix}= a_{11}\cdot a_{22}-a_{12}\cdot a_{21}
$$

For
$$
\mathbf{A}_{3\times3} =
\begin{bmatrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}\\
\end{bmatrix}
$$ the
$$
\operatorname{det}\mathbf{A} = \begin{vmatrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}\\
\end{vmatrix}
$$

$$
\begin{align}
=&\quad\ (a_{11}\cdot a_{22}\cdot a_{33}) + (a_{12}\cdot a_{23}\cdot a_{31}) + (a_{13}\cdot a_{21}\cdot a_{32})\\
& - (a_{11}\cdot a_{23}\cdot a_{32}) - (a_{12}\cdot a_{21}\cdot a_{33}) - (a_{13}\cdot a_{22}\cdot a_{31})
\end{align}
$$

For higher orders the determinant has to be calculated through *cofactor expansion*, or by using the determinant rules and known determinants. Cofactor expansion requires calculating lower order determinants. With cofactor expansion the determinant of any matrix $\mathbf{A}_{n\times n}$ is just the cofactor expansion of any row $r$:

$$\operatorname{det}\mathbf{A} = a_{r1}\cdot C_{r1}+a_{r2}\cdot C_{r2}+\ldots + a_{rn}\cdot C_{rn}$$

The determinant for any triangular matrix is just the product of the elements on the main diagonal.

### Rule of Sarrus

The "Rule of Sarrus" is a method to remember the determinant of a $3\times3$ matrix. Write down the matrix's entries twice next to each other. Multiply the elements in each 3-length diagonal with each other. Diagonals that move from top-left to bottom-right should be added and diagonals that move from top-right to bottom-left should be subtracted.

<div class="svg-center-overlay">
<svg height="210" width="740">
    <!-- w=740, w/2=370, h=+30 -->
    <line x1="245" y1="0" x2="360" y2="75" style="stroke:rgb(var(--text-color-rgb));stroke-width:2" />
    <line x1="292" y1="0" x2="407" y2="75" style="stroke:rgb(var(--text-color-rgb));stroke-width:2" />
    <line x1="339" y1="0" x2="454" y2="75" style="stroke:rgb(var(--text-color-rgb));stroke-width:2" />
    <line x1="400" y1="0" x2="290" y2="75" style="stroke:rgb(var(--text-color-rgb));stroke-width:2" />
    <line x1="443" y1="0" x2="333" y2="75" style="stroke:rgb(var(--text-color-rgb));stroke-width:2" />
    <line x1="486" y1="0" x2="376" y2="75" style="stroke:rgb(var(--text-color-rgb));stroke-width:2" />
</svg>
</div>
<div>
$$
\begin{matrix}
a_{11} & a_{12} & a_{13} & a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23} & a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33} & a_{31} & a_{32} & a_{33}\\
\end{matrix}
$$
</div>

<!--
$$
\begin{picture}(5,5)
\put(5,15){\line(2,-1){50}}
\put(30,15){\line(2,-1){50}}
\put(55,15){\line(2,-1){50}}
\put(75,15){\line(-2,-1){50}}
\put(100,15){\line(-2,-1){50}}
\put(125,15){\line(-2,-1){50}}
$\begin{matrix}
a_{11} & a_{12} & a_{13} & a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23} & a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33} & a_{31} & a_{32} & a_{33}\\
\end{matrix}$
\end{picture}
$$
-->

### Determinant rules

$\operatorname{det}\mathbf{A} = \operatorname{det}\mathbf{A}^T$ (the determinant handles rows and columns identically)

$\operatorname{det}(\mathbf{A}\mathbf{B}) = \operatorname{det}\mathbf{A}\cdot \operatorname{det}\mathbf{B}$

$\operatorname{det}\mathbf{A} = 0$ if a row/column of $\mathbf{A}$ contains only zeros

$\operatorname{det}\mathbf{A} = 0$ if two rows/columns of $\mathbf{A}$ are identical

$-\operatorname{det}\mathbf{A} = \operatorname{det}\mathbf{B}$ if $\mathbf{B}$ is a matrix obtained by swapping any two rows/columns of the matrix $\mathbf{A}$

$k\cdot \operatorname{det}\mathbf{A} = \operatorname{det}\mathbf{B}$ if $\mathbf{B}$ is a matrix obtained by multiplying a single row/column of matrix $\mathbf{A}$ with a non-zero number $k$

$\operatorname{det}\mathbf{A} = \operatorname{det}\mathbf{B}$ if $\mathbf{B}$ is a matrix obtained from $\mathbf{A}$ by multiplying a row/column with a non-zero number $k$ and then adding the result to another row/column's respective elements

$\operatorname{det}\mathbf{A} = a_{11}\cdot a_{22}\ldots a_{nn}$ (the product of the elements on the main diagonal) if $\mathbf{A}$ is a triangular matrix

## Adjugate matrix

The adjugate of $\mathbf{A}$ is a matrix that is created by replacing the entries of the matrix $\mathbf{A}$ with their cofactors and then transposing it:

$$
\operatorname{adj}\mathbf{A} = \mathbf{C}^T = \begin{bmatrix}
C_{11} & C_{12} & \cdots & C_{1n}\\
C_{21} & C_{22} & \cdots & C_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
C_{m1} & C_{m2} & \ldots & C_{mn}\\
\end{bmatrix}^T =
\begin{bmatrix}
C_{11} & C_{21} & \cdots & C_{m1}\\
C_{12} & C_{22} & \cdots & C_{m2}\\
\vdots & \vdots & \ddots & \vdots\\
C_{1n} & C_{2n} & \ldots & C_{mn}\\
\end{bmatrix}
$$

## Inverse

The inverse of the $\mathbf{A}$ can be calculated with:

$$\mathbf{A}^{-1} = \operatorname{det}\mathbf{(A)}^{-1} \cdot \operatorname{adj}\mathbf{(A)} = \frac{1}{\operatorname{det}\mathbf{A}}\cdot \operatorname{adj}\mathbf{A}$$

The inverse of a matrix $\mathbf{A}$ is the matrix $\mathbf{A}^{-1}$ such that the product of the matrix and its inverse is equal to the identity matrix:

$\therefore \mathbf{A}\cdot\mathbf{A}^{-1} = \mathbf{I}$

If such a matrix does not exist then the matrix $\mathbf{A}$ is not *invertible* and is called a *singular matrix*.

The inverse can also be calculated by finding a few valid operation whereby $\mathbf{A}$ can be transformed into $\mathbf{I}$, and then applying those operations to $\mathbf{I}$. Valid operations include: swapping rows, scalar multiplication of a row with a constant and replacing a row with the sum of that row and any other row.
