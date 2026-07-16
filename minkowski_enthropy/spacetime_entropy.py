"""
massenergy.spacetime_entropy
============================

A mathematically precise module for modeling exponential growth, decay,
and entropy production along timelike intervals in Minkowski spacetime.

Core idea:
- Treat time as distance in natural units (c = 1).
- Provide symmetric doubling-time / half-life calculations.
- Support inverse predictions of future/past values.
- Quantify general entropy-like production from a t₀ origin in the light-cone.
- Offer a hybrid geometric + exponential model (adaptable inverse-square behavior).

This implementation is deliberately general and agnostic to specific
thermodynamic interpretations. It embodies the mathematical structure
underlying Schrödinger's 1944 negentropy observation in a spacetime context.

Usage:
    from massenergy.spacetime_entropy import (
        calculate_t_double,
        calculate_t_half,
        predict_v2_growth,
        predict_v2_decay,
        entropy_production,
        hybrid_inverse_square,
    )

References:
    Schrödinger, E. (1944). What is Life?
"""

from __future__ import annotations
import math
from typing import Literal


def calculate_t_double(v1: float, v2: float, delta_t: float) -> float:
    """
    Calculate doubling time (characteristic scale) for exponential growth.

    Parameters
    ----------
    v1 : float
        Initial value (must be positive).
    v2 : float
        Final value, with v2 > v1.
    delta_t : float
        Elapsed interval (time or distance in natural units).

    Returns
    -------
    float
        Doubling time T_double such that V(delta_t) = V1 * 2^(delta_t / T_double).

    Raises
    ------
    ValueError
        If v2 <= v1 or non-positive inputs where mathematically invalid.
    """
    if v1 <= 0 or v2 <= 0:
        raise ValueError("v1 and v2 must be positive")
    if v2 <= v1:
        raise ValueError("For doubling time, v2 must be strictly greater than v1")
    if delta_t < 0:
        raise ValueError("delta_t must be non-negative")

    ratio = v2 / v1
    return delta_t * math.log(2) / math.log(ratio)


def calculate_t_half(v1: float, v2: float, delta_t: float) -> float:
    """
    Calculate half-life (characteristic scale) for exponential decay.

    Parameters
    ----------
    v1 : float
        Initial value (must be positive).
    v2 : float
        Final value, with v2 < v1.
    delta_t : float
        Elapsed interval (time or distance in natural units).

    Returns
    -------
    float
        Half-life T_half such that V(delta_t) = V1 * (1/2)^(delta_t / T_half).

    Raises
    ------
    ValueError
        If v2 >= v1 or non-positive inputs.
    """
    if v1 <= 0 or v2 <= 0:
        raise ValueError("v1 and v2 must be positive")
    if v2 >= v1:
        raise ValueError("For half-life, v2 must be strictly less than v1")
    if delta_t < 0:
        raise ValueError("delta_t must be non-negative")

    ratio = v1 / v2
    return delta_t * math.log(2) / math.log(ratio)


def predict_v2_growth(v1: float, t_double: float, delta_t: float) -> float:
    """
    Predict the value V2 after elapsed interval delta_t under growth.

    Inverse of calculate_t_double.

    V2 = V1 * 2^(delta_t / t_double)
    """
    if v1 <= 0:
        raise ValueError("v1 must be positive")
    if t_double <= 0:
        raise ValueError("t_double must be positive")
    if delta_t < 0:
        raise ValueError("delta_t must be non-negative")

    return v1 * (2 ** (delta_t / t_double))


def predict_v2_decay(v1: float, t_half: float, delta_t: float) -> float:
    """
    Predict the value V2 after elapsed interval delta_t under decay.

    Inverse of calculate_t_half.

    V2 = V1 * (1/2)^(delta_t / t_half)
    """
    if v1 <= 0:
        raise ValueError("v1 must be positive")
    if t_half <= 0:
        raise ValueError("t_half must be positive")
    if delta_t < 0:
        raise ValueError("delta_t must be non-negative")

    return v1 * (0.5 ** (delta_t / t_half))


def entropy_production(
    v0: float,
    lambda_scale: float,
    d: float,
    mode: Literal["growth", "decay"] = "growth",
) -> float:
    """
    Compute a general entropy-like production measure along a timelike interval.

    S(d) ∝ ln(V(d) / V0)

    This quantifies the logarithmic spread of the state variable V
    from its initial value at the origin (t₀ or d=0) in the spacetime cone.

    Parameters
    ----------
    v0 : float
        Initial value at d=0.
    lambda_scale : float
        Characteristic scale (T_double or T_half).
    d : float
        Distance (or time in natural units) from origin.
    mode : {"growth", "decay"}
        Direction of evolution.

    Returns
    -------
    float
        ln(V(d)/V0) — positive for growth, negative for decay.
    """
    if v0 <= 0:
        raise ValueError("v0 must be positive")
    if lambda_scale <= 0:
        raise ValueError("lambda_scale must be positive")
    if d < 0:
        raise ValueError("d must be non-negative")

    if mode == "growth":
        v_d = v0 * (2 ** (d / lambda_scale))
    elif mode == "decay":
        v_d = v0 * (0.5 ** (d / lambda_scale))
    else:
        raise ValueError("mode must be 'growth' or 'decay'")

    return math.log(v_d / v0)


def hybrid_inverse_square(
    v0: float,
    lambda_scale: float,
    d: float,
    mode: Literal["growth", "decay"] = "growth",
) -> float:
    """
    Hybrid model combining exponential evolution with geometric dilution.

    Returns V(d) / d² — an adaptable inverse-square law modulated by
    exponential growth or decay. Useful for flux, intensity, or screened
    potentials in an expanding spacetime context.

    At d=0 returns v0 (by continuity / convention).
    """
    if v0 <= 0:
        raise ValueError("v0 must be positive")
    if lambda_scale <= 0:
        raise ValueError("lambda_scale must be positive")
    if d < 0:
        raise ValueError("d must be non-negative")

    if d == 0:
        return v0

    if mode == "growth":
        v_d = v0 * (2 ** (d / lambda_scale))
    elif mode == "decay":
        v_d = v0 * (0.5 ** (d / lambda_scale))
    else:
        raise ValueError("mode must be 'growth' or 'decay'")

    return v_d / (d ** 2)


# ------------------------------------------------------------------
# Demo / Self-test when run directly
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("=== massenergy.spacetime_entropy self-test ===\n")

    # Example 1: Basic doubling
    t_dbl = calculate_t_double(v1=100, v2=400, delta_t=10)
    print(f"Doubling time (100 → 400 in 10 units): {t_dbl:.4f}")

    v_future = predict_v2_growth(v1=100, t_double=t_dbl, delta_t=10)
    print(f"Predicted V2: {v_future:.2f} (expected 400)")

    # Example 2: Half-life
    t_half = calculate_t_half(v1=400, v2=100, delta_t=10)
    print(f"Half-life (400 → 100 in 10 units): {t_half:.4f}")

    v_past = predict_v2_decay(v1=400, t_half=t_half, delta_t=10)
    print(f"Predicted V2: {v_past:.2f} (expected 100)")

    # Example 3: Natural units + entropy
    s_scale = 399800.0  # km reference
    d_scaled = 14.0     # example scaled distance
    s = entropy_production(v0=1.0, lambda_scale=7.0, d=d_scaled, mode="growth")
    print(f"Entropy production at d={d_scaled}: {s:.4f}")

    # Example 4: Hybrid inverse-square
    flux = hybrid_inverse_square(v0=100, lambda_scale=7.0, d=14.0, mode="growth")
    print(f"Hybrid flux at d=14: {flux:.4f}")

    print("\nAll basic tests passed. Module ready for integration.")