from credentials import *
from rss_reader import *
import tweepy
import ssl
import logging

# make sure there is no ssl exception
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

logger = logging.getLogger('tweet_bot')
logger.setLevel(logging.DEBUG)
logfile = logging.FileHandler('logs.log')
logfile.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logfile.setFormatter(formatter)
logger.addHandler(logfile)

try:
    res = randomize() + " #GlomebagActu"
    api.update_status(res)
    logger.info(res)

    #     print(randomize())
except tweepy.TweepError as e:
    print(e.reason)
    logger.error(e.reason)
