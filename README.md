# Twitter News Title Bot

This is a simple bot* that generates a news title based on news title 
taken randomly from the internet

Usage:
- pip install feedparser tweepy
- Add your credentials in credentials.py
- Add the url feeds to search in rss_urls.py. See next paragraph
- python tweet.py

*For the moment it's more a script than an actual bot


## rss_urls.py
You'll need to enter your rss urls in the feed_urls parameter.

Examples of what you can do:

1. only links -> will take two links randomly

    ---
    
        feed_urls = {
            1: "url-1",
            2: "url-2",
            ...
            n: "url-n"
        }
    ---
2. links by themes -> will take two theme randomly then one link randomly in each theme

    ---
    
        feed_urls = {
            # theme 1
            1: [
                "url-1-theme-1",
                "url-2-theme-1",
                ...
                "url-n-theme-1
            ],
            # theme 2
            2: [
                "url-1-theme-2",
                "url-2-theme-2",
                ...
                "url-n-theme-n
            ],
            ...
            # theme n
            n: [
                "url-1-theme-n",
                "url-2-them-n"
            ]
        }
    ---
3. mixup -> will take two items randomly, if it's a link, it'll take it, if it's a list, it'll take a random item inside
    
    ---
        
        feed_urls = {
            1: "url-1",
            2: "url-2"
            ...,
            # theme
            n: [
                "url-1-theme",
                "url-2-theme"
            ]
        }
    ---
    
4. mandatory -> if you want to always pick one same theme/url,
just give it the "mandatory" key (will only work for one)

    ---
    feed_urls = {
            "mandatory: "url-1",  # mandatory field, will always be picked
            2: "url-2"
            ...,
            # theme
            n: [
                "url-1-theme",
                "url-2-theme"
            ]
        }
    ---