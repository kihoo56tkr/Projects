import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data = yf.download("ZW=F", start = "2023-01-01", end = "2025-01-01")
#data.to_csv("wheat_futures.csv")

df_wheat = pd.read_csv("wheat_futures.csv")
df_wheat = df_wheat.loc[2:]
df_wheat = df_wheat.reset_index(drop = True)
df_wheat = df_wheat.rename(columns = {'Price': 'Date'})
df_wheat['Date'] = pd.to_datetime(df_wheat['Date'])
df_wheat['Close'] = df_wheat['Close'].astype(float)

print(df_wheat.isnull().sum())

print(df_wheat.head())
print(df_wheat.dtypes)
print(df_wheat.columns)

df_sb = pd.read_csv("soybean_futures.csv")
df_sb = df_sb.loc[2:]
df_sb.reset_index(drop = True)
df_sb = df_sb.rename(columns = {'Price': 'Date'})
df_sb['Date'] = pd.to_datetime(df_sb['Date'])
df_sb['Close'] = df_sb['Close'].astype(float)

print(df_sb.head())
print(df_sb.dtypes)
print(df_sb.columns)

# Expect Return Analysis
df_wheat['Expected Return'] = (df_wheat['Close'] - df_wheat['Close'].shift(1)) / df_wheat['Close'].shift(1)
# same as above line df_wheat['PC change'] = df_wheat['Close'].pct_change()
df_sb['Expected Return'] = (df_sb['Close'] - df_sb['Close'].shift(1)) / df_sb['Close'].shift(1)

plt.plot(df_wheat['Date'], df_wheat['Expected Return'])
plt.title("A Graph of Expected Return against Date")
plt.xlabel("Date")
plt.ylabel("Expected Return")
plt.show()

plt.hist(df_wheat['Expected Return'], bins = 30, edgecolor = 'black')
plt.title("Histogram of Expected Return")
plt.show()

# Volatility
df_wheat['Volatility'] = df_wheat['Expected Return'].rolling(window = 21).std() * np.sqrt(252)
df_sb['Volatility'] = df_sb['Expected Return'].rolling(window = 21).std() * np.sqrt(252)

fig, ax = plt.subplots()
ax.plot(df_wheat['Date'], df_wheat['Close'], color = 'blue')
ax1 = ax.twinx()
ax1.plot(df_wheat['Date'], df_wheat['Volatility'], color = 'orange')
plt.title("Graph of Price and Volatility Over Time")
plt.show()

low_vol = df_wheat['Volatility'].quantile(0.2)
high_vol = df_wheat['Volatility'].quantile(0.8)

df_wheat['Signal'] = df_wheat['Volatility'].apply(lambda v: 1 if v < low_vol else (-1 if v > high_vol else 0))

low_vol = df_sb['Volatility'].quantile(0.2)
high_vol = df_sb['Volatility'].quantile(0.8)

df_sb['Signal'] = df_sb['Volatility'].apply(lambda x : 1 if x < low_vol else (-1 if x > high_vol else 0))

fig, ax = plt.subplots()
ax.plot(df_wheat['Date'], df_wheat['Close'], label="Price", color='black')

for i in range(1, len(df_wheat)):
    if df_wheat['Signal'].iloc[i] == 1:
        ax.axvspan(df_wheat['Date'].iloc[i-1], df_wheat['Date'].iloc[i], color='green', alpha = 0.1)
    elif df_wheat['Signal'].iloc[i] == -1:
        ax.axvspan(df_wheat['Date'].iloc[i-1], df_wheat['Date'].iloc[i], color = 'red', alpha = 0.1)

plt.show()

# Efficient Portfolio
mean_wheat = np.mean(df_wheat['Expected Return'])
mean_sb = np.mean(df_sb['Expected Return'])

std_wheat = np.std(df_wheat['Expected Return'])
std_sb = np.std(df_sb['Expected Return'])

print(std_wheat ** 2)
print(std_sb ** 2)

mean_vector = np.array([mean_wheat, mean_sb])

df_wheatrename = df_wheat.rename(columns = {'Close': 'Price Wheat'})
df_sbrename = df_sb.rename(columns = {'Close': 'Price SB'})

df_all = pd.merge(df_wheatrename[['Date', 'Price Wheat']], df_sbrename[['Date', 'Price SB']], on='Date', how='inner')
df_all = df_all.sort_values('Date')
returns = df_all[['Price Wheat', 'Price SB']].pct_change().dropna()
cov_matrix = returns.cov()

print(cov_matrix)
print(returns)

weights = np.linspace(0, 1, 100)
port_returns = []
port_vols = []

for w in weights:
    w_vec = np.array([w, 1-w])
    ret = np.dot(w_vec, mean_vector)
    vol = np.sqrt(np.dot(w_vec.T, np.dot(cov_matrix, w_vec)))
    port_returns.append(ret)
    port_vols.append(vol)

port_returns = np.array(port_returns)
port_vols = np.array(port_vols)
print(port_returns.shape)
print(port_vols.shape)

min_vol_index = np.argmin(port_vols) # returns index of min std
mvp_return = port_returns[min_vol_index]
mvp_vol = port_vols[min_vol_index]
mvp_weight = weights[min_vol_index]

plt.plot(port_vols, port_returns, label = "Efficient Frontier")
plt.scatter(mvp_vol, mvp_return, color='red', label='MVP')
plt.title('Efficient Frontier and Minimum Variance Portfolio')
plt.xlabel('Volatility (Standard Deviation)')
plt.ylabel('Expected Return')
plt.legend()
plt.grid(True)
plt.show()

print("MVP Weight (Wheat) ", mvp_weight)
print("MVP Weight (Soybean) ", 1 - mvp_weight)

print(returns.corr())

df_wheat.to_csv("wheat_futures_edited.csv")

