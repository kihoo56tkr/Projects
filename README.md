# 🌾 Wheat & Soybean Futures: Portfolio Analytics & Optimization
This project explores return dynamics, volatility-based trading signals, and portfolio optimization using historical futures data for wheat and soybeans.

📌 Project Objectives
📈 Expected Return Analysis:
Calculates daily returns and visualizes them using line and histogram plots.

📊 Volatility Estimation:
Uses a 21-day rolling window to estimate annualized volatility of returns.

🚦 Signal Generation:
Generates trading signals based on quantiles of volatility (low → buy, high → sell).

🧮 Efficient Frontier & MVP:
Constructs the efficient frontier and identifies the Minimum Variance Portfolio (MVP) from a two-asset allocation.

🛠️ Tools & Technologies
Language: Python

Libraries: pandas, numpy, matplotlib, yfinance (optional for live data fetching)

🔍 Key Visualizations
- Time-series plot of expected returns
- Histogram of return distributions
- Volatility-over-time plots (with dual y-axes)
- Highlighted volatility signal zones on price charts
- Efficient frontier with MVP marked

