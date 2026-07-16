# massenergy: Spacetime Entropy & Growth/Decay Module

**A mathematically precise framework for modeling growth, decay, and entropy production in Minkowski spacetime.**

This module generalizes exponential growth/decay processes (doubling times, half-lives) into a relativistic spacetime context. It treats time as a distance in natural units (c = 1) and provides a basis for entropy evolution from a t₀ origin point within a light-cone geometry.

The implementation is **purely mathematical** — no thermodynamic assumptions beyond the general case of a quantity V evolving exponentially along a timelike interval.

---

## Mathematical Foundation

### Symmetric Doubling Time and Half-Life

For a quantity evolving from value **V₁** to **V₂** over interval **Δt**:

**Growth (V₂ > V₁):**
$$
T_{\text{double}} = \frac{\Delta t \cdot \ln 2}{\ln (V_2 / V_1)}
$$

**Decay (V₂ < V₁):**
$$
T_{\text{half}} = \frac{\Delta t \cdot \ln 2}{\ln (V_1 / V_2)}
$$

These are symmetric: the formulas are identical in structure; only the ratio test (V₂/V₁ ≷ 1) selects which to apply.

### Inverse: Predicting Future/Past Values

Given a characteristic scale (T_double or T_half) and elapsed interval Δt:

**Growth:**
$$
V_2 = V_1 \cdot 2^{(\Delta t / T_{\text{double}})}
$$

**Decay:**
$$
V_2 = V_1 \cdot \left(\frac{1}{2}\right)^{(\Delta t / T_{\text{half}})}
$$

### Natural Units: Time as Distance

In units where **c = 1**, time and distance share dimensions. The interval **Δt** can be interpreted directly as a proper distance **d** along the timelike direction (scaled by a reference length, e.g., your chosen **s ≈ 399.8 × 10³ km**).

This converts the exponential law into a function of **spacetime separation**:

$$
V(d) = V_0 \cdot 2^{(d / \lambda)} \quad \text{or} \quad V(d) = V_0 \cdot \left(\frac{1}{2}\right)^{(d / \lambda)}
$$

where **λ** is the characteristic doubling or halving length.

### Entropy Production in the Spacetime Cone

We model a general quantity **V** (state variable) evolving from an origin **t₀** (or d = 0) outward in a Minkowski light-cone. Entropy-like growth is quantified by the logarithmic spread:

$$
S(d) \propto \ln \left( \frac{V(d)}{V_0} \right)
$$

or, more generally, any monotonic function of the interval that captures increasing "spread" or differentiation from the initial state.

This provides a basis for **active entropy evolution** along timelike paths without committing to specific thermodynamic interpretations.

### Hybrid Geometric + Exponential Behavior (Adaptable Inverse-Square)

When geometric dilution (e.g., flux through expanding 3-surfaces) is combined with the exponential evolution:

$$
F(d) \approx \frac{V(d)}{d^2} = \frac{V_0}{d^2} \cdot 2^{(d / \lambda)} \quad \text{(growth case)}
$$

or the decaying counterpart. This yields an **adaptable inverse-square law** modulated by exponential growth/decay — useful for modeling screened potentials, radiative transfer in expanding media, or information propagation in spacetime.

---

## Python Implementation

The core module (`spacetime_entropy.py`) implements the above with clean, reusable functions.

### Key Functions

```python
import math

def calculate_t_double(v1: float, v2: float, delta_t: float) -> float:
    """Doubling time for growth (V2 > V1). Returns characteristic time/distance."""
    if v2 <= v1:
        raise ValueError("V2 must be greater than V1 for doubling time")
    return delta_t * math.log(2) / math.log(v2 / v1)

def calculate_t_half(v1: float, v2: float, delta_t: float) -> float:
    """Half-life for decay (V2 < V1). Returns characteristic time/distance."""
    if v2 >= v1:
        raise ValueError("V2 must be less than V1 for half-life")
    return delta_t * math.log(2) / math.log(v1 / v2)

def predict_v2_growth(v1: float, t_double: float, delta_t: float) -> float:
    """Predict V2 given V1, doubling time, and elapsed interval (natural units ok)."""
    return v1 * (2 ** (delta_t / t_double))

def predict_v2_decay(v1: float, t_half: float, delta_t: float) -> float:
    """Predict V2 given V1, half-life, and elapsed interval."""
    return v1 * (0.5 ** (delta_t / t_half))

def entropy_production(v0: float, lambda_scale: float, d: float, mode: str = 'growth') -> float:
    """General entropy-like measure: ln(V(d)/V0)."""
    if mode == 'growth':
        v_d = v0 * (2 ** (d / lambda_scale))
    else:
        v_d = v0 * (0.5 ** (d / lambda_scale))
    return math.log(v_d / v0)

def hybrid_inverse_square(v0: float, lambda_scale: float, d: float, mode: str = 'growth') -> float:
    """V(d)/d² — adaptable inverse-square modulated by exponential evolution."""
    if d == 0:
        return v0
    if mode == 'growth':
        v_d = v0 * (2 ** (d / lambda_scale))
    else:
        v_d = v0 * (0.5 ** (d / lambda_scale))
    return v_d / (d ** 2)
```

### Example Usage

```python
# Basic doubling time
t_dbl = calculate_t_double(v1=100, v2=400, delta_t=10)
print(f"Doubling time: {t_dbl:.4f}")

# Predict future value
v_future = predict_v2_growth(v1=100, t_double=5, delta_t=10)  # → 400

# In natural units (distance d)
s_scale = 399800.0  # km reference
d = 10 * s_scale    # example distance
v_at_d = predict_v2_growth(100, 5, d / s_scale)  # scale interval

# Entropy production
s = entropy_production(v0=1.0, lambda_scale=7.0, d=14.0, mode='growth')

# Hybrid flux
flux = hybrid_inverse_square(v0=100, lambda_scale=7.0, d=14.0)
```

---

## Theoretical Context (Mathematical Only)

- **Schrödinger (1944)** observed that living systems import "negentropy" to maintain order against the general tendency toward disorder. This module treats the *general mathematical case* of a quantity V that can grow or decay exponentially from an origin.
- In Minkowski spacetime, evolution occurs along timelike intervals within the future light-cone of t₀. The module provides the exponential mapping along those intervals.
- No claim is made about thermodynamic entropy production rates; the framework is agnostic and can be specialized (e.g., by identifying V with energy density, information measure, or metabolic state).

---

## Philosophical Notes -- Gedankenexperiment

In natural units (**c = 1**), the spacetime interval \( ds \) is already a unified 4-distance. Any timelike separation from the origin \( t_0 \) is therefore a proper distance along the future light-cone.

The module separates two tightly related but distinct layers:

- **Geometry layer**: The Minkowski metric supplies the distance measure. Once \( c = 1 \), every statement about evolution “with time” is automatically a statement about evolution with 4-distance inside the light-cone.
- **Process layer**: The exponential mapping \( V(d) = V_0 \cdot 2^{d/\lambda} \) (or the decaying counterpart) and the derived functions `entropy_production(d)` and `hybrid_inverse_square(d)` describe *how* a state variable spreads or differentiates as one moves away from \( t_0 \).

Thus “spacetime” and “space-entropy” are dual descriptions of the same underlying reality:
- Spacetime provides the arena and the distance.
- Entropy production (in the general mathematical sense used here) is the process defined along that distance.

When \(Δ t \) is  re-interpreted as \( d \), the two languages become interchangeable. The framework makes no stronger ontological claim; it simply renders the mathematics consistent and natural in units where time and space share dimensions.

> **In tief Gedanken versunken**
---

## Integration into massenergy Project

1. Place `spacetime_entropy.py` in the `physics/` or `core/` directory.
2. Import as:
   ```python
   from massenergy.spacetime_entropy import (
       calculate_t_double, calculate_t_half,
       predict_v2_growth, predict_v2_decay,
       entropy_production, hybrid_inverse_square
   )
   ```
3. Extend with Minkowski metric utilities or numerical integration over light-cone surfaces as needed.

---

## References & Further Reading

- Schrödinger, E. (1944). *What is Life?*
- Standard treatments of exponential growth/decay and characteristic times.
- Minkowski spacetime geometry (any standard relativity text).


---

## Contributing / sharing

See **[CONTRIBUTING.md](../CONTRIBUTING.md)** for issues, pull requests, and testing.

Contributions and refinements welcome. Keep it mathematically rigorous.

## License

[MIT](../LICENSE) — Copyright (c) 2025-2026 Jillian England.

---

**Status**: Core mathematical engine complete. Ready for extension with visualization, differential forms, or project-specific V interpretations.

Contributions and refinements welcome. Keep it mathematically rigorous.
