---
layout: post
title:  "Integrals"
categories: math
header: mathematics
---

## Fundamental theorem

If $f$ is continuous on $[a,b]$ and if $g(x)=\int^x_af(t)dt$ then $g$ is also continuous on $[a,b]$ and $g'(x)=f(x)$ (thus $\displaystyle\frac{d}{dx}(\int^x_af(t)dt) = f(x)$).

## Definite integral

If $f$ is continuous on $[a,b]$, then $\int^b_af(x)dx = F(b) - F(a)$ where $F$ is any antiderivative of $f$ (i.e. $F'(x)=f(x)$).

## General definite integral rules

$\displaystyle\int^b_af(x)\,dx = -\int^a_bf(x)\,dx$ 

$\displaystyle\int^c_af(x)\,dx = \int^b_af(x)\,dx + \int^c_bf(x)\,dx \qquad \\{a \leq b \leq c\\}$

<!-- Ongelykheid/vergelyking reels -->

If $f(x) \geq 0$ for all $a \leq x \leq b$ then $\displaystyle\int^b_af(x)\,dx \geq 0$

If $f(x) \geq g(x)$ for all $a \leq x \leq b$ then $\displaystyle\int^b_af(x)\,dx \geq \int^b_ag(x)d(x)$

If $m \leq f(x) \leq M$ for all $a \leq x \leq b$ then $\displaystyle m(b-a) \leq \int^b_af(x)\,dx \leq M(b-a)$

## Definite integral rules

$\displaystyle\int^b_af(x)\,dx$ only exists if $f(x)$ exists over the whole interval

$\displaystyle\int^x_af(t)\,dt = f(x)$

$\displaystyle\int^a_af(x)\,dx = 0$

If $f(x)$ is an even function, then $\displaystyle\int^a_{-a}f(x)\,dx = 0$

If $f(x)$ is an odd function, then $\displaystyle\int^a_{-a}f(x)\,dx = 2\int^a_0f(x)\,dx$

$\displaystyle\int^b_ac\,dx = c(b-a)$ (the area of the rectangle)

## General indefinite integral rules

$\displaystyle\int c\cdot f(x)\,dx = c\cdot\int f(x)\,dx$

$\displaystyle\int f(x)\pm g(x)\,dx = \int f(x)\,dx \pm \int g(x) \,dx$

$\displaystyle\int f(x)\cdot g(x)\,dx = f(u)\cdot G(x)-  \int f'(u)G(x) \,dx$ with $\displaystyle G(x) = \int g(x)\,dx$

$\displaystyle\int \frac{f'(x)}{f(x)}\,dx = \int \frac{1}{u}\,du$ with $u = f(x)$

$\displaystyle\int f(g(x))\cdot g'(x)\,dx = \int f(u)\,du$ with $u = g(x)$

## Indefinite integral rules

$\displaystyle\int c\,dx = c\cdot x + k$

$\displaystyle\int x^n\,dx = \frac{1}{n+1}x^{n+1} + k \qquad \\{n \neq -1\\}$

$\displaystyle\int \frac{1}{x}\,dx = \ln\|x\| + k$

$\displaystyle\int \ln\|x\|\,dx = \frac{1}{x} + k$

$\displaystyle\int e^x\,dx = e^x + k$

$\displaystyle\int c^x\,dx = \frac{1}{\ln c}\cdot c^x + k$

### Trigonometric functions

$\displaystyle\int \sin x\,dx = -\cos x + k$

$\displaystyle\int \cos x\,dx = \sin x + k$

$\displaystyle\int \tan x\,dx = -\ln\|\cos x\| + k = \ln\|\sec x\| + k$

$\displaystyle\int \cot x\,dx = \ln\|\sin x\| + k$

$\displaystyle\int \sec x\,dx = \ln\|\sec x+\tan x\| + k$

$\displaystyle\int \mathrm{cosec}\ x\,dx = \ln\|\mathrm{cosec}\ x-\cot x\| + k$

$\displaystyle\int \sec^2 x\,dx = \tan x + k$ if $\sec^2x$ exists over the interval

$\displaystyle\int \mathrm{cosec}^2\ x\,dx = -\cot x + k$

$\displaystyle\int \sec x\cdot\tan x\,dx = \sec x + k$

$\displaystyle\int \mathrm{cosec}\ x\cdot\cot x\,dx = -\mathrm{cosec}\ x + k$

$\displaystyle\int \frac{1}{\sqrt{1-x^2}}\,dx = \arcsin x + k = -\arccos x + k$

$\displaystyle\int \frac{1}{1+x^2}\,dx = \arctan x + k$

### Hyperbolic functions

$\displaystyle\int \sinh x\,dx = \cosh x + k$

$\displaystyle\int \cosh x\,dx = \sinh x + k$

$\displaystyle\int \mathrm{sech}^2\ x\,dx = \tanh x + k$

$\displaystyle\int \mathrm{cosech}^2\ x\,dx = -\coth x + k$

$\displaystyle\int \mathrm{sech}\ x\cdot\tanh x\,dx = -\mathrm{sech}\ x + k$

$\displaystyle\int \mathrm{cosech}\ x\cdot\coth x\,dx = -\mathrm{cosech}\ x + k$

$\displaystyle\int \frac{1}{\sqrt{1+x^2}} \,dx = \mathrm{arcsinh}\ x + k$

$\displaystyle\int \frac{1}{\sqrt{x^2-1}} \,dx = \mathrm{arccosh}\ x + k$

$\displaystyle\int \frac{1}{1-x^2} \,dx = \mathrm{arctanh}\ x + k$

### Reduction formulas

$\displaystyle\int \sin^n x\,dx = -\frac{1}{n}\cdot \cos x\cdot \sin^{n-1}x+\frac{n-1}{n}\int \sin^{n-2}x$

$\displaystyle\int \cos^n x\,dx = \frac{1}{n}\cdot \cos^{n-1} x\cdot \sin x+\frac{n-1}{n}\int \cos^{n-2}x$
