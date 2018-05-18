# Twitter News Title Bot

This is a simple bot[^1] that generates a news title based on news title 
taken randomly from the internet

Usage:
- pip install feedparser tweepy
- Add your credentials in credentials.py
- Add the url feeds to search in rss_urls.py. See next paragraph
- python tweet.py

[^1]:For the moment it's more a script than an actual bot


## rss_urls.py
You'll need to enter your rss urls in the feed_urls parameter.

Examples of what you can do:

1. only links -> will take two links randomly

    ---
    
        feed_urls = [
            "url-1",
            "url-2",
            ...
            "url-n"
        ]
    ---
2. links by themes -> will take two theme randomly then one link randomly in each theme

    ---
    
        feed_urls = [
            # theme 1
            [
                "url-1-theme-1",
                "url-2-theme-1",
                ...
                "url-n-theme-1
            ]
            # theme 2
            [
                "url-1-theme-2",
                "url-2-theme-2",
                ...
                "url-n-theme-n
            ],
            ...
            # theme n
            [
                "url-1-theme-n",
                "url-2-them-n"
            ]
        ]
    ---
3. mixup -> will take two items randomly, if it's a link, it'll take it, if it's a list, it'll take a random item inside
    
    ---
        
        feed_urls = [
            "url-1"
            "url-2"
            ...,
            # theme n
            [
                "url-1-theme-n",
                "url-2-them-n"
            ]
        ]
    ---