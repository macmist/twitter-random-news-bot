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


gw_feed_url = "https://gamewave.fr/rss/"
gb_feed_url = "http://www.gameblog.fr/rss.php"
gw_entries = get_entries(gw_feed_url)
gb_entries = get_entries(gb_feed_url)

try:
    api.update_status(random_title(gw_entries, gb_entries) + " #GlomebagActu")
except tweepy.TweepError as e:
    print(e.reason)
