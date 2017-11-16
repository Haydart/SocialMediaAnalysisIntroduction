import twitter
import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud, STOPWORDS

api = twitter.Api(consumer_key='TjtC3Moxczg62gsMYNzrxGtQ3',
                  consumer_secret='rObL9LQu7pH0iU1DmvRvYiNpwzqBKtHQfWLJxBbuEfyvroAxB6',
                  access_token_key='913148816668454912-ir0ibXXXO0h2NU4PZhYIPm42ZbtNflf',
                  access_token_secret='hyTdLdsIGHaOMnPVQIaHEr3KCeThW4hlPK3BXTUkKthd6')

print(api.VerifyCredentials())
print(api.GetFriends())
print(api.GetHomeTimeline())


# def grey_color_func(word, font_size, position, orientation, random_state=None,
#                     **kwargs):
#     return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
#
#
# d = path.dirname(__file__)
#
# # read the mask image
# mask = np.array(Image.open(path.join(d, "bitcoin_mask.png")))
#
# # movie script of "a new hope"
# # http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html
# # May the lawyers deem this fair use.
# text = open(path.join(d, 'a_new_hope.txt')).read()
#
# # preprocessing the text a little bit
# text = text.replace("HAN", "Han")
# text = text.replace("LUKE'S", "Luke")
#
# # adding movie script specific stopwords
# stopwords = set(STOPWORDS)
# stopwords.add("int")
# stopwords.add("ext")
#
# wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
#                random_state=1).generate(text)
# # store default colored image
# default_colors = wc.to_array()
# plt.title("Custom colors")
# plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
#            interpolation="bilinear")
# wc.to_file("a_new_hope.png")
# plt.axis("off")
# plt.figure()
# plt.title("Default colors")
# plt.imshow(default_colors, interpolation="bilinear")
# plt.axis("off")
# plt.show()
