
import os
import time

import tweepy
from dotenv import load_dotenv

load_dotenv()

bearer_token = "AAAAAAAAAAAAAAAAAAAAAFpekAEAAAAANliUriJrNuBCotth2jby3fGiXlE%3DHMMwkgisYAjbl4pnibp6d7p9kDFSeWFohqf5F46lLv1vaOw2A9"

class MyStreamer(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.id)
        print(tweet.text)
        print("======")


def myFunc():
    streamer = MyStreamer(bearer_token)
    streamer.add_rules(tweepy.StreamRule("pakistan lang:en"))

    a = streamer.filter()

    print(a)
    file  = open("new.txt")
    file.write(a)
    file.close()
    return

myFunc()