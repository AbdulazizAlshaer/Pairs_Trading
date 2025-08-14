from Pairs_Trading.data_loader import get_stock_pair_data
from Pairs_Trading.cointegration import run_cointegration_test
from Pairs_Trading.spread_calculator import calculate_spread
from Pairs_Trading.Backtest import backtest_pairs_strategy

# ✅ NEW imports for Z-score and signal generation
from Pairs_Trading.signal_generator import calculate_zscore, generate_signals

# Load Al Rajhi and SNB data
df = get_stock_pair_data("7010.SR", "7020.SR", start_date="2024-08-01", end_date="2025-08-01")

# Run cointegration test
result = run_cointegration_test(df["7010.SR"], df["7020.SR"])

# Print cointegration results
print("Hedge Ratio (β):", result["hedge_ratio"])
print("ADF p-value:", result["p_value"])
print("Are the stocks cointegrated?", result["is_cointegrated"])

# Calculate the spread using the hedge ratio
spread = calculate_spread(df["7010.SR"], df["7020.SR"], result["hedge_ratio"])

# ✅ Print first few spread values
print("\nSpread series (first 5 rows):")
print(spread.head())

# ✅ NEW: Calculate Z-score of the spread (using 30-day rolling window)
zscore = calculate_zscore(spread, window=30)
print("\nZ-score (first 5 rows):")
print(zscore.head())

# ✅ NEW: Generate trading signals based on Z-score thresholds
signals = generate_signals(zscore, entry_threshold=1.0, exit_threshold=0.5)
print("\nSignals (first 10 rows):")
print(signals.head(40))

cum_returns, daily_returns, sharpe = backtest_pairs_strategy(
    df, 
    result["hedge_ratio"], 
    zscore, 
    signals
)

print(f"Sharpe Ratio: {sharpe:.2f}")
cum_returns.plot(title="Cumulative Returns of Pairs Trading Strategy")


