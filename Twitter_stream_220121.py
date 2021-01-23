############################ Twitter Stream Analysis ###########################################

!pip install tweepy

# Import modules
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json
from pymongo import MongoClient
import pandas as pd
pd.__version__
from sklearn.feature_extraction.text import CountVectorizer
import sklearn
sklearn.__version__

# Key insert
consumer_key = "XXXXX" # API Key
consumer_secret = "XXXX" # API secret
access_token = "XXXX" 
access_token_secret = "XXXXX"

# Authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Database of Twitter stream
class MyListener(StreamListener):
    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        tweetind = col.insert_one(obj).inserted_id
        print (obj)
        return True

mylistener = MyListener()
mystream = Stream(auth, listener = mylistener)

# MongoDB connection
client = MongoClient('localhost', 27017)
db = client.twitterdb
col = db.tweets 
keywords = ['Big Data', 'Python', 'Data Mining', 'Data Science']

# Start
mystream.filter(track=keywords)

# Stop
mystream.disconnect()

# Verify
col.find_one()

# Twitter Srteam analysis
dataset = [{"created_at": item["created_at"], "text": item["text"],} for item in col.find()]
df = pd.DataFrame(dataset)
df
cv = CountVectorizer()
count_matrix = cv.fit_transform(df.text)
word_count = pd.DataFrame(cv.get_feature_names(), columns=["word"])
word_count["count"] = count_matrix.sum(axis=0).tolist()[0]
word_count = word_count.sort_values("count", ascending=False).reset_index(drop=True)
word_count[:50]