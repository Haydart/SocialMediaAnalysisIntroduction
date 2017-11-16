import requests
from IPython.display import display, Image
import json
from pprint import pprint

# get an access token from registered Instagram App
mediaItemImage = 'https://api.instagram.com/oauth/authorize/?client_id=6a039190c7f24a39adea53685a17e401&redirect_uri=pwr.edu.pl&response_type=token&display=touch&scope=likes+relationships+public_content'
scope = 'likes+relationships+public_content'
oauth_token_url = mediaItemImage.format("6a039190c7f24a39adea53685a17e401", "pwr.edu.pl", scope)
print(oauth_token_url)  # authorize app here to get API access token

# perform HTTP request for user's last media files
response = requests.get(
    'https://api.instagram.com/v1/users/self/media/recent/?access_token=1546791944.6a03919.49f1b786e8c14afd9707758614fd8c3f')
mediafilesJson = response.json()

photosCount = 0
searchHashtags = ['wrocław', 'Wrocław', 'Wroclaw', 'wroclaw', 'Wroclove', 'wroclove', 'Wroc', 'wroc']
filteredMediaUrls = []

# filter for media with one with keyword hashtags in it
for mediaItem in mediafilesJson['data']:
    mediaItemTags = mediaItem['tags']
    print(mediaItemTags)
    for tag in mediaItemTags:
        if tag in searchHashtags:
            filteredMediaUrls.append(mediaItem['images']['standard_resolution'])
            break

# print the resulting photos
for mediaItemImage in filteredMediaUrls:
    print(mediaItemImage)
    display(Image(mediaItemImage['url']))
