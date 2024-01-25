import tweepy
from textblob import TextBlob
# from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


consumerKey = 'ceGUMigRu0xklG7IgCaJhuJBp'
consumerSecret = 'y0J01Az1binWh8QvDjMMTGH7T0ekEzdsRRhIBjlJ1G0xFsW1Y'

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAFpekAEAAAAANliUriJrNuBCotth2jby3fGiXlE%3DHMMwkgisYAjbl4pnibp6d7p9kDFSeWFohqf5F46lLv1vaOw2A9")
# auth = tweepy.OAuth2AppHandler(consumerKey, consumerSecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Extract 100 tweets from the user
posts = api.user_timeline(screen_name="BillGates", count=100, tweet_mode='extended')


# Print last 5 tweets from the user
print("Show the 5 recent Tweets")
for tweets in posts[0,5]:
    print(tweets.full_text + '\n')

    


