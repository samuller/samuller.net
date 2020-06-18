---
layout: post
title:  "Limits"
categories: math
header: mathematics
---

## Definition

$$\displaystyle \lim_{x \to c}f(x) = L$$

Means that $f(x)$ approaches as close as possible to $L$ by making $x$ approach as close as possible to $c$, without being equal to $c$.

## Rules

$\displaystyle \lim_{x\to a}c = c$

$\displaystyle \lim_{x\to a}x = a$

$\displaystyle \lim_{x\to a}x^n = a^n$

$\displaystyle \lim_{x\to a}x^\frac{1}{n} = a^\frac{1}{n}$

$\displaystyle \lim_{x\to 0}\frac{\sin x}{x} = 1$

$\displaystyle \lim_{x\to 0}\frac{x}{\sin x} = 1$

$\displaystyle \lim_{x\to 0}\frac{\cos x -1}{x} = 0$

$\displaystyle \lim_{x\to 0}\frac{x}{\cos x - 1} = 0$

$\displaystyle \lim_{x\to 0}\frac{\tan x}{x} = 1$

$\displaystyle \lim_{x\to 0}\frac{x}{\tan x} = 1$

$\displaystyle \lim_{x\to \infty}\frac{1}{x^r} = 0 \qquad \\{$r > 0$, r \in \mathbb{Q}\\}$

$\displaystyle \lim_{x\to -\infty}\frac{1}{x^r} = 0 \qquad \\{$r < 0$, r \in \mathbb{Q}\\}$

$\displaystyle \lim_{x\to -\infty}x^r = \infty$ (i.e. limit doesn't exist)

## General rules

Assume both $\displaystyle \lim_{x\to a}f(x)$ and $\displaystyle \lim_{x\to a}g(x)$ exist:

$\displaystyle \lim_{x\to a}f(x)\pm g(x) = \lim_{x\to a}f(x) \pm \lim_{x\to a}g(x)$

$\displaystyle \lim_{x\to a}c\cdot f(x) = c \cdot \lim_{x\to a}f(x)$

$\displaystyle \lim_{x\to a}f(x)\cdot g(x) = \lim_{x\to a}f(x) \cdot \lim_{x\to a}g(x)$

$\displaystyle \lim_{x\to a}\frac{f(x)}{g(x)} = \frac{\displaystyle \lim_{x\to a}f(x)}{\displaystyle \lim_{x\to a}g(x)} \qquad \\{\lim g(x) \neq 0\\}$

$\displaystyle \lim_{x\to a}f(x)^n = (\lim_{x\to a}f(x))^n$

$\displaystyle \lim_{x\to a}f(x)^\frac{1}{n} = (\lim_{x\to a}f(x))^\frac{1}{n}$

## Solution approaches

### Direct substitution

If a function is continuous at the point which the limit approaches, then the value can be directly substituted into the function.

_Therefore, try to rewrite a function into a function that's continuous at the point the limit is approaching._

### Use one-sided limits

$\displaystyle\lim_{x\to a}f(x)$ exists if both $\displaystyle\lim_{x\to a-}f(x) $ and $\displaystyle\lim_{x\to a+}f(x)$ exist and are equal.

_Useful to find the limit of discontinuous functions._

### Pinching theorem

Attempt to find two functions $h$ and $g$ such that $h(x) \leq f(x) \leq g(x)$ and both function's limits are equal at the point being approached by the limit being calculated. Then the limit of the two functions is equal to the limit being calculated.

_Useful for functions where limit rules don't apply, such as where a portion of the function's limit doesn't exist_.

### Rewrite limit as other known limits

For example, attempt to rewrite the limit as the definition of the derivative

$$f'(x) = \lim_{h \to 0}\frac{f(x+h)-f(x)}{h} = \frac{f(b) - f(a)}{b - a}$$

### L'Hospital's rule

If both $\displaystyle\lim_{x\to a}f(x) = 0$ and $\displaystyle\lim_{x\to a}g(x) = 0$ or both are equal to $\pm \infty$ then

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$

_Possible results that can be rewritten so that l'Hospital's rule applies, include those that at first sight might look like they approach:_

$$\frac{\infty}{\infty}, \frac{0}{0}, 0\cdot\infty, \infty\cdot-\infty, 0^0, 1^\infty, \infty^0$$
