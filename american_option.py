from binomial_tree import tree_building, calculate_payoff
import numpy as np

def backward_induction_american_with_tracking(payoff, u, d, r, q, N, stock_tree, K, option_type="call"):
    dt = 1 / N
    p = (np.exp((r - q) * dt) - d) / (u - d)

    option_prices_over_time = [payoff.copy()]

    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            expected_value = np.exp(-r * dt) * (p * payoff[j] + (1 - p) * payoff[j + 1])

            if option_type == "call":
                intrinsic_value = max(stock_tree[j, i] - K, 0)
            else:
                intrinsic_value = max(K - stock_tree[j, i], 0)

            payoff[j] = max(expected_value, intrinsic_value)

        option_prices_over_time.append(payoff[:i + 1].copy())  # Store option prices at this step

    option_prices_over_time.reverse()  # Reverse to start from t=0
    return option_prices_over_time

def price_american_option(S, K, T, r, sigma, N, option_type="call"):
    dt = T / N

    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u

    stock_tree = tree_building(S, u, d, N)
    payoff = calculate_payoff(stock_tree, K, option_type)

    option_prices_over_time = backward_induction_american_with_tracking(payoff, u, d, r, 0, N, stock_tree, K, option_type)

    return option_prices_over_time