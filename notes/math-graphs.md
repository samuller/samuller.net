---
layout: post
title:  "Common function graphs"
categories: math
header: mathematics
---

These graphs are all specified as functions on the cartesian coordinate system. Since functions only have one output value for each input, these cases exclude implicit functions or more canonical forms.

<!--
Inverse

$x$ is the independent variable
$y$ is the dependent variable
-->

## Straight line

![graph of x+1](/img/math/x+1.svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$y = mx + c$$

Interpretation of constants:

- $m$: slope or gradient of the line
- $c$: $y$-intercept

Properties:

- Gradient = $\dfrac{y_1 - y_0}{x_1 - x_0} = \dfrac{\Delta y}{\Delta x} = \tan\theta = m$

## Parabola

![graph of -x^2 + 3](/img/math/-x^2 + 3.svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$
\begin{align}
y =&\ ax^2 + bx + c\\
=&\ a(x + p)^2 + q
\end{align}
$$

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

- Vertex/symmetry axis at $(p,q)$ or $\left(\dfrac{b}{2a}, -\dfrac{b^2 - 4ac}{4a}\right)$
- $\Delta = b^2 - 4ac$, called the discriminant, determines number of solutions or $x$-intercepts
  - $\Delta > 0$: 2 solutions
  - $\Delta = 0$: 1 solution
  - $\Delta < 0$: no solutions

## Hyperbola

![graph of xy=1](/img/math/xy=1.svg){: height="35%" width="35%" class="float-right hover-highlight"}

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

## Absolute value

![graph of abs(x)](/img/math/abs(x).svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$y = \left|f(x)\right|$$

Example graph shows $y = \|x\|$.

Properties:

- No negative $y$ values
- Graph has a symmetry axis at $x = 0$ such that the negative $x$ values reflect the positive $x$ values

&nbsp;

## Exponential

![graph of e^x](/img/math/e^x.svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$y = a^x$$

Interpretation of constants:

- $a$: direction of growth
  - $0 < \|a\| < 1$: grows as $x$ increases
  - $1 \geq \|a\|$: shrinks as $x$ increases

Properties:

- $y$-intercept is always at 1 since $a^0 = 1$
- Asymptote at $y = 0$

## Logarithm

![graph of ln(x)](/img/math/ln(x).svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$y = \log_ax$$

Interpretation of constants:

- $a$: direction of growth
  - $0 < \|a\| < 1$: grows as $x$ increases
  - $1 \geq \|a\|$: grows negative as $x$ increases

Properties:

- Inverse of the exponential graph
- $x$-intercept is always at 1 since $a^0 = 1$
- Asymptote at $x = 0$

## Floor

![graph of floor(x)](/img/math/floor(x).svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$
\begin{align}
y =& \lfloor x\rfloor\\
=& \max\{m \in \mathbb{Z}\ |\ m \leq x\}
\end{align}
$$

Properties:

- $\lfloor x\rfloor = m$ if and only if $m \leq x < m + 1$
- $\lfloor x\rfloor = m$ if and only if $x - 1 < m \leq x$

&nbsp;

&nbsp;

## Heaviside step

![graph of H(x)](/img/math/H(x).svg){: height="35%" width="35%" class="float-right hover-highlight"}

Equation:

$$
\begin{align}
y = H(x) =& \left\{ \begin{array}{rl}
    0, & x < 0\\
    1, & x \geq 0
   \end{array} \right.\\
=& \dfrac{x + |x|}{2x}
\end{align}
$$

&nbsp;

&nbsp;

&nbsp;

## Polynomials

Equation:

$$
\begin{align}
y =&\ a_nx^n + a_{n-1}x^{n-1} + ... + a_2x^2 + a_1x + a_0\\
=&\ a_n(x - r_1)...(x - r_n)
\end{align}
$$
{: style="clear:both"}

![graph of (x+3)(x - 2)^2(x + 1)^3](/img/math/(x+3)(x - 2)^2(x + 1)^3.svg){: height="35%" width="35%" class="float-right hover-highlight"}

Interpretation of constants:

- $n$ is the *degree* of the polynomial and determines direction of arms/branches (endpoints that approach $-\infty$ and $\infty$)
  - If $n$ is odd (1,3,5,...) both branches move in opposite directions
  - If $n$ is even (2,4,...) the branches are parabolic and move in the same direction
- $a_n$ determines the direction of branches
  - $a > 0$: branch approaching positive $\infty$ increases (average gradient positive if $n$ is odd)
  - $a < 0$: branch approaching positive $\infty$ decreases (average gradient negative if $n$ is odd)
- $r_i$ are called the factors, roots or $x$-intercept points ($1 \leq i \leq n$)

Properties:

- Behaviour near the root intercepts are determined by the number of identical factors/roots, called the factor's *multiplicity*
  - Multiplicity 1: similar to a line, the graph crosses or intersects the root intercept
  - Multiplicity 2 or even: similar to a parabola, the graph touches and "bounces" at the intercept (the $x$-axis acts as a *tangent*)
  - Multiplicity 3 or odd: similar to a cubic, the graph crosses with an S-shape near the intercept
  - Higher values of multiplicity: even or odd determines the main behaviour, but higher values increase the flatness of the curvature

For more details see this chapter on [polynomial functions](https://courses.lumenlearning.com/wmopen-collegealgebra/chapter/graphs-of-polynomial-functions/) by Lumen Learning.
