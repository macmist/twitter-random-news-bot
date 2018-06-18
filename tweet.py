from credentials import *
from rss_reader import *
import tweepy
import ssl

# make sure there is no ssl exception
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


try:
    # api.update_status(randomize() + " #GlomebagActu")
    print(randomize())
except tweepy.TweepError as e:
    print(e.reason)
