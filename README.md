# 📈 Efficient Frontier and Minimum Variance Portfolio (MVP)
This project demonstrates how to construct the efficient frontier and identify the minimum variance portfolio (MVP) using historical price data from five assets. It uses NumPy, Pandas, and SciPy for portfolio optimization, and Matplotlib for visualizations.

⚙️ Workflow Summary
1. Data Cleaning & Transformation
- Convert long format to wide format using pivot
- Handle missing data and convert date formats

2. Expected Return and Volatility
- Calculate daily log returns and annualized volatility using a 21-day rolling window

3. Covariance Matrix
- Compute the covariance matrix of asset returns for use in portfolio optimization

4. Optimization
- Define an objective to minimize portfolio volatility
- Use scipy.optimize.minimize under constraints: Weights sum to 1, No short selling (weights ≥ 0)

5. Efficient Frontier Simulation
- Simulate 10,000 random portfolios
- Compute and plot their expected return and volatility

6. Visualization
- Plot efficient frontier with: Random portfolios, Minimum variance portfolio (MVP)

📊 Output
- Optimal weights of the 5-asset MVP
- Efficient frontier scatter plot with MVP highlighted

🛠 Libraries Used
- pandas – data wrangling
- numpy – matrix computations
- matplotlib – visualization
- scipy.optimize – portfolio optimization
