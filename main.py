import sqlite3

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
nltk.download('vader_lexicon')
nltk.download('punkt')


def getSentiment(sentence):
    sid = SentimentIntensityAnalyzer()
    print(sentence)  # To delete
    sentiment_dictionary = sid.polarity_scores(sentence)
    # print(sentiment_dictionary['compound'])
    # decide sentiment as positive, negative and neutral
    # return sentiment_dictionary['compound']
    if sentiment_dictionary['compound'] >= 0.3:
        return 1

    elif sentiment_dictionary['compound'] <= - 0.3:
        return -1

    else:
        return 0


# sentences = ["VADER is smart, handsome, and funny.", "VADER is smart, handsome, and funny!", "Guns are bad!!!", "It's ridiculous &amp; yes, it promotes a culture of violence that has nothing to do with 2A. The overwhelming, uniquely American attraction to guns is antithetical to the American values of public safety and law and order. America has gone totally off track w/a lock &amp; load mentality. https://t.co/O1ZX3X6l2p"]
#
# for sentence in sentences:
#     print(getSentiment(sentence))

connSQL = sqlite3.connect('tweets.db')
# conn = sqlite3.connect(':memory:')

c = connSQL.cursor()

def update_twt_sentiment(tweet_id, sentiment, table_name):
    with connSQL:
        c.execute("""UPDATE {} SET sentiment = ?
                    WHERE tweet_id=?""".format(table_name),
                  (sentiment, tweet_id))

def get_all_tweets(table_name):
    # not need to be commited so not need to use context manager
    c.execute("SELECT * FROM {}".format(table_name))
    return c.fetchall()

# print(get_all_tweets("tweets_16_18"))

alltweets = get_all_tweets("tweets_16_22_geo")

for tweet in alltweets:
    tweet_id = tweet[0]
    text = tweet[1]
    sentiment = getSentiment(text)
    update_twt_sentiment(tweet_id,sentiment,"tweets_16_22_geo")


