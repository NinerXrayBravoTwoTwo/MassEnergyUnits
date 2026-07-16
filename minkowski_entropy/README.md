# Spacetime Entropy & Growth/Decay Module

**A mathematically precise framework for modeling growth, decay, and entropy production in Minkowski spacetime.**

This module generalizes exponential growth/decay processes (doubling times, half-lives) into a relativistic spacetime context. It treats time as a distance in natural units (**c = 1**) and provides a basis for entropy evolution from a **t₀** origin within light-cone geometry.

The implementation is **purely mathematical** — no thermodynamic assumptions beyond the general case of a quantity **V** evolving exponentially along a timelike interval.

Location in this repo: `minkowski_entropy/`

---

## Mathematical foundation

### Symmetric doubling time and half-life

For a quantity evolving from value **V₁** to **V₂** over interval **Δt**:

**Growth (V₂ > V₁):**

$$
T_{\text{double}} = \frac{\Delta t \cdot \ln 2}{\ln (V_2 / V_1)}
$$

**Decay (V₂ < V₁):**

$$
T_{\text{half}} = \frac{\Delta t \cdot \ln 2}{\ln (V_1 / V_2)}
$$

These are symmetric: the formulas share structure; only the ratio test (V₂/V₁ ≷ 1) selects which to apply.

### Inverse: predicting future/past values

Given a characteristic scale (T_double or T_half) and elapsed interval Δt:

**Growth:**

$$
V_2 = V_1 \cdot 2^{(\Delta t / T_{\text{double}})}
$$

**Decay:**

$$
V_2 = V_1 \cdot \left(\frac{1}{2}\right)^{(\Delta t / T_{\text{half}})}
$$

### Natural units: time as distance

In units where **c = 1**, time and distance share dimensions. The interval **Δt** can be read as a proper distance **d** along the timelike direction.

Reference length (same as `massenergy.units`):

$$
1\ \mathrm{s} = 299\,792.458\ \mathrm{km}
$$

(constant `LIGHT_SECOND_KM` in the Python module).

This converts the exponential law into a function of **spacetime separation**:

$$
V(d) = V_0 \cdot 2^{(d / \lambda)} \quad \text{or} \quad V(d) = V_0 \cdot \left(\frac{1}{2}\right)^{(d / \lambda)}
$$

where **λ** is the characteristic doubling or half-life length.

### Entropy production in the spacetime cone

We model a general quantity **V** evolving from an origin **t₀** (or d = 0) outward in a Minkowski light-cone. Entropy-like growth is quantified by the logarithmic spread:

$$
S(d) \propto \ln \left( \frac{V(d)}{V_0} \right)
$$

Positive for growth, negative for decay (change in log-state, not a claim of Clausius entropy).

### Hybrid geometric + exponential behavior

When geometric dilution (e.g. flux through expanding 3-surfaces) is combined with exponential evolution:

$$
F(d) \approx \frac{V(d)}{d^2} = \frac{V_0}{d^2} \cdot 2^{(d / \lambda)} \quad \text{(growth case)}
$$

or the decaying counterpart — an **adaptable inverse-square law** useful for screened potentials, radiative transfer, or information propagation sketches.

---

## Quick start

Requires Python 3.9+ (stdlib only).

From the **repository root**:

```bash
# Library self-test
python minkowski_entropy/spacetime_entropy.py

# CLI
python minkowski_entropy/half_double.py double 100 400 10
python minkowski_entropy/half_double.py half 400 100 10
python minkowski_entropy/half_double.py pred_double 100 5 10
```

### Import the package

```python
# Run from the repository root so minkowski_entropy is on sys.path
from minkowski_entropy import (
    calculate_t_double,
    calculate_t_half,
    predict_v2_growth,
    predict_v2_decay,
    entropy_production,
    hybrid_inverse_square,
    LIGHT_SECOND_KM,
)

t_dbl = calculate_t_double(v1=100, v2=400, delta_t=10)
v_future = predict_v2_growth(v1=100, t_double=5, delta_t=10)  # → 400
s = entropy_production(v0=1.0, lambda_scale=7.0, d=14.0, mode="growth")
flux = hybrid_inverse_square(v0=100, lambda_scale=7.0, d=14.0)

print(LIGHT_SECOND_KM)  # 299792.458
```

If you are already inside `minkowski_entropy/`:

```python
from spacetime_entropy import calculate_t_double, entropy_production
```

### Key functions

| Function | Role |
| -------- | ---- |
| `calculate_t_double` | Doubling time from V₁, V₂, Δt |
| `calculate_t_half` | Half-life from V₁, V₂, Δt |
| `predict_v2_growth` / `predict_v2_decay` | Inverse predictions |
| `entropy_production` | ln(V(d)/V₀) along a timelike interval |
| `hybrid_inverse_square` | V(d)/d² |
| `v_at_distance` | V(d) under growth or decay |
| `LIGHT_SECOND_KM` | 299792.458 (aligned with `massenergy.units`) |

---

## Theoretical context (mathematical only)

- **Schrödinger (1944)** observed that living systems import “negentropy” to maintain order. This module treats the *general mathematical case* of a quantity V that can grow or decay exponentially from an origin.
- In Minkowski spacetime, evolution occurs along timelike intervals within the future light-cone of t₀.
- No claim is made about thermodynamic entropy production rates; specialize by identifying V with energy density, information measure, metabolic state, etc.

---

## Philosophical notes — Gedankenexperiment

In natural units (**c = 1**), the spacetime interval \(ds\) is already a unified 4-distance. Any timelike separation from the origin \(t_0\) is a proper distance along the future light-cone.

The module separates two layers:

- **Geometry layer**: The Minkowski metric supplies the distance measure. With \(c = 1\), evolution “with time” is evolution with 4-distance inside the light-cone.
- **Process layer**: The exponential mapping \(V(d) = V_0 \cdot 2^{d/\lambda}\) (or decay) and the derived `entropy_production` / `hybrid_inverse_square` describe how a state variable spreads or differentiates away from \(t_0\).

Thus “spacetime” and “space-entropy” are dual descriptions of the same structure:

- Spacetime provides the arena and the distance.
- Entropy production (in the general mathematical sense used here) is the process defined along that distance.

When \(\Delta t\) is re-interpreted as \(d\), the two languages become interchangeable. The framework makes no stronger ontological claim; it keeps the mathematics consistent where time and space share dimensions.

> **In tief Gedanken versunken**

---

## Integration with the massenergy project

1. Keep this package under `minkowski_entropy/` at the repo root (alongside `massenergy.units`).
2. Import from the repo root as shown above.
3. Use the same natural-unit scale as the units file (`LIGHT_SECOND_KM` / `s = 2.99792458e8 m`).
4. Extend with Minkowski metric utilities or numerical integration over light-cone surfaces as needed.

Related top-level docs: [README.md](../README.md), [HYPERFACET.md](../HYPERFACET.md), [massenergy.units](../massenergy.units).

---

## References & further reading

- Schrödinger, E. (1944). *What is Life?*
- Standard treatments of exponential growth/decay and characteristic times.
- Minkowski spacetime geometry (any standard relativity text).

---

## Contributing / sharing

See **[CONTRIBUTING.md](../CONTRIBUTING.md)** for issues, pull requests, and testing.

Contributions and refinements welcome. Keep it mathematically rigorous.

## License

[MIT](../LICENSE) — Copyright (c) 1995–2026 Jillian England.

---

**Status**: Core mathematical engine complete. Ready for extension with visualization, differential forms, or project-specific V interpretations.
