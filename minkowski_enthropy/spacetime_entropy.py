import math
import numpy as np
from scipy.integrate import odeint  # for differential forms

class MinkowskiEntropyFlow:
    def __init__(self, s_scale=399800.0):  # km reference
        self.s_scale = s_scale  # your characteristic length
        self.c = 1.0  # natural units

    def proper_time_interval(self, v1, v2, spatial_dist=0):
        """Δτ from V1 to V2, with optional spatial separation"""
        delta_v = abs(v2 - v1)
        # Timelike interval contribution
        return math.sqrt(delta_v**2 - spatial_dist**2)  # simplified

    def entropy_production(self, v0, lambda_scale, d, mode='growth'):
        """dS ~ ln(V(d)/V0) or similar"""
        v_d = v0 * (2 ** (d / lambda_scale) if mode == 'growth' else 0.5 ** (d / lambda_scale))
        return math.log(v_d / v0)  # or more sophisticated form

    def hybrid_inverse_square(self, v0, lambda_scale, d, mode='growth'):
        """Adaptable 1/d² modulated by exponential"""
        v_d = v0 * (2 ** (d / lambda_scale) if mode == 'growth' else 0.5 ** (d / lambda_scale))
        return v_d / (d ** 2) if d > 0 else v0