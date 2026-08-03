import numpy as np
import pandas as pd

def simulate_btc_prices(days=60, start_price=60000.0, mu=0.001, sigma=0.03, seed=42):
    """
    Simulates daily Bitcoin price data using Geometric Brownian Motion (GBM).

    Parameters:
    - days (int): Number of days to simulate (default 60)
    - start_price (float): The price on Day 1
    - mu (float): Daily drift rate (expected return)
    - sigma (float): Daily volatility
    - seed (int): Random seed for reproducibility

    Returns:
    - pd.DataFrame: DataFrame containing daily prices and SMAs
    """
    np.random.seed(seed)

    # Generate daily returns
    # S_t = S_{t-1} * exp((mu - 0.5 * sigma^2) + sigma * Z_t)
    shocks = np.random.normal(0, 1, days - 1)
    price_multipliers = np.exp((mu - 0.5 * sigma ** 2) + sigma * shocks)

    prices = [start_price]
    for mult in price_multipliers:
        prices.append(prices[-1] * mult)

    df = pd.DataFrame({
        'Day': range(1, days + 1),
        'Price': prices
    })

    # Calculate Moving Averages using Pandas
    df['SMA_7'] = df['Price'].rolling(window=7).mean()
    df['SMA_30'] = df['Price'].rolling(window=30).mean()

    return df

def run_trading_simulation(df, initial_cash=10000.0):
    """
    Executes the Golden Cross trading strategy on the price DataFrame.
    Golden Cross is defined here as:
    - Buy (Golden Cross): 7-day SMA crosses above 30-day SMA.
    - Sell (Death Cross): 7-day SMA crosses below 30-day SMA.

    Parameters:
    - df (pd.DataFrame): DataFrame with Price, SMA_7, and SMA_30
    - initial_cash (float): Starting portfolio cash

    Returns:
    - pd.DataFrame: DataFrame with full simulation details including trading signals and ledger
    """
    cash = initial_cash
    btc_holdings = 0.0

    actions = []
    cash_ledger = []
    btc_ledger = []
    portfolio_values = []

    # Track the previous day's relation to check for crossings
    # True if SMA_7 > SMA_30, False if SMA_7 < SMA_30, None if either is NaN
    prev_above = None

    for idx, row in df.iterrows():
        price = row['Price']
        sma7 = row['SMA_7']
        sma30 = row['SMA_30']

        action = "HOLD"

        # We need both SMAs to be available to make a crossover decision
        if not pd.isna(sma7) and not pd.isna(sma30):
            current_above = sma7 > sma30

            if prev_above is not None:
                if current_above and not prev_above:
                    # Golden Cross -> BUY (if we have cash)
                    if cash > 0:
                        btc_holdings = cash / price
                        cash = 0.0
                        action = "BUY"
                elif not current_above and prev_above:
                    # Death Cross -> SELL (if we have BTC)
                    if btc_holdings > 0:
                        cash = btc_holdings * price
                        btc_holdings = 0.0
                        action = "SELL"

            prev_above = current_above

        actions.append(action)
        cash_ledger.append(cash)
        btc_ledger.append(btc_holdings)
        portfolio_values.append(cash + btc_holdings * price)

    df_result = df.copy()
    df_result['Action'] = actions
    df_result['Cash'] = cash_ledger
    df_result['BTC_Holdings'] = btc_ledger
    df_result['Portfolio_Value'] = portfolio_values

    return df_result

def print_summary(df_result, initial_cash=10000.0):
    """
    Prints a detailed daily ledger of trades and the final portfolio performance.
    """
    print("=" * 115)
    print(f"{'DAILY LEDGER OF TRADES & PORTFOLIO STATUS':^115}")
    print("=" * 115)
    print(f"{'Day':^5} | {'BTC Price':^12} | {'7-Day SMA':^12} | {'30-Day SMA':^12} | {'Action':^8} | {'Cash Balance':^14} | {'BTC Holdings':^14} | {'Portfolio Value':^16}")
    print("-" * 115)

    for _, row in df_result.iterrows():
        day = int(row['Day'])
        price = row['Price']
        sma7 = f"{row['SMA_7']:.2f}" if not pd.isna(row['SMA_7']) else "N/A"
        sma30 = f"{row['SMA_30']:.2f}" if not pd.isna(row['SMA_30']) else "N/A"
        action = row['Action']
        cash = row['Cash']
        btc = row['BTC_Holdings']
        p_val = row['Portfolio_Value']

        # Color or highlight the Action row if it is a trade
        action_str = f"**{action}**" if action != "HOLD" else action

        print(f"{day:5d} | {price:12.2f} | {sma7:>12} | {sma30:>12} | {action_str:^8} | {cash:14.2f} | {btc:14.6f} | {p_val:16.2f}")

    print("=" * 115)
    print(f"{'FINAL PORTFOLIO PERFORMANCE SUMMARY':^115}")
    print("=" * 115)

    start_btc_price = df_result.iloc[0]['Price']
    end_btc_price = df_result.iloc[-1]['Price']
    final_portfolio_val = df_result.iloc[-1]['Portfolio_Value']

    # Calculate returns
    strat_return_pct = ((final_portfolio_val - initial_cash) / initial_cash) * 100

    # Buy & Hold strategy: Buy $10,000 worth of BTC on Day 1, hold to Day 60
    buy_and_hold_btc = initial_cash / start_btc_price
    buy_and_hold_final_val = buy_and_hold_btc * end_btc_price
    buy_and_hold_return_pct = ((buy_and_hold_final_val - initial_cash) / initial_cash) * 100

    print(f"Initial Investment:        ${initial_cash:,.2f}")
    print(f"Starting BTC Price:        ${start_btc_price:,.2f}")
    print(f"Ending BTC Price:          ${end_btc_price:,.2f}")
    print("-" * 60)
    print(f"Golden Cross Strategy:")
    print(f"  Final Portfolio Value:   ${final_portfolio_val:,.2f}")
    print(f"  Total Return (%):        {strat_return_pct:+.2f}%")
    print("-" * 60)
    print(f"Buy & Hold Strategy:")
    print(f"  Final Portfolio Value:   ${buy_and_hold_final_val:,.2f}")
    print(f"  Total Return (%):        {buy_and_hold_return_pct:+.2f}%")
    print("-" * 60)

    outperformance = final_portfolio_val - buy_and_hold_final_val
    if outperformance > 0:
        print(f"Success! Golden Cross Strategy outperformed Buy & Hold by ${outperformance:,.2f}.")
    else:
        print(f"Golden Cross Strategy underperformed Buy & Hold by ${abs(outperformance):,.2f}.")
    print("=" * 115)

if __name__ == "__main__":
    # Simulate and run with a specific seed that yields crossover signals
    # We found seed 40 has crossover signals
    df = simulate_btc_prices(days=60, seed=40)
    df_traded = run_trading_simulation(df)
    print_summary(df_traded)
