from binomial_tree import tree_building, calculate_payoff, backward_induction
from plots import plot_binomial_tree, plot_option_values
import numpy as np

def get_user_input():
    """
    Gathers input parameters from the user.

    Returns:
        dict: A dictionary containing all the input parameters for the option pricing model.
    """
    S = float(input("Enter the current stock price (S): "))
    K = float(input("Enter the strike price (K): "))
    T = float(input("Enter the time to maturity in years (T): "))
    r = float(input("Enter the risk-free interest rate (r, in decimal form, e.g., 0.05 for 5%): "))
    sigma = float(input("Enter the volatility of the asset (σ, in decimal form): "))
    N = int(input("Enter the number of steps in the binomial tree (N): "))
    option_type = input("Enter the option type ('call' or 'put'): ").lower()

    return {
        'S': S,
        'K': K,
        'T': T,
        'r': r,
        'sigma': sigma,
        'N': N,
        'option_type': option_type
    }


def price_option():
    """
    Prices a European option using the binomial tree model and user inputs.
    """
    # Gather user input
    params = get_user_input()

    # Extract parameters
    S = params['S']
    K = params['K']
    T = params['T']
    r = params['r']
    sigma = params['sigma']
    N = params['N']
    option_type = params['option_type']

    # Calculate time step
    dt = T / N

    # Calculate up and down factors
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor

    # Build the binomial tree of stock prices
    stock_tree = tree_building(S, u, d, N)

    # Calculate the option payoff at maturity
    payoff = calculate_payoff(stock_tree, K, option_type)

    # Perform backward induction to find the option price at t=0
    option_price = backward_induction(payoff, u, d, r, 0, N)  # Assuming no dividends (q = 0)

    # Output the final result
    print(f"The price of the {option_type} option is: {option_price:.2f}")


def price_option():
    """
    Prices a European option using the binomial tree model and visualizes the result.
    """
    # Gather user input
    params = get_user_input()

    # Extract parameters
    S = params['S']
    K = params['K']
    T = params['T']
    r = params['r']
    sigma = params['sigma']
    N = params['N']
    option_type = params['option_type']

    # Calculate time step
    dt = T / N

    # Calculate up and down factors
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor

    # Build the binomial tree of stock prices
    stock_tree = tree_building(S, u, d, N)

    # Plot the stock binomial tree
    plot_binomial_tree(stock_tree)

    # Calculate the option payoff at maturity
    payoff = calculate_payoff(stock_tree, K, option_type)

    # Perform backward induction to find the option price at t=0
    option_price = backward_induction(payoff, u, d, r, 0, N)  # Assuming no dividends (q = 0)

    # Output the final result
    print(f"The price of the {option_type} option is: {option_price:.2f}")

    # Plot the option prices evolution
    plot_option_values(payoff, stock_tree, option_type)


if __name__ == "__main__":
    price_option()