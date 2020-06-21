---
layout: post
title:  "Cartesian graphing"
categories: math
header: mathematics
---

## Transformations

With the graph for $y = f(x)$ already known.

Translating/shifting:

- $y = f(x - c)$  
Replacing $x$ with $x - c$ will translate/shift the graph along the $x$-axis, moving it rightward by $c$.
- $y = f(x) + c$  
Replacing $y$ with $y - c$ will translate/shift the graph along the $y$-axis, moving it upward by $c$.

Stretching/shrinking:

- $y = f(a\cdot x)$  
Replacing $x$ with $a\cdot x$ will shrink the graph on the $x$-axis by a factor of $a$.
- $y = \frac{f(x)}{a}$  
Replacing $y$ with $a\cdot y$ will shrink the graph on the $y$-axis by a factor of $a$.
- $y = f(\frac{x}{a})$  
Replacing $x$ with $\frac{x}{a}$ will stretch the graph on the $x$-axis by a factor of $a$.
- $y = a\cdot f(x)$  
Replacing $y$ with $\frac{y}{a}$ will stretch the graph on the $y$-axis by a factor of $a$.

Flipping/mirroring:

- $y = f(-x)$  
Replacing $x$ with $-x$ will create flipped mirror image with $y = 0$ as the symmetry axis.
- $y = -f(x)$  
Replacing $y$ with $-y$ will create flipped mirror image with $x = 0$ as the symmetry axis.
- $y = f^{-1}(x)$ or $x = f(y)$  
Swapping $x$ and $y$ is sometimes no longer a function, but will create the inverse graph which is a flipped mirror image with $x = y$ as the symmetry axis.

## Strategy

Strategy for drawing/graphing arbitrary functions (some steps only apply to polinomials):

1. Find intersections with $x$-axis and $y$-axis
    - Find $f(0)$ and $f(x) = 0$
    - Use Newton's method to find approximate roots
2. Find *critical points*
    - Where $f'(x)$ equals 0 or doesn't exist
3. Find *local minima* and *maxima* and where function rises or falls
    - Use the sign of $f'(x)$
    - Use the sign of $f^{\prime\prime}(x)$ where $f'(x) = 0$ ($f^{\prime\prime}(x) = 0$ won't help)
4. Find *inflection points* / *concavity*
    - Where $f^{\prime\prime}(x) = 0$ and sign changes
    - If $f^{\prime\prime}(x) > 0$, function is concave upwards
    - If $f^{\prime\prime}(x) < 0$, function is concave downwards
5. Find *asymptotes*
    - Vertical asymptote
        - Look for where function might divide by zero
    - Horizontal asymptote
        - Not applicable if function is only defined on a limited interval
        - Possible if function contains division
        - Attempt limit of $f(x)$ as $x$ approaches $- \infty$ and $\infty$ (left and right)
        - Divide fraction by $x^n$ (above and below) with $n$ the highest power in the numerator
    - Diagonal asymptote
        - Not applicable if function is only defined on a limited interval
        - Same as for horizontal asymptote
        - Use long division te remove division
        - Put formula in the form $f(x) - (mx + c)$

<!--
Cartesian axes
Functions

Rotations require implicit graphs
-->
