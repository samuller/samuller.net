---
layout: post
title:  "Continuity"
categories: math
header: mathematics
---

## Definition

A function $f$ is continuous at the point $a$ if:

* $f(a)$ exists
* $lim_{x\to a}f(x)$ exists, and
* $lim_{x\to a}f(x) = f(a)$

## Continuous functions

Functions that are always continuous:

* Polynomials
* Rational functions (where the divisor $\neq 0$)
* Root functions
* Trigonometric functions

## Rules

If both functions $f$ and $g$ are continuous at $x = a$, then the following functions are also continuous at $a$:

$f \pm g$

$c\cdot f$

$f \cdot g$

$\dfrac{f}{g} \qquad \\{g(a) \neq 0\\}$

$f^\circ g$, i.e. $(f^\circ g)(x) = f(g(x))$

## Intermediate value theorem

If $f$ is continuous on the closed interval $[a,b]$ then you can take any value $k$ between $f(a)$ and $f(b)$ and there will exist at least be one value $c \in [a,b]$ such that $f(c) = k$.

_If a function is continuous on an interval for $x$, then you can take any $y$ value between the interval's endpoints and the function will have at least one $x$ value where the function at $x$ is equal to the chosen $y$ value._

## Extreme value theorem

If $f$ is continuous on the closed interval $[a,b]$ then there exists $c,d \in [a,b]$ such that $f(c)$ is an absolute maximum and $f(d)$ is an absolute minimum.

_If a function is continuous over an interval, then it has an absolute min and max in that interval._

