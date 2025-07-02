import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("prices.csv")

# Understand the Data
print(df.columns)
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)

# Clean Data
df['as_of_date'] = pd.to_datetime(df['as_of_date'])
df['id'] = df['id'].astype(str)
df = df.dropna()
df = df.reset_index(drop = True)
df_wide = df.pivot(index = 'as_of_date', columns = 'id', values = 'close_')

# Expected Return
returns = df_wide.pct_change(fill_method = None).dropna()
#returns_n = (df_wide - df_wide.shift(1))/df_wide.shift(1)
#returns_n = returns_n.dropna()
volatility = returns.rolling(window = 21).std() * np.sqrt(252)

# Graphs of Expected Return
for stock in returns.columns:
    plt.plot(returns.index, returns[stock])
    plt.title("Graph of Expected Returns of Stock " + stock)
    plt.show()

    plt.hist(returns[stock], bins = 30, edgecolor = 'black')
    plt.title("Histogram of Expected Returns of Stock " + stock)
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(returns.index, returns[stock])
    ax1 = ax.twinx()
    ax1.plot(volatility.index, volatility[stock], color = 'orange')
    plt.title("Graph of Expected Return and Volatility of Stock " + stock)
    plt.show()

    high_vol = returns[stock].quantile(0.8)
    low_vol = returns[stock].quantile(0.2)
    returns["Signal" + stock] = returns[stock].apply(lambda row: 1 if row < low_vol else (-1 if row > high_vol else 0))

    fig, ax = plt.subplots()
    ax.plot(returns.index, returns[stock], color = 'black')

    for i in range(1, len(returns["Signal" + stock])):
        if(returns["Signal" + stock].iloc[i] == 1):
            ax.axvspan(returns.index[i - 1], returns.index[i], color = 'green', alpha = 0.3)
        if(returns["Signal" + stock].iloc[i] == -1):
            ax.axvspan(returns.index[i - 1], returns.index[i], color = 'red', alpha = 0.3)
    plt.title("Graph of Expected Return of Stock " + stock + " and Volatility against Time")
    plt.show()

# Portfolio Analysis
cov_matrix = returns.cov()
print(cov_matrix)

import seaborn as sns

# Create a pair plot
sns.pairplot(returns)
plt.show()

from scipy.optimize import minimize

# Objective function (minimize volatility)
def minimize_volatility(weights):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

n_assets = 5
weights = np.array([1/n_assets] * n_assets)  # [0.25, 0.25, 0.25, 0.25]

# Constraints: weights sum to 1, target return
constraints = (
    {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},  # Sum to 100%
)
bounds = tuple((0, 1) for _ in range(5))  # No short-selling

result = minimize(
    minimize_volatility,
    x0=weights,
    bounds=bounds,
    constraints=constraints
)
optimal_weights = result.x
print("Optimal Weights:", dict(zip(returns.columns, optimal_weights)))

import plotly.express as px

# Simulate random portfolios

expected_returns = returns.mean()

def portfolio_volatility(weights):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

def portfolio_return(weights):
    return np.dot(weights.T, expected_returns)

mvp_volatility = portfolio_volatility(optimal_weights)
mvp_return = portfolio_return(optimal_weights)

# Generate random portfolios for frontier
n_portfolios = 10000
results = np.zeros((n_portfolios, 2))  # Only need Return and Volatility now

for i in range(n_portfolios):
    weights = np.random.random(5)
    weights /= np.sum(weights) # so sum is 1
    results[i, 0] = portfolio_return(weights)  # Return
    results[i, 1] = portfolio_volatility(weights)  # Volatility

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(results[:, 1], results[:, 0], alpha=0.3, label='Random Portfolios')
plt.scatter(mvp_volatility, mvp_return, 
            color='red', marker='*', s=200, 
            label='Minimum Variance Portfolio')
plt.xlabel('Annualized Volatility')
plt.ylabel('Annualized Return')
plt.title('Efficient Frontier with MVP (5-Asset Portfolio)')
plt.legend()
plt.grid(True)
plt.show()
