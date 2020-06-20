---
layout: post
title:  "Cartesian graphing"
categories: math
header: mathematics
---

Strategy for graphing arbitrary functions (partially focused on polinomials):

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
