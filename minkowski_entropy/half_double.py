#!/usr/bin/env python3
"""
CLI for doubling-time / half-life calculations.

Thin wrapper around minkowski_entropy.spacetime_entropy for command-line use.

Examples
--------
  python half_double.py double 100 400 10
  python half_double.py half 400 100 10
  python half_double.py pred_double 100 5 10
  python half_double.py pred_half 400 5 10
"""

from __future__ import annotations
import sys

try:
    from .spacetime_entropy import (
        LIGHT_SECOND_KM,
        calculate_t_double,
        calculate_t_half,
        predict_v2_growth,
        predict_v2_decay,
        v_at_distance,
    )
except ImportError:  # running as a script: python half_double.py
    from spacetime_entropy import (
        LIGHT_SECOND_KM,
        calculate_t_double,
        calculate_t_half,
        predict_v2_growth,
        predict_v2_decay,
        v_at_distance,
    )


def main(argv: list[str]) -> int:
    print("=== Half-Life / Doubling Time Calculator ===")
    print(f"(c = 1; 1 s ≈ {LIGHT_SECOND_KM} km)\n")
    print("Commands:")
    print("  double V1 V2 dt")
    print("  half V1 V2 dt")
    print("  pred_double V1 t_double dt")
    print("  pred_half V1 t_half dt")
    print("  v_at V0 lambda d growth|decay\n")

    if len(argv) < 5:
        print("Example usage:")
        print("  python half_double.py double 100 400 10")
        print("  python half_double.py half 400 100 10")
        print("  python half_double.py pred_double 100 5 10")
        print("  python half_double.py pred_half 400 5 10")
        print("  python half_double.py v_at 100 7 14 growth")
        return 1

    cmd = argv[1].lower()
    try:
        if cmd == "double":
            v1, v2, dt = map(float, argv[2:5])
            t = calculate_t_double(v1, v2, dt)
            print(f"Doubling time: {t:.4f} time units")
        elif cmd == "half":
            v1, v2, dt = map(float, argv[2:5])
            t = calculate_t_half(v1, v2, dt)
            print(f"Half-life: {t:.4f} time units")
        elif cmd == "pred_double":
            v1, t_dbl, dt = map(float, argv[2:5])
            v2 = predict_v2_growth(v1, t_dbl, dt)
            print(f"Predicted V2: {v2:.4f}")
        elif cmd == "pred_half":
            v1, t_half, dt = map(float, argv[2:5])
            v2 = predict_v2_decay(v1, t_half, dt)
            print(f"Predicted V2: {v2:.4f}")
        elif cmd == "v_at":
            if len(argv) < 6:
                print("Usage: v_at V0 lambda d growth|decay")
                return 1
            v0, lam, d = map(float, argv[2:5])
            mode = argv[5].lower()
            if mode not in ("growth", "decay"):
                print("mode must be 'growth' or 'decay'")
                return 1
            v = v_at_distance(v0, lam, d, mode=mode)  # type: ignore[arg-type]
            print(f"V at d={d}: {v:.4f}")
        else:
            print("Unknown command.")
            return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
