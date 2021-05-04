---
layout: post
title:  "Partial derivatives"
categories: math
header: mathematics
---

## Chain rule

$\displaystyle \frac{\partial f(u)}{\partial x} = \frac{\partial f(u)}{\partial u} \cdot \frac{\partial u}{\partial x}$

## Matrices

Order of multiplication matters.

$\displaystyle \frac{\partial f(\mathbf{u})}{\partial \mathbf{x}} = \frac{\partial \mathbf{u}}{\partial \mathbf{x}} \cdot \frac{\partial \mathbf{f}(\mathbf{u})}{\partial \mathbf{u}}$

### Identities

Matrix $\mathbf{A}$ and vector $\mathbf{a}$ are constants.

$\displaystyle \frac{\partial \mathbf{u}(\mathbf{x}) + \mathbf{v}(\mathbf{x})}{\partial \mathbf{x}} = \frac{\partial \mathbf{u}(\mathbf{x})}{\partial \mathbf{x}} + \frac{\partial \mathbf{v}(\mathbf{x})}{\partial \mathbf{x}}$

$\displaystyle \frac{\partial \mathbf{A}\mathbf{x}}{\partial \mathbf{x}} = \mathbf{A}^T$

$\displaystyle \frac{\partial \mathbf{x}^T\mathbf{a}}{\partial \mathbf{x}} = \mathbf{a}$

$\displaystyle \frac{\partial \mathbf{x}^T\mathbf{A}\mathbf{x}}{\partial \mathbf{x}} = 2\mathbf{A}\mathbf{x}$ if $\mathbf{A}$ is symmetric

$\displaystyle \frac{\partial \|\mathbf{X}\|}{\partial \mathbf{X}} = \|\mathbf{X}\|(\mathbf{X}^{-1})^T$

$\displaystyle \frac{\partial \ln\|\mathbf{X}\|}{\partial \mathbf{X}} = (\mathbf{X}^{-1})^T$
