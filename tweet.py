from credentials import *
from rss_reader import *
import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


jvc_feed_url = "feed://www.jeuxvideo.com/rss/rss.xml"
gb_feed_url = "http://www.gameblog.fr/rss.php"
jvc_entries = get_entries(jvc_feed_url)
gb_entries = get_entries(gb_feed_url)

try:
    api.update_status(random_title(jvc_entries, gb_entries) + " #GlomebagActu")
except tweepy.TweepError as e:
    print(e.reason)
