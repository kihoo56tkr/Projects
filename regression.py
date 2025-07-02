import pandas as pd
import statsmodels.api as sm

price_df = pd.read_csv("prices.csv")
price_df = price_df.dropna()
price_df = price_df.reset_index(drop = True)
price_df['as_of_date'] = pd.to_datetime(price_df['as_of_date'])
price_wide = price_df.pivot(index = 'as_of_date', columns='id', values='close_')

print(price_df.describe())
print(price_df.columns)
print(price_df.isnull().sum())
print(price_df.head())
print(price_df.dtypes)
print(price_wide.head())

returns = price_wide.pct_change(fill_method = None).dropna()
returns.index = pd.to_datetime(returns.index)

factor_df = pd.read_csv("factors.csv")
factor_df['date'] = pd.to_datetime(factor_df['Unnamed: 0'], format='%Y%m%d')
factor_df = factor_df.set_index('date').drop(columns=['Unnamed: 0'])
merged = returns.join(factor_df, how='inner')

returns = merged[returns.columns]
factor_df = merged[factor_df.columns]
print(merged.head())

results = {}

for stock in returns.columns:
    Y = returns[stock] * 100
    X = factor_df[['FACTOR1', 'FACTOR2', 'FACTOR3']]
    X = sm.add_constant(X)

    model = sm.OLS(Y, X).fit()
    results[stock] = model
    
import matplotlib.pyplot as plt

betas = {
    'FACTOR1': [],
    'FACTOR2': [],
    'FACTOR3': [],
}

for model in results.values():
    for f in betas:
        betas[f].append(model.params[f])

print(results[355].summary())
print(results[33].summary())

# Plot betas
plt.figure(figsize=(10, 6))
for f in betas:
    plt.plot(list(returns.columns), betas[f], label=f)
plt.xlabel('Stock ID')
plt.ylabel('Beta Coefficient')
plt.title('Factor Loadings Across Stocks')
plt.legend()
plt.grid(True)
plt.show()

fitted = results[355].fittedvalues
actual = returns[355]

plt.plot(actual.index, actual, label='Actual')
plt.plot(fitted.index, fitted, label='Fitted')
plt.legend()
plt.title('Actual vs Fitted Returns for Stock 355')
plt.show()


