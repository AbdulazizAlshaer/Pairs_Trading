import pandas as pd

def calculate_zscore(spread_series, window=30):
    """
    Calculate the Z-score of a spread series using a rolling window.

    Parameters:
    - spread_series: pd.Series
    - window: int (number of days for rolling mean & std)

    Returns:
    - pd.Series of Z-score values
    """
    rolling_mean = spread_series.rolling(window=window).mean()
    rolling_std = spread_series.rolling(window=window).std()
    zscore = (spread_series - rolling_mean) / rolling_std
    return zscore


def generate_signals(zscore_series, entry_threshold=1.0, exit_threshold=0.5):
    """
    Generate long/short/exit signals based on Z-score thresholds.

    Parameters:
    - zscore_series: pd.Series
    - entry_threshold: float (e.g. 1.0 or 2.0)
    - exit_threshold: float (e.g. 0.5)

    Returns:
    - pd.Series of signals: 'Long', 'Short', 'Exit', or None
    """
    signals = []

    for z in zscore_series:
        if z > entry_threshold:
            signals.append("Short")  # Spread too wide → Short A, Long B
        elif z < -entry_threshold:
            signals.append("Long")   # Spread too narrow → Long A, Short B
        elif abs(z) < exit_threshold:
            signals.append("Exit")   # Spread reverted → Close positions
        else:
            signals.append(None)     # No action

    return pd.Series(signals, index=zscore_series.index)
