#!/usr/bin/env python3
"""
finance-examples.py
===================

Practical examples of using the spacetime_entropy module
for compound interest, investments, loans, and inflation.

All examples treat money as an exponentially evolving state variable
along a timelike interval (exactly the same mathematics as entropy production).

Requires: spacetime_entropy.py in the same directory or on PYTHONPATH.
"""

import math
from spacetime_entropy import (
    calculate_t_double,
    predict_v2_growth,
    predict_v2_decay,
    entropy_production,
)


# ============================================================
# Core Helpers
# ============================================================

def future_value_compound(principal: float, annual_rate: float, years: float,
                          compounds_per_year: int = 12) -> float:
    """
    Future value with discrete compounding (standard bank formula).
    """
    if annual_rate < 0:
        raise ValueError("annual_rate must be non-negative")
    periods = years * compounds_per_year
    rate_per_period = annual_rate / compounds_per_year
    return principal * (1 + rate_per_period) ** periods


def future_value_continuous(principal: float, annual_rate: float, years: float) -> float:
    """
    Future value with continuous compounding (e^rt).
    Maps directly to the exponential growth in spacetime_entropy.
    """
    if annual_rate < 0:
        raise ValueError("annual_rate must be non-negative")
    return principal * math.exp(annual_rate * years)


def doubling_time_from_rate(annual_rate: float) -> float:
    """
    Time required for money to double at the given continuous rate.
    Maps directly to the module's characteristic doubling time.
    """
    if annual_rate <= 0:
        raise ValueError("annual_rate must be positive")
    # For continuous compounding, doubling time is ln(2) / rate
    return math.log(2) / annual_rate


def inflation_adjusted_value(nominal_value: float, inflation_rate: float, years: float) -> float:
    """
    Real purchasing power after inflation (decay of value).
    Uses the decay predictor.
    """
    if inflation_rate < 0:
        raise ValueError("inflation_rate must be non-negative")
    # Treat inflation as decay of purchasing power
    # Half-life of purchasing power at given inflation rate
    t_half = math.log(2) / inflation_rate
    return predict_v2_decay(v1=nominal_value, t_half=t_half, delta_t=years)


# ============================================================
# Example Scenarios
# ============================================================

def run_examples():
    print("=== Finance Examples using spacetime_entropy ===\n")

    # 1. Standard compound interest
    principal = 10_000.0
    rate = 0.05          # 5% annual
    years = 10

    fv_discrete = future_value_compound(principal, rate, years, compounds_per_year=12)
    fv_continuous = future_value_continuous(principal, rate, years)

    print("1. Compound Interest on $10,000 at 5% for 10 years")
    print(f"   Monthly compounding:  ${fv_discrete:,.2f}")
    print(f"   Continuous compounding: ${fv_continuous:,.2f}")
    print()

    # 2. Doubling time (Rule of 72 approximation)
    t_dbl = doubling_time_from_rate(rate)
    print("2. Time to Double at 5% annual rate")
    print(f"   Calculated doubling time: {t_dbl:.2f} years")
    print(f"   Rule-of-72 estimate:      {72 / (rate * 100):.2f} years")
    print()

    # 3. Predict future value using module's growth function
    t_double = calculate_t_double(v1=principal, v2=principal * 2, delta_t=t_dbl)
    future_from_module = predict_v2_growth(v1=principal, t_double=t_double, delta_t=years)
    print("3. Future value via spacetime_entropy growth predictor")
    print(f"   Predicted value: ${future_from_module:,.2f}")
    print()

    # 4. Inflation adjustment (purchasing power decay)
    inflation = 0.03     # 3% annual inflation
    real_value = inflation_adjusted_value(fv_discrete, inflation, years)
    print("4. Inflation-adjusted purchasing power after 10 years")
    print(f"   Nominal future value:     ${fv_discrete:,.2f}")
    print(f"   Real purchasing power:    ${real_value:,.2f}")
    print()

    # 5. Loan / decay example (paying down principal)
    loan_amount = 200_000.0
    annual_payment_rate = 0.04   # effective rate at which principal is reduced
    payoff_years = 15
    t_half_loan = math.log(2) / annual_payment_rate
    remaining = predict_v2_decay(v1=loan_amount, t_half=t_half_loan, delta_t=payoff_years)
    print("5. Loan payoff example (simplified decay)")
    print(f"   Original loan: ${loan_amount:,.0f}")
    print(f"   Remaining after {payoff_years} years at effective 4% reduction rate: ${remaining:,.2f}")
    print()

    # 6. Entropy-style "interest entropy"
    interest_entropy = entropy_production(v0=principal, lambda_scale=t_double, d=years, mode="growth")
    print("6. Entropy production analogy (log growth of wealth)")
    print(f"   ln(Future / Principal) over {years} years: {interest_entropy:.4f}")
    print()

    print("All examples completed successfully.")
    print("The same exponential mathematics governs bank balances, biological aging, and spacetime entropy.")


if __name__ == "__main__":
    run_examples()
