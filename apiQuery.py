import http.client
import json
import os

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
                    "place_country%3AUS)&max_results=100&start_time=2022-07-18T00:00:00-02:00&end_time=2022-07-18T05"
                    ":00:00-02:00&tweet.fields=created_at&expansions=geo.place_id,"
                    "author_id&user.fields=created_at&place.fields=full_name,place_type", payload, headers)
res = conn.getresponse()
data = res.read()
x = data.decode("utf-8")
jsonResponse = json.loads(x)
data = jsonResponse["data"]
print(data)
include = jsonResponse["includes"]
meta = jsonResponse["meta"]
next_token = meta["next_token"]
print(next_token)

apiCallcounter += 1
tweetsCounter += len(data)

# if its 4 means it has next_token, no token will be 3
metaSize = len(meta)
while metaSize > 3:
    conn.request("GET",
                 f"/2/tweets/search/recent?query=(gun%20OR%20guns)%20("
                 f"place_country%3AUS)&max_results=100&start_time=2022-07-18T00:00:00-02:00&end_time=2022-07-18T05:00"
                 f":00-02:00&tweet.fields=created_at&expansions=geo.place_id,"
                 f"author_id&user.fields=created_at&place.fields=full_name,place_type&next_token={next_token}",
                 payload, headers)
    res = conn.getresponse()
    data = res.read()
    x = data.decode("utf-8")
    print(jsonResponse["data"])
    jsonResponse = json.loads(x)
    data = jsonResponse["data"]
    include = jsonResponse["includes"]
    meta = jsonResponse["meta"]
    metaSize = len(meta)
    # print(metaSize)
    apiCallcounter += 1
    tweetsCounter += len(data)
    print("apiCallNum: " + str(apiCallcounter))
    if metaSize > 3:
        next_token = meta["next_token"]

print(tweetsCounter)
