import feedparser
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import numpy as np
from scipy.stats import pearsonr, spearmanr

nltk.download('vader_lexicon')

def get_rss_feed(url):
    return feedparser.parse(url)

# Apple news RSS feed (from Google News)
rss_url = "https://news.google.com/rss/search?q=Apple&hl=en-US&gl=US&ceid=US:en"

feed = get_rss_feed(rss_url)

print(f"Collected {len(feed.entries)} entries")

sia = SentimentIntensityAnalyzer()

# Extract headlines and their published dates
headlines = [entry.title for entry in feed.entries]
dates = [entry.published for entry in feed.entries if hasattr(entry, 'published')]

# Calculate sentiment for each headline
sentiments = [sia.polarity_scores(title)['compound'] for title in headlines]

# Average sentiment
avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
print(f"Average sentiment score for Apple news headlines: {avg_sentiment:.3f}")

if avg_sentiment > 0.05:
    print("Overall sentiment is positive.")
elif avg_sentiment < -0.05:
    print("Overall sentiment is negative.")
else:
    print("Overall sentiment is neutral.")

# Count sentiment categories
pos = sum(1 for s in sentiments if s > 0.05)
neg = sum(1 for s in sentiments if s < -0.05)
neu = len(sentiments) - pos - neg
print(f"Positive: {pos}, Neutral: {neu}, Negative: {neg}")

# Top positive and negative headlines
headline_scores = list(zip(headlines, sentiments))
top_pos = sorted(headline_scores, key=lambda x: x[1], reverse=True)[:5]
top_neg = sorted(headline_scores, key=lambda x: x[1])[:5]

print("\nTop Positive Headlines:")
for h, score in top_pos:
    print(f"{score:.2f}: {h}")

print("\nTop Negative Headlines:")
for h, score in top_neg:
    print(f"{score:.2f}: {h}")


date_sentiment = [(entry.published, sia.polarity_scores(entry.title)['compound']) 
                  for entry in feed.entries if hasattr(entry, 'published')]

# Create DataFrame
df = pd.DataFrame(date_sentiment, columns=['date', 'sentiment'])
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# Resample daily average sentiment
daily_sentiment = df.resample('D').mean().fillna(0)

# Plot
daily_sentiment.plot(title='Daily Average Sentiment for Apple News')
plt.ylabel('Sentiment Score')
plt.show()

# Get Apple stock data
aapl = yf.download("AAPL", period="1mo", auto_adjust=True)

# [Previous code remains the same until the stock data part]

# Get Apple stock data
aapl = yf.download("AAPL", period="1mo", auto_adjust=True)

# Create a clean DataFrame with just the closing prices
aapl_price = aapl[['Close']].copy()
aapl_price.columns = ['price']  # Rename column directly

# Make sure both DataFrames have datetime index
daily_sentiment.index = pd.to_datetime(daily_sentiment.index)
aapl_price.index = pd.to_datetime(aapl_price.index)

# Now merge using pd.merge() with explicit index merging
combined = pd.merge(
    daily_sentiment, 
    aapl_price, 
    left_index=True, 
    right_index=True, 
    how='inner'
)

fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot stock price
ax1.set_xlabel("Date")
ax1.set_ylabel("AAPL Price", color="blue")
ax1.plot(combined.index, combined["price"], color="blue", label="AAPL Price")
ax1.tick_params(axis="y", labelcolor="blue")

# Plot sentiment
ax2 = ax1.twinx()
ax2.set_ylabel("Sentiment Score", color="red")
ax2.plot(combined.index, combined["sentiment"], color="red", linestyle="--", label="News Sentiment")
ax2.tick_params(axis="y", labelcolor="red")

plt.title("Apple Stock Price vs News Sentiment")
plt.grid(True)
plt.show()

print(combined.corr())
