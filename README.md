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

4. Store Results
  - Store model summary and coefficients for each stock

5. Visualization
  - Plot beta coefficients across all stocks
  - Plot actual vs fitted returns for a sample stock

📊 Outputs
- results: Dictionary of OLS regression models per stock
- betas: Dictionary of beta coefficients for all stocks
- Graphs:Factor loadings per stock, Actual vs Fitted returns for sample stock (e.g. ID 355)

📦 Libraries Used
- pandas – Data manipulation
- statsmodels – OLS regression modeling
- matplotlib – Data visualization

