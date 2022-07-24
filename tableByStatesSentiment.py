import sqlite3

connSQL = sqlite3.connect('tweets.db')
# conn = sqlite3.connect(':memory:')

c = connSQL.cursor()

def update_twt_sentiment(tweet_id, sentiment, table_name):
    with connSQL:
        c.execute("""UPDATE {} SET sentiment = ?
                    WHERE tweet_id=?""".format(table_name),
                  (sentiment, tweet_id))

# def update_state_sentimnet(state_name, sentiment, table_name):
#     with connSQL:
#         c.execute("""UPDATE {} SET place_name = ?
#                     WHERE tweet_id=?""".format(table_name),
#                   (newname, tweet_id))

def insert_state(state_name,sentiment, table_name):
    c.execute("INSERT INTO {} VALUES (?,?)".format(table_name), (
       state_name,sentiment))

def get_all_tweets(table_name):
    # not need to be commited so not need to use context manager
    c.execute("SELECT * FROM {}".format(table_name))
    return c.fetchall()

# print(get_all_tweets("tweets_16_18"))

alltweets = get_all_tweets("tweets_16_22_geo")

statesDict = dict()

for tweet in alltweets:
    sentiment = tweet[8]
    sentiment = int(sentiment)
    state = tweet[4]

    if state not in statesDict:
        statesDict[state] = sentiment
    else: statesDict[state] += sentiment

print(statesDict)

c.execute("""CREATE TABLE states_sentiment_v3 (
            state_name text,
            sentiment integer
            )""")

for state in statesDict:
    sentiment = statesDict[state]
    if sentiment <0:
        sentiment = -1
    elif sentiment >0:
        sentiment =1
    # else: sentiment = 0
    insert_state(state,sentiment,"states_sentiment_v3")

connSQL.commit()