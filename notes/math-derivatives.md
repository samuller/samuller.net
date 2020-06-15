---
layout: post
title:  "Derivatives"
categories: math
header: mathematics
---

## Notation

For $y = f(x)$:

$$y' = \dot{y} = \frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}}{\mathrm{d}x}(y) = f^{\prime}(x) = \dot{f} = \frac{\mathrm{d}f}{\mathrm{d}x} = \frac{\mathrm{d}f(x)}{\mathrm{d}x} = \frac{\mathrm{d}}{\mathrm{d}x}f(x)$$

## Definition

$$f'(x) = \lim_{h \to 0}\frac{f(x+h)-f(x)}{h} = \frac{f(b) - f(a)}{b - a}$$

When the limit exists, $f$ is said to be differentiable at $a$.

## General rules

$\displaystyle \frac{d}{dx}(c\cdot f(x)) = c\cdot f'(x)$

$\displaystyle \frac{d}{dx}(f(x)\pm g(x)) = f'(x)\pm g'(x)$

$\displaystyle \frac{d}{dx}(f(x)\cdot g(x)) = f(x)\cdot g'(x)+g(x)\cdot f'(x)$

$\displaystyle \frac{d}{dx}(\frac{f(x)}{g(x)}) = \frac{g(x)\cdot f'(x)-f(x)\cdot g'(x)}{g(x)^2}$

## Chain rule

$\displaystyle \frac{d}{dx}(f(g(x))) = f'(g(x))\cdot g'(x)$ (let op dat $f(g(x)) = (f^\circ g)(x)$)

$\displaystyle \frac{d}{dx}(f^{-1}(x)) = \frac{1}{f(f^{-1}(x))}$

## Antiderivative

$\displaystyle \frac{d}{dx}(\int^x_af(x)dt) = f(x)$

$\displaystyle \frac{d}{dx}(\int^{g(x)}_af(x)dt) = f(x)\cdot \frac{d}{dx}g(x)$

## Rules

$\displaystyle \frac{d}{dx}c = 0$

$\displaystyle \frac{d}{dx}x = 1$

$\displaystyle \frac{d}{dx}c\cdot x = c$

$\displaystyle \frac{d}{dx}x^n = n\cdot x^{n-1}$

$\displaystyle \frac{d}{dx}\ln x = \frac{1}{x} \qquad \\{x > 0\\}$

$\displaystyle \frac{d}{dx}\ln \|x\| = \frac{1}{x} \qquad \\{x \neq 0\\}$

$\displaystyle \frac{d}{dx}a^x = a^x\cdot \ln a$

$\displaystyle \frac{d}{dx}\log_ax = \frac{1}{x\cdot\ln a}$

$\displaystyle \frac{d}{dx}\sin x = \cos x$

$\displaystyle \frac{d}{dx}\cos x = -\sin x$

$\displaystyle \frac{d}{dx}\tan x = \sec^2x$

$\displaystyle \frac{d}{dx}\cot x = -\mathrm{cosec}^2x$

$\displaystyle \frac{d}{dx}\sec x = \sec x\cdot\tan x$

$\displaystyle \frac{d}{dx}\mathrm{cosec} x = -\mathrm{cosec} x\cdot\cot x$

$\displaystyle \frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}$

$\displaystyle \frac{d}{dx}\arccos x = \frac{-1}{\sqrt{1-x^2}}$

$\displaystyle \frac{d}{dx}\arctan x = \frac{1}{1+x^2}$

$\displaystyle \frac{d}{dx}\mathrm{arccot} x = \frac{-1}{1+x^2}$

$\displaystyle \frac{d}{dx}\mathrm{arcsec} x = \frac{1}{\|x\|\sqrt{x^2-1}}$

$\displaystyle \frac{d}{dx}\mathrm{arccosecant} x = \frac{-1}{\|x\|\sqrt{x^2-1}}$

## Implicit differentiation

If an implicit function cannot be written in terms of a single variable, differentiate on both sides of the equation and try writing in terms of the differentiated variable.

## Second and n-th derivatives

If patterns arise, the n-th derivative can be easier to calculate, otherwise it needs to be calculated through repeated differentiation. Patterns arise with the derivatives of $e^x$ because it's derivative stays the same (itself), and also with $\sin(x)$ and $\cos(x)$ because they are each other's derivative (with just a sign change).

Notations for the second derivative are $y''$ or $f^{\prime\prime}(x)$. For the n-th derivative there are the following notations:

$$f^n(x) = \dot{y}^n = \frac{d^ny}{dx^n} = \frac{d^nf}{dx^n} = \frac{d^nf(x)}{dx^n} = \frac{d^n}{dx^n}f(x)$$

## Mean value theorem

If a function $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then there exists a $c \in [a,b]$ such that $f'(c) = \dfrac{f(b) - f(a)}{b -a}$.

I.e. if a function is continuous and differentiable on an interval, then there is somewhere in that interval where the function's derivative equals the function's average mean over the interval.

## Rolle's theorem

If a function $f$ is continuous on $[a,b]$, differentiable on $(a,b)$ and $f(a) = f(b)$, then there exists a $c \in [a,b]$ such that $f'(c) = 0$.

This is just a special case of the Mean value theorem where the endpoints have the same heights and the mean gradient is thus 0.
