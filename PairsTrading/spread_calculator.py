import pandas as pd

def calculate_spread(series_a, series_b, hedge_ratio):
    """
    Calculate the spread between two stocks using the hedge ratio.
    
    S_t = A_t - β * B_t

    Parameters:
    - series_a: pd.Series (stock A prices)
    - series_b: pd.Series (stock B prices)
    - hedge_ratio: float (β)

    Returns:
    - pd.Series of spread values over time
    """
    spread = series_a - hedge_ratio * series_b
    return spread
