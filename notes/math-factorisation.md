---
layout: post
title:  "Factorisation"
categories: math
header: mathematics
---

## Terminology

Factorisation: $ab + ac \to a(b + c)$

Expansion: $a(b + c) \to ab + ac$

Polynomial: $a_nx^n + a_{n-1}x^{n-1} + ... + a_2x^2 + a_1x + a_0$

## Formulas

$a(c + d) + b(c + d) = (a + b)(c + d)$

$a^2 \pm 2ab + b^2  = (a \pm b)^2$

$a^2 - b^2  = (a + b)(a – b)$

$a^3 \pm b^3  = (a \pm b)( a^2 \mp ab + b^2 )$

$ac + ad \pm bc \pm bd = (a \pm b)(c + d)$

## Quadratic formula

If $ax^2 + bx + c = 0$ then

$$x = \frac{-b\pm\sqrt{b^2 - 4ac}}{2a}$$

## Cardano's formula

If $x^3 + px + q = 0$ then

$$\displaystyle x = \sqrt[3]{-\frac{q}{2} + \sqrt{\frac{q^2}{4} + \frac{p^3}{27}}} + \sqrt[3]{-\frac{q}{2} - \sqrt{\frac{q^2}{4} + \frac{p^3}{27}}}$$


## Quadratic factorisation

$ax^2 + bx + c = 0 \to (px + q)(rx + s) = 0$

### By inspection

1. Find factors of $a$ and $c$
2. With possible factors as $a = pr$ and $c = qs$, attempt combinations of their factors such that $b = ps + qr$

Only works for rational roots (i.e. $p$,$q$,$r$,$s$ integers)

### Example

$$6x^2 - 7x - 20 = 0$$

With factors as

| Factors of $6$ | Factors of $20$ |
|----------------|-----------------|
| $1\times 6$    | $1\times 20$    |
| $2\times 3$    | $2\times 10$    |
|                | $4\times 5$     |

After some attempts, we can find $b = -7 = - (3\times 5) + (2\times 4)$

Which leads to a solution of

$$(3x + 4)(2x - 5)=0$$

### Completing the square

Turn quadratic equation into the algebraic identity

$$x^2 + 2hx + h^2 = (x+h)^2$$

by starting with a quadratic equation in standard form, ax^2 + bx + c = 0:

1. Divide each side by $a$, the coefficient of the squared term.
2. Subtract the constant $c/a$ from both sides.
3. Add the square of half the coefficient of $x$ to both sides (i.e. $(b/2a)^2$).
4. Write the left side as a square.
5. Square root both sides, creating two linear equations for the positive and negative roots.

This method can be used to derive the quadratic formula by applying it to the general case.

### Example

$$
\begin{align}
-3x^2 + 4x + 6 &= 0 \\
x^2 - \tfrac{4}{3}x - 2 &= 0 \tag{1} \\
x^2 - \tfrac{4}{3}x &= 2 \tag{2} \\
x^2 - 2\cdot\tfrac{2}{3}x &= 2 \\
x^2 - 2\cdot\tfrac{2}{3}x + (\tfrac{2}{3})^2 &= 2 + (\tfrac{2}{3})^2 \tag{3} \\
(x - \tfrac{2}{3})^2 &= \tfrac{22}{9} \tag{4} \\
x - \tfrac{2}{3} &= \pm\sqrt{\tfrac{22}{9}} \tag{5} \\
x &= \pm\sqrt{\tfrac{22}{9}} + \tfrac{2}{3} \\
x &= 2.23...\ \mathrm{or} -0.90... \\
\end{align}
$$
