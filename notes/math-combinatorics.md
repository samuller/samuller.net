---
layout: post
title:  "Combinatorics"
categories: math
header: mathematics
---

## Factorial

### Definition

$\displaystyle n! = \prod^n_{k=1}k = 1 \times 2 \times 3 \times 4 \times ...  \times (n-2) \times (n-1) \times n \qquad \\{n \in \mathbb{N}\\}$

$0! = 1$

### Rules

$n! = n(n - 1)!$

$(n + 1)! = (n-1)n!$

## Combinatorics

### Definition

$\displaystyle \binom{n}{k}$ is the number of groups of size $k$ that can be formed out of a group of size $n$.

Thus, for $0 \leq k \leq n$ where $\\{k,n \in \mathbb{N_0}\\}$ it is defined as

$$\binom{n}{k} = \frac{n!}{k!(n - k)!} = \frac{n(n - 1)(n - 2)...(n - k))}{1 \cdot 2 \cdot 3 ... n}$$

### Rules

$\displaystyle \binom{n}{0} = 1$

$\displaystyle \binom{n}{n} = 1$

$\displaystyle \binom{n}{1} = n$

$\displaystyle \binom{n}{n - 1} = n$

$\displaystyle \binom{n}{k} = \binom{n}{n - k}$

$\displaystyle \binom{n}{k} + \binom{n}{k + 1} = \binom{n + 1}{k + 1}$

## Binomial theorem

Polynomials of the form $(x + y)^n$ (a power of a binomial) can be expanded into a sum involving terms of the form $ax^by^c$ where the exponents $b$ and $c$ are nonnegative integers with $b + c = n$, and the coefficient $a$ is known as the *binomial coefficient* and equals $\binom{n}{b}$.

$$\displaystyle (x + y)^n = \sum^n_{k=0}\binom{n}{k}x^{n-k}y^k = \sum^n_{k=0}\binom{n}{k}x^{k}y^{n-k}$$

### Rules

$\displaystyle (1 + x)^n = \sum^n_{k=0}\binom{n}{k}x^r$

$\displaystyle 2^n = (1 + 1)^n = \sum^n_{k=0}\binom{n}{k}$
