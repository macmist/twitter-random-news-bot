# Twitter News Title Bot

This is a simple bot* that generates a news title based on news title 
taken randomly from the internet

Usage:
- pip install feedparser tweepy
- Add your credentials in credentials.py
- Add the url feeds to search in rss_urls.py. At least 2 needed, but you can put more.
Note that it will take two randomly each time. Also this is not optimised for a too big
amount of link.
- python tweet.py

*For the moment it's more a script than an actual bot