import sqlite3

connSQL = sqlite3.connect('tweets.db')
# conn = sqlite3.connect(':memory:')

c = connSQL.cursor()

def update_twt_sentiment(tweet_id, sentiment, table_name):
    with connSQL:
        c.execute("""UPDATE {} SET sentiment = ?
                    WHERE tweet_id=?""".format(table_name),
                  (sentiment, tweet_id))

def update_twt_place(tweet_id, newname, table_name):
    with connSQL:
        c.execute("""UPDATE {} SET place_name = ?
                    WHERE tweet_id=?""".format(table_name),
                  (newname, tweet_id))

def get_all_tweets(table_name):
    # not need to be commited so not need to use context manager
    c.execute("SELECT * FROM {}".format(table_name))
    return c.fetchall()

# print(get_all_tweets("tweets_16_18"))

alltweets = get_all_tweets("tweets_16_22_geo")

for tweet in alltweets:
    tweet_id = tweet[0]
    place_oldname = tweet[4]
    temp = place_oldname.split(", ")
    if len(temp)>1:
        update_twt_place(tweet_id,temp[1],"tweets_16_22_geo")

