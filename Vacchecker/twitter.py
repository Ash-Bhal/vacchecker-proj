## Twitter Sentiment

#API KEY llIbynGPl74kCZAgTLT0MBUQy
import csv
import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List
from tweepy import OAuthHandler

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Idaho"
,"Hawaii","Illinois"
,"Indiana"
,"Iowa"
,"Kansas"
,"Kentucky"
,"Louisiana"
,"Maine"
,"Maryland"

,"Massachusetts"
,"Michigan"
,"Minnesota"
,"Mississippi"
,"Missouri"
,"Montana"
,"Nebraska"
,"Nevada"
,"New Hampshire"
,"New Jersey"

,"New Mexico"
,"New York"
,"North Carolina"
,"North Dakota"
,"Ohio"
,"Oklahoma"
,"Oregon"
,'Pennsylvania'
,'Rhode Island'
,'South Carolina'

,'South Dakota'
,'Tennessee'
,"Texas"
,"Utah"
,"Vermont","Virginia,""Washington","West Virginia","Wisconsin","Wyoming"]
consumer_key = 'llIbynGPl74kCZAgTLT0MBUQy'
consumer_secret = 'JRAKYmiCo6OPyxpQzEExAczCjkJQGOWZ1b9NzMIfQcgjrkEUQl'
auth = OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode = 'extended', lang='en').items(10):
        all_tweets.append(tweet.full_text)
    return all_tweets

def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))

    return tweets_clean

def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

def generate_average_sentiment_score(keyword: str)-> int:
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    if tweets_clean == []:
        average_score = 0
    else:
        sentiment_scores = get_sentiment(tweets_clean)
        print(sentiment_scores)
        average_score = statistics.mean(sentiment_scores)
    return average_score

statecoviddict = {}
if __name__ == "__main__":

    with open('vaccine.csv', 'w', newline='') as f:
        for i in range(len(states)):
            string = states[i] + " Covid Vaccine"
            print(string)
            score = generate_average_sentiment_score(string)
            statecoviddict[states[i]] = (score)
            display = csv.writer(f)
            display.writerow([states[i],score])
            

        
print(statecoviddict)
    
## This will feed all our data and sentiment analysis ratings into a csv file.
## We will then use plotly and the geo location api's to create the map
