# 📰 Apple Sentiment vs Stock Price Analysis
This project explores the relationship between news sentiment and Apple Inc.'s (AAPL) stock price using Python. It collects news headlines via Google News RSS, performs sentiment analysis using VADER, and compares aggregated daily sentiment against AAPL's closing price.

## 📈 Summary of Findings
- Data Collected: 104 headlines over ~30 days
- Average Sentiment Score: +0.074 (Positive)

Sentiment Breakdown: 31 Positive, 55 Neutral, 18 Negative

Top Headlines:

"Apple introduces a delightful and elegant new software design" (+0.78)

"Apple's AI research has failed..." (−0.51)

Correlation with Stock Price:

Pearson correlation: −0.05 → No significant short-term predictive power

🔧 Tools & Technologies
Python, feedparser, nltk (VADER), yfinance, pandas, matplotlib

Data Cleaning: Removed duplicates, normalized headlines, preserved timestamps

Sentiment Aggregation: Daily resampling of compound scores

📊 Visualizations
Daily Average Sentiment Time Series

Overlay plot of Apple stock price vs sentiment trends

Correlation matrix
