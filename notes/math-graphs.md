---
layout: post
title:  "Cartesian graphs"
categories: math
header: mathematics
---

These graphs are all specified as functions on the cartesian coordinate system. Since functions only have one output value for each input, these cases exclude implicit functions or more canonical forms.

<!--
$x$ is the independent variable
$y$ is the dependent variable
-->

## Straight line

![straight line graph](/img/math/x+1.svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$y = mx + c$$

Interpretation of constants:

- $m$: slope or gradient of the line
- $c$: $y$-intercept

Properties:

- Gradient = $\dfrac{y_1 - y_0}{x_1 - x_0} = \dfrac{\Delta y}{\Delta x} = \tan\theta = m$

## Parabola

![parabola graph](/img/math/-x^2 + 3.svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$y = ax^2 + bx + c$$

$$y = a(x + p)^2 + q$$

Interpretation of constants:

- $a$: width and direction in which parabola opens up
  - $a > 0$: opens upward
  - $a < 0$: opens downward
  - smaller $\|a\|$ leads to wider parabola
- $a$ and $b$: determines $x$-position of vertex (turning point)
  - $a\times b > 0$: vertex at negative $x$
  - $a\times b < 0$: vertex at positive $x$
- $c$: $y$-intercept

Properties:

- Vertex/Symmetry axis at $(p,q)$ or $\left(\dfrac{b}{2a}, -\dfrac{b^2 - 4ac}{4a}\right)$
- $\Delta = b^2 - 4ac$, called the discriminant, determines number of solutions or $x$-intercepts
  - $\Delta > 0$: 2 solutions
  - $\Delta = 0$: 1 solution
  - $\Delta < 0$: no solutions

## Hyperbola

![hyperbola graph](/img/math/xy=1.svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$xy = k$$

Interpretation of constants:

- $k$ determines which line forms the symmetry axis called the *major axis* and the distance between the vertices
  - $k > 0$: the $y = x$ line forms the major axis
  - $k < 0$: the $y = -x$ line forms the major axis
  - distance between vertices is $2\sqrt{2k}$

Properties:

- Vertices are at $(\sqrt{k}, \sqrt{k})$ and $(-\sqrt{k}, -\sqrt{k})$
- The major axis crosses the hyperbola at its vertices
- Asymptotes along the $x$ and $y$ axes
