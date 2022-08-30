'''
Sentiment analysis of tweets 
version 1.0
'''
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy
import csv
#nesseracy API tokens
#API_key = "XXX"
#API_key_secret = "XXX"
#bearer_token = "XXX"


client = tweepy.Client(bearer_token)

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

#search for trump, could be anything
response = client.search_recent_tweets("Trump", max_results = 100)
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

#sentiment analyser
analyzer = SentimentIntensityAnalyzer()

# Each Tweet object has default ID and text fields
final_score = 0
for tweet in tweets:
    ps = analyzer.polarity_scores(tweet.text)
    print("{}".format(str(ps)))
    final_score += ps["compound"]

print("Final score:", final_score/len(tweets))
