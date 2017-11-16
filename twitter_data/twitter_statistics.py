import twitter
import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
import json

from wordcloud import WordCloud, STOPWORDS

api = twitter.Api(consumer_key='TjtC3Moxczg62gsMYNzrxGtQ3',
                  consumer_secret='rObL9LQu7pH0iU1DmvRvYiNpwzqBKtHQfWLJxBbuEfyvroAxB6',
                  access_token_key='913148816668454912-ir0ibXXXO0h2NU4PZhYIPm42ZbtNflf',
                  access_token_secret='hyTdLdsIGHaOMnPVQIaHEr3KCeThW4hlPK3BXTUkKthd6')

print(api.VerifyCredentials())
print(api.GetFriends())
print(api.GetHomeTimeline())

timelineTweets = api.GetHomeTimeline()
print(type(timelineTweets[0]))

text = ""

for tweetStatus in timelineTweets:
    j = json.loads(tweetStatus.AsJsonString())
    text += j['text']


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


directory = path.dirname(__file__)

# read the mask image
mask = np.array(Image.open(path.join(directory, "bitcoin_mask.png")))

# # adding specific stopwords
stopwords = set(STOPWORDS)
stopwords.add("https")

wordCloud = WordCloud(max_words=1000, mask=mask, margin=10, stopwords=stopwords, random_state=1).generate(text)
default_colors = wordCloud.to_array()
plt.title("Custom colors")
plt.imshow(wordCloud.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
wordCloud.to_file("cryptocurrencies.png")
plt.axis("off")
plt.figure()
plt.title("Default colors")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.show()
