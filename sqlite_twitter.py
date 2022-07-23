import sqlite3
from tweet import Tweet

conn = sqlite3.connect('tweets.db')
# conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE tweets (
            tweet_id text,
            text text,
            author_name text,
            author_id text,
            place_name text,
            place_id text,
            time_created text,
            sentiment integer
            )""")


# sql methods for handling db, "twt" is tweet instance

def insert_tweet(twt,table_name):
    with conn:
        c.execute("INSERT INTO {} VALUES (?,?,?,?,?,?,?,0)".format(table_name), (
            twt.tweet_id, twt.text, twt.author_id, twt.author_name, twt.place_name, twt.place_id, twt.time_created))


def get_tweet_by_id(twt_id,table_name):
    # not need to be commited so not need to use context manager
    c.execute("SELECT * FROM {} WHERE tweet_id=(?)".format(table_name), (twt_id,))
    return c.fetchall()


def update_twt_sentiment(tweet_id,sentiment,table_name):
    with conn:
        c.execute("""UPDATE {} SET sentiment = ?
                    WHERE tweet_id=?""".format(table_name),
                  (sentiment,tweet_id))

def remove_twt(twt,table_name):
    with conn:
        c.execute("DELETE from {} WHERE tweet_id=?".format(table_name),(twt.tweet_id,))


tweet_1 = Tweet("1548855343698120705",
                "Another week another asshole with a gun larger than a handgun mass shooting… waiting for what ever lame excuse the GOP has this time about why they don’t want better gun control"
                , 'Midget Tamer', "2196775588", 'Gahanna, OH', 'c97807ac2cd60207', '2022-07-18T02:21:04.000Z')

insert_tweet(tweet_1, "tweets")
update_twt_sentiment(tweet_1.tweet_id,1,"tweets")
print(get_tweet_by_id(tweet_1.tweet_id,"tweets"))
# dont forget to commit your changes
conn.commit()

# close the connection
conn.close()
