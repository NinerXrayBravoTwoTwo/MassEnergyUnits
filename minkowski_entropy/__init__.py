"""
Growth, decay, and entropy-like measures along timelike intervals (c = 1).

Import from the package root (repository root on PYTHONPATH / cwd)::

    from minkowski_entropy import (
        LIGHT_SECOND_KM,
        calculate_t_double,
        calculate_t_half,
        predict_v2_growth,
        predict_v2_decay,
        entropy_production,
        hybrid_inverse_square,
        v_at_distance,
    )
"""

from .spacetime_entropy import (
    LIGHT_SECOND_KM,
    calculate_t_double,
    calculate_t_half,
    predict_v2_growth,
    predict_v2_decay,
    entropy_production,
    hybrid_inverse_square,
    v_at_distance,
)

__all__ = [
    "LIGHT_SECOND_KM",
    "calculate_t_double",
    "calculate_t_half",
    "predict_v2_growth",
    "predict_v2_decay",
    "entropy_production",
    "hybrid_inverse_square",
    "v_at_distance",
]
