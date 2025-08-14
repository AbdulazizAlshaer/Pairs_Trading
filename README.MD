# 📈 Pairs Trading Strategy – Abdulaziz Alshaer

This project implements a baseline **Pairs Trading Strategy** on the Saudi Stock Market using Python. It identifies cointegrated stock pairs, generates long/short signals based on spread Z-scores, and evaluates performance through backtesting and Sharpe ratio.

---

## 📂 Project Structure

Pairs_Trading_Project/
│
├── Pairs_Trading/
│ ├── data_loader.py # Downloads historical stock data
│ ├── cointegration.py # Tests for cointegration using ADF test
│ ├── spread_calculator.py # Calculates spread using hedge ratio
│ ├── signal_generator.py # Generates signals based on Z-score thresholds
│ └── Backtest.py # Backtests strategy and computes Sharpe ratio
│
├── main.py # Main execution script
├── README.md 
└── requirements.txt # Python libraries list