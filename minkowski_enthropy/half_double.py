#!/usr/bin/env python3
import math
import sys

def calculate_t_double(v1, v2, delta_t):
    if v2 <= v1:
        raise ValueError("For doubling time, V2 must be > V1")
    ratio = v2 / v1
    return delta_t * math.log(2) / math.log(ratio)

def calculate_t_half(v1, v2, delta_t):
    if v2 >= v1:
        raise ValueError("For half-life, V2 must be < V1")
    ratio = v1 / v2
    return delta_t * math.log(2) / math.log(ratio)

def predict_v2_from_double(v1, t_double, delta_t):
    """Inverse: predict V2 given V1, doubling time, and elapsed time"""
    return v1 * (2 ** (delta_t / t_double))

def predict_v2_from_half(v1, t_half, delta_t):
    """Inverse: predict V2 given V1, half-life, and elapsed time"""
    return v1 * (0.5 ** (delta_t / t_half))

if __name__ == "__main__":
    print("=== Half-Life / Doubling Time Calculator ===")
    print("Commands:")
    print("  double V1 V2 dt")
    print("  half V1 V2 dt")
    print("  pred_double V1 t_double dt")
    print("  pred_half V1 t_half dt\n")

    if len(sys.argv) < 5:
        print("Example usage:")
        print("  python3 half_double.py double 100 400 10")
        print("  python3 half_double.py half 400 100 10")
        print("  python3 half_double.py pred_double 100 5 10")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    try:
        if cmd == "double":
            v1, v2, dt = map(float, sys.argv[2:5])
            t = calculate_t_double(v1, v2, dt)
            print(f"Doubling time: {t:.4f} time units")
        elif cmd == "half":
            v1, v2, dt = map(float, sys.argv[2:5])
            t = calculate_t_half(v1, v2, dt)
            print(f"Half-life: {t:.4f} time units")
        elif cmd == "pred_double":
            v1, t_dbl, dt = map(float, sys.argv[2:5])
            v2 = predict_v2_from_double(v1, t_dbl, dt)
            print(f"Predicted V2: {v2:.4f}")
        elif cmd == "pred_half":
            v1, t_half, dt = map(float, sys.argv[2:5])
            v2 = predict_v2_from_half(v1, t_half, dt)
            print(f"Predicted V2: {v2:.4f}")
        else:
            print("Unknown command.")
    except Exception as e:
        print(f"Error: {e}")