---
layout: post
title:  "Cartesian graphs"
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
