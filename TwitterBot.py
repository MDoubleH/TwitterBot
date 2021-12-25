# https://www.tweepy.org/
# https://developer.twitter.com/en/portal/dashboard

import tweepy
import time

consumer_key = 'UhGZOyvUbcV2AdP6qKO0JVyO5'
consumer_secret = '4rBfUDC5GI5vfWZ7wrRGWC6z8L2IRnUHVRy552kuucr22ihucr'
access_token = '184273645-bdNU0KIie6lF5dt7befq1E0O22xCB8y2w4HfMn8Z'
access_token_secret = 'LKmvs4A7c2auo4RlVLP5ArNcij1wCIhgSQ6nOeguuWq0f'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) 
print (user.screen_name)
print (user.followers_count)

search = "btc"
numberOfTweets = 2

#Limit API access speed. If we hit the rate limit pause for 10s
def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
            print("Sleeping now....")
            time.sleep(10)    # sleeps for 10 secs

#Follow your followers back.
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()

#Like my own teets and retweet anything with a keyword
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
