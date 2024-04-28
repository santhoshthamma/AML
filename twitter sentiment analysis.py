import tweepy
from textblob import TextBlob

# Authenticate with your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets related to a specific topic
search_query = 'Python'
tweets = api.search(q=search_query, count=100)

positive_count = 0
negative_count = 0
neutral_count = 0

# Analyze sentiment for each tweet
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    
    # Classify sentiment as positive, negative, or neutral
    if analysis.sentiment.polarity > 0:
        positive_count += 1
    elif analysis.sentiment.polarity < 0:
        negative_count += 1
    else:
        neutral_count += 1

# Calculate percentages
total_tweets = len(tweets)
positive_percentage = (positive_count / total_tweets) * 100
negative_percentage = (negative_count / total_tweets) * 100
neutral_percentage = (neutral_count / total_tweets) * 100

# Print sentiment analysis results
print(f"Sentiment Analysis Results for '{search_query}'")
print(f"Total tweets analyzed: {total_tweets}")
print(f"Positive tweets: {positive_percentage:.2f}%")
print(f"Negative tweets: {negative_percentage:.2f}%")
print(f"Neutral tweets: {neutral_percentage:.2f}%")
