# 📊 Multi-Factor Regression Analysis on Stock Returns
This project performs linear regression using a multi-factor model (similar to the Fama-French approach) to examine how stock returns are explained by common market factors. It includes return computation, regression, and factor loading visualization.

🔍 Objectives
✅ Estimate factor exposures (betas) of stocks using OLS regression

✅ Visualize factor sensitivities across all stocks

✅ Evaluate the fit quality for specific stocks

✅ Understand how market factors explain variations in stock returns


⚙️ Workflow
1. Data Preprocessing
  - Reshape wide format from long-format prices.csv
  - Merge stock return data with factor data

2. Return Calculation
  - Compute daily returns as % changes

3. Regression
  - For each stock:
    Return_stock = α + β1 * FACTOR1 + β2 * FACTOR2 + β3 * FACTOR3 + ε

Store Results

Store model summary and coefficients for each stock

Visualization

Plot beta coefficients across all stocks

Plot actual vs fitted returns for a sample stock

