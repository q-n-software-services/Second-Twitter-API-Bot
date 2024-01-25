import tweepy
from textblob import TextBlob
# from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAFpekAEAAAAANliUriJrNuBCotth2jby3fGiXlE%3DHMMwkgisYAjbl4pnibp6d7p9kDFSeWFohqf5F46lLv1vaOw2A9")
print(client.search_all_tweets('pakistan'))