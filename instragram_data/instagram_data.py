import requests
from IPython.display import display, Image
import json

# get an access token from registered Instagram App
url = 'https://api.instagram.com/oauth/authorize/?client_id=6a039190c7f24a39adea53685a17e401&redirect_uri=pwr.edu.pl&response_type=token&display=touch&scope=likes+relationships+public_content'
scope = 'likes+relationships+public_content'
oauth_token_url = url.format("6a039190c7f24a39adea53685a17e401", "pwr.edu.pl", scope)
print(oauth_token_url) #authorize app here to get API access token

# perform HTTP request for user's last media files
response = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token=1546791944.6a03919.49f1b786e8c14afd9707758614fd8c3f')
mediafilesJson = response.json()
json.loads(mediafilesJson)