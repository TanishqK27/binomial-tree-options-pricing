import numpy as np

def tree_building(S, u, d, N):
    """
    Builds a binomial tree for stock prices.

    args:
        S: current stock price.
        u: up factor.
        d: down factor.
        N: total number of time steps.

    Returns:
        np.ndarray: a 2D array representing the binomial tree of stock prices.
    """
    # Create an array to store the stock prices at each node
    tree = np.zeros((N + 1, N + 1))

    # Initialize the stock price at the root of the tree
    tree[0, 0] = S

    # Populate the binomial tree with stock prices
    for i in range(1, N + 1):
        for j in range(i + 1):
            if j == 0:
                # Up movement (u^i)
                tree[j, i] = tree[j, i - 1] * u
            else:
                # Down movement (d^(i - j))
                tree[j, i] = tree[j - 1, i - 1] * d

    return tree

def calculate_payoff(tree, K, option_type="call"):
    """
    Calculates the payoff at maturity for each node in the binomial tree.

    args:
        tree: the binomial tree of stock prices.
        K: strike price of the option.
        option_type: type of option, either "call" or "put".

    """
    N = tree.shape[1] - 1
    payoff = np.zeros(N + 1)

    # Calculate payoff at maturity based on option type
    if option_type == "call":
        payoff = np.maximum(0, tree[:, N] - K)
    elif option_type == "put":
        payoff = np.maximum(0, K - tree[:, N])

    return payoff

def backward_induction(payoff, u, d, r, q, N):
    """
    Performs backward induction to calculate the option price at the initial node.

    Args:
        payoff: payoff at maturity for each node.
        u: up factor.
        d: down factor.
        r: risk-free interest rate.
        q: dividend yield.
        N: number of time steps.

    """
    dt = 1 / N  # Time step
    p = (np.exp((r - q) * dt) - d) / (u - d)  # Risk-neutral probability

    # Work backwards through the tree
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            payoff[j] = np.exp(-r * dt) * (p * payoff[j] + (1 - p) * payoff[j + 1])

    return payoff[0]