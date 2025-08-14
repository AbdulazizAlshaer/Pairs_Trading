import pandas as pd
import numpy as np

def backtest_pairs_strategy(df, hedge_ratio, zscore_series, signals):
    """
    Simulates trading based on pairs trading signals and calculates Sharpe Ratio.

    Parameters:
    - df: pd.DataFrame with stock A and B prices
    - hedge_ratio: float (β)
    - zscore_series: pd.Series of Z-scores
    - signals: pd.Series of 'Long', 'Short', 'Exit', or None

    Returns:
    - cumulative returns, daily returns, and Sharpe ratio
    """

    a = df.iloc[:, 0]  # Stock A
    b = df.iloc[:, 1]  # Stock B

    # Daily returns
    returns_a = a.pct_change()
    returns_b = b.pct_change()

    # Align everything
    zscore_series = zscore_series.shift(1)   # ensure no lookahead
    signals = signals.shift(1)
    returns_a = returns_a.reindex(signals.index)
    returns_b = returns_b.reindex(signals.index)

    # Track daily strategy returns
    strategy_returns = []

    for i in range(len(signals)):
        signal = signals.iloc[i]
        if signal == 'Long':
            # Long A, Short B
            daily_return = returns_a.iloc[i] - hedge_ratio * returns_b.iloc[i]
        elif signal == 'Short':
            # Short A, Long B
            daily_return = -returns_a.iloc[i] + hedge_ratio * returns_b.iloc[i]
        else:
            # No position
            daily_return = 0
        strategy_returns.append(daily_return)

    # Convert to Series
    strategy_returns = pd.Series(strategy_returns, index=signals.index).fillna(0)

    # Cumulative returns
    cumulative_returns = (1 + strategy_returns).cumprod()

    # Sharpe ratio
    mean_return = strategy_returns.mean()
    std_return = strategy_returns.std()
    sharpe_ratio = (mean_return / std_return) * np.sqrt(252) if std_return != 0 else 0

    return cumulative_returns, strategy_returns, sharpe_ratio
