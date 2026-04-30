Title: Trigonometric graphs
Template: post-grid
Category: math
Header: mathematics

{#
period, asymptotes
- Function: $\mathrm{sin}(x)$
- Period: $2\pi$
class="float-right"
{: style="width: 32%"}
#}

{% macro img(url, alt, description) %}{% set img = {'url': url, 'alt': alt, 'description': description} %}{% include "partials/image.html" %}{% endmacro %}

{{ img("/img/math/sin(x).svg", "graph of sin(x).svg", "Sine: $\\mathrm{sin}(x)$") }}
{{ img("/img/math/cos(x).svg", "graph of cos(x).svg", "Cosine: $\\mathrm{cos}(x)$") }}
{{ img("/img/math/tan(x).svg", "graph of tan(x).svg", "Tangent: $\\mathrm{tan}(x)$") }}
{{ img("/img/math/sec(x).svg", "graph of sec(x).svg", "Secant: $\\mathrm{sec}(x)$") }}
{{ img("/img/math/cosec(x).svg", "graph of cosec(x).svg", "Cosecant: $\\mathrm{cosec}(x)$") }}
{{ img("/img/math/cot(x).svg", "graph of cot(x).svg", "Cotangent: $\\mathrm{cot}(x)$") }}

## Hyperbolic functions
{: style="grid-column: 1 / 4;"}

{{ img("/img/math/sinh(x).svg", "graph of sinh(x).svg", "Hyperbolic sine: $\\mathrm{sinh}(x)$") }}
{{ img("/img/math/cosh(x).svg", "graph of cosh(x).svg", "Hyperbolic cosine: $\\mathrm{cosh}(x)$") }}
{{ img("/img/math/tanh(x).svg", "graph of tanh(x).svg", "Hyperbolic tangent: $\\mathrm{tanh}(x)$") }}
{{ img("/img/math/arcsinh(x).svg", "graph of arcsinh(x).svg", "Inverse hyperbolic sine: $\\mathrm{arcsinh}(x)$") }}
{{ img("/img/math/arccosh(x).svg", "graph of arccosh(x).svg", "Inverse hyperbolic cosine: $\\mathrm{arccosh}(x)$") }}
{{ img("/img/math/arctanh(x).svg", "graph of arctanh(x).svg", "Inverse hyperbolic tangent: $\\mathrm{arctanh}(x)$") }}
