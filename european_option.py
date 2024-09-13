from binomial_tree import tree_building, calculate_payoff
import numpy as np

def backward_induction_with_tracking(payoff, u, d, r, N):
    """
    Performs backward induction and tracks the option prices at each time step for European options.

    Args:
        payoff (np.ndarray): Payoff at maturity.
        u (float): Up factor.
        d (float): Down factor.
        r (float): Risk-free interest rate.
        N (int): Number of time steps.

    Returns:
        list: Option prices at each time step.
    """
    dt = 1 / N
    p = (np.exp(r * dt) - d) / (u - d)

    option_prices_over_time = [payoff.copy()]

    # Work backwards through the tree
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            payoff[j] = np.exp(-r * dt) * (p * payoff[j] + (1 - p) * payoff[j + 1])
        option_prices_over_time.append(payoff[:i + 1].copy())  # Store option prices at this step

    option_prices_over_time.reverse()  # Reverse to start from t=0
    return option_prices_over_time


def price_european_option(S, K, T, r, sigma, N, option_type="call"):
    dt = T / N

    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u

    stock_tree = tree_building(S, u, d, N)
    payoff = calculate_payoff(stock_tree, K, option_type)

    # Get option prices over time
    option_prices_over_time = backward_induction_with_tracking(payoff, u, d, r, N)

    return option_prices_over_time