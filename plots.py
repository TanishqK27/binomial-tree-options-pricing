import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt


def plot_option_price_evolution(european_prices, american_prices, N):
    """
    Plots the evolution of European and American option prices over time.

    Args:
        european_prices (list): European option prices at each time step.
        american_prices (list): American option prices at each time step.
        N (int): Number of time steps.
    """
    time_steps = range(N + 1)

    # Get the option prices at the root for both options at each step
    european_root_prices = [prices[0] for prices in european_prices]
    american_root_prices = [prices[0] for prices in american_prices]

    plt.plot(time_steps, european_root_prices, label='European Option', marker='o', color='blue')
    plt.plot(time_steps, american_root_prices, label='American Option', marker='o', color='green')

    plt.title('Option Price Evolution Over Time')
    plt.xlabel('Time Step')
    plt.ylabel('Option Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_binomial_tree(stock_tree):
    """
    Visualizes the binomial tree of stock prices with proper branching.

    Args:
        stock_tree (np.ndarray): A 2D array representing the binomial tree of stock prices.
    """
    N = stock_tree.shape[1] - 1  # Number of time steps

    # Plot the stock price nodes
    for i in range(N + 1):  # Time steps
        for j in range(i + 1):  # Nodes at each time step
            plt.scatter(i, stock_tree[j, i], color="blue")

            # Draw the connecting lines between nodes
            if i < N:  # Only draw connections to future time steps
                plt.plot([i, i + 1], [stock_tree[j, i], stock_tree[j, i + 1]], color="blue")
                plt.plot([i, i + 1], [stock_tree[j, i], stock_tree[j + 1, i + 1]], color="blue")

    plt.title("Binomial Tree for Stock Prices")
    plt.xlabel("Time Step")
    plt.ylabel("Stock Price")
    plt.grid(True)
    plt.show()


def plot_option_values(option_values, stock_tree, option_type="call"):
    """
    Visualizes the evolution of option prices over the binomial tree structure.

    Args:
        option_values (np.ndarray): Option prices at maturity.
        stock_tree (np.ndarray): Binomial tree of stock prices.
        option_type (str): Type of option (call or put).
    """
    N = stock_tree.shape[1] - 1  # Number of time steps

    # Plot option prices at each node, starting from maturity
    for i in range(N + 1):  # Time steps
        for j in range(i + 1):  # Nodes at each time step
            plt.scatter(i, option_values[j], color="green")

            # Connect nodes with lines
            if i < N:  # Only connect up and down for intermediate steps
                plt.plot([i, i + 1], [option_values[j], option_values[j]], color="green")
                plt.plot([i, i + 1], [option_values[j], option_values[j + 1]], color="green")

    plt.title(f"Evolution of {option_type.capitalize()} Option Prices")
    plt.xlabel("Time Step")
    plt.ylabel(f"{option_type.capitalize()} Option Price")
    plt.grid(True)
    plt.show()


def plot_european_vs_american(european_price, american_price):
    """
    Plots the comparison of European and American option prices.

    Args:
        european_price (float): Price of the European option.
        american_price (float): Price of the American option.
    """
    labels = ['European Option', 'American Option']
    prices = [european_price, american_price]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, prices, color=['blue', 'green'])
    plt.title('European vs American Option Prices')
    plt.ylabel('Option Price')
    plt.show()