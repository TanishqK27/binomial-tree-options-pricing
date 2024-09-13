from european_option import price_european_option
from american_option import price_american_option
from plots import plot_option_price_evolution

def get_option_type():
    option_style = input("Enter the option style ('european' or 'american'): ").strip().lower()
    if option_style not in ['european', 'american']:
        raise ValueError("Invalid option style. Choose 'european' or 'american'.")
    return option_style

def main():
    S = float(input("Enter the current stock price (S): "))
    K = float(input("Enter the strike price (K): "))
    T = float(input("Enter the time to maturity in years (T): "))
    r = float(input("Enter the risk-free interest rate (r): "))
    sigma = float(input("Enter the volatility (σ): "))
    N = int(input("Enter the number of steps in the binomial tree (N): "))
    option_type = input("Enter the option type ('call' or 'put'): ").lower()

    option_style = get_option_type()

    # Price the options and track evolution
    european_prices_over_time = price_european_option(S, K, T, r, sigma, N, option_type)
    american_prices_over_time = price_american_option(S, K, T, r, sigma, N, option_type)

    # Plot price evolution
    plot_option_price_evolution(european_prices_over_time, american_prices_over_time, N)

if __name__ == "__main__":
    main()