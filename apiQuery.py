import http.client
import json
import sqlite3

from tweet import Tweet

# init the sql service

connSQL = sqlite3.connect('tweets.db')
# conn = sqlite3.connect(':memory:')

c = connSQL.cursor()


c.execute("""CREATE TABLE tweets_18_20 (
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

def insert_tweet(twt, table_name):
    c.execute("INSERT INTO {} VALUES (?,?,?,?,?,?,?,0)".format(table_name), (
        twt.tweet_id, twt.text, twt.author_name, twt.author_id, twt.place_name, twt.place_id, twt.time_created))



def get_tweet_by_id(twt_id, table_name):
    # not need to be commited so not need to use context manager
    c.execute("SELECT * FROM {} WHERE tweet_id=(?)".format(table_name), (twt_id,))
    return c.fetchall()


def update_twt_sentiment(tweet_id, sentiment, table_name):
    with conn:
        c.execute("""UPDATE {} SET sentiment = ?
                    WHERE tweet_id=?""".format(table_name),
                  (sentiment, tweet_id))


def remove_twt(twt, table_name):
    with conn:
        c.execute("DELETE from {} WHERE tweet_id=?".format(table_name), (twt.tweet_id,))


tweet_1 = Tweet("1548855343698120705",
                "Another week another asshole with a gun larger than a handgun mass shooting… waiting for what ever lame excuse the GOP has this time about why they don’t want better gun control"
                , 'Midget Tamer', "2196775588", 'Gahanna, OH', 'c97807ac2cd60207', '2022-07-18T02:21:04.000Z')




def findUserName(index, user_id, include_users, dicti):
    isAdded = False
    existname = dicti.get(user_id)
    if existname is None:

        isAdded = True
        # newid = include_users[index]["id"]
        newname = include_users[index]["name"]
        # print("adding to user dict: " + user_id + " " +newname)
        dicti.update({user_id: newname})
        return newname,isAdded
    return existname,isAdded


def findPlaceName(index, place_id, include_places,dicti):
    isAdded = False
    existname = dicti.get(place_id)
    # if place_id == "04cb31bae3b3af93":
    #     print("existname : "+str(existname))
    if existname is None:
        isAdded = True
        # print(str(index)+" "+place_id)
        # newid = include_places[index]["id"]
        # print("debug: "+str(index) + " "+ place_id)
        # print(len(dicti))
        # print(dicti)
        newname = include_places[index]["full_name"]

        # print("adding to place dict: " + place_id + " " + newname)
        dicti.update({place_id: newname})
        return newname,isAdded
    return existname,isAdded


def parsePageResults(jsonResponse, usersDict, placesDict):
    data = jsonResponse["data"]
    include = jsonResponse["includes"]
    meta = jsonResponse["meta"]
    usercounter = 0
    placecounter = 0
    for i in data:
        tweet_id = i["id"]
        text = i["text"]

        author_id = i["author_id"]

        place_id = i["geo"]["place_id"]
        time_created = i["created_at"]

        #the method retrieve a tuple with 2 params the first is the name and the second is the boolean if changed need to know in order to inc the counter
        tupleUserName = findUserName(usercounter, author_id, include["users"], usersDict)
        tuplePlaceName = findPlaceName(placecounter, place_id, include["places"], placesDict)
        author_name = tupleUserName[0]
        place_name =  tuplePlaceName[0]
        twt = Tweet(tweet_id, text, author_name, author_id, place_name, place_id, time_created)
        insert_tweet(twt, "tweets_18_20")
        # print("inc place counter? : "+ str(tuplePlaceName[1]))
        if tupleUserName[1] is True:
            usercounter+=1
        if tuplePlaceName[1] is True:
            placecounter+=1
        # print("end of 1 tweet################")

    connSQL.commit()


apiCallcounter = 0
tweetsCounter = 0

with open('TwitToken.txt') as f:
    lines = f.readlines()


conn = http.client.HTTPSConnection("api.twitter.com")
payload = ''
headers = {
    'Authorization': 'Bearer ' + lines[0],
    'Cookie': 'guest_id=v1%3A165557234361279783'
}
conn.request("GET", "/2/tweets/search/recent?query=(gun%20OR%20guns)%20("
                    "place_country%3AUS)&max_results=100&start_time=2022-07-18T14:00:00-04:00&end_time=2022-07-20T14"
                    ":00:00-04:00&tweet.fields=created_at&expansions=geo.place_id,"
                    "author_id&user.fields=created_at&place.fields=full_name,place_type", payload, headers)
res = conn.getresponse()
data = res.read()
x = data.decode("utf-8")
jsonResponse = json.loads(x)
# print(jsonResponse)
data = jsonResponse["data"]
print(data)
include = jsonResponse["includes"]
meta = jsonResponse["meta"]
next_token = meta["next_token"]
print(next_token)

placesDict = dict()
usersDict = dict()

# parsing and add to DB
parsePageResults(jsonResponse, usersDict, placesDict)

apiCallcounter += 1
tweetsCounter += len(data)

# if its 4 means it has next_token, no token will be 3
metaSize = len(meta)
while metaSize > 3:
    conn.request("GET",
                 f"/2/tweets/search/recent?query=(gun%20OR%20guns)%20("
                 f"place_country%3AUS)&max_results=100&start_time=2022-07-18T14:00:00-04:00&end_time=2022-07-20T14:00"
                 f":00-04:00&tweet.fields=created_at&expansions=geo.place_id,"
                 f"author_id&user.fields=created_at&place.fields=full_name,place_type&next_token={next_token}",
                 payload, headers)
    res = conn.getresponse()
    data = res.read()
    x = data.decode("utf-8")

    jsonResponse = json.loads(x)
    data = jsonResponse["data"]
    print(data)
    include = jsonResponse["includes"]
    meta = jsonResponse["meta"]
    metaSize = len(meta)
    # print(metaSize)
    apiCallcounter += 1
    tweetsCounter += len(data)
    print("apiCallNum: " + str(apiCallcounter))

    placesDict = dict()
    usersDict = dict()
    parsePageResults(jsonResponse, usersDict, placesDict)
    # connSQL.commit()
    if metaSize > 3:
        next_token = meta["next_token"]

print(tweetsCounter)
# print(usersDict)
# print(placesDict)

# dont forget to commit your changes
connSQL.commit()

# close the connection
connSQL.close()
