import twitter

api = twitter.Api(consumer_key='TjtC3Moxczg62gsMYNzrxGtQ3',
                  consumer_secret='rObL9LQu7pH0iU1DmvRvYiNpwzqBKtHQfWLJxBbuEfyvroAxB6',
                  access_token_key='913148816668454912-ir0ibXXXO0h2NU4PZhYIPm42ZbtNflf',
                  access_token_secret='hyTdLdsIGHaOMnPVQIaHEr3KCeThW4hlPK3BXTUkKthd6')

print(api.VerifyCredentials())
print(api.GetFriends())
