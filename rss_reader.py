import feedparser
import random
import shlex

jvc_feed_url = "feed://www.jeuxvideo.com/rss/rss.xml"
gb_feed_url = "http://www.gameblog.fr/rss.php"


def get_entries(url):
    feed = feedparser.parse(url)
    entries = feed["items"]
    return entries


def print_titles(entries):
    for entry in entries:
        print(entry["title"])


def random_title(entries1, entries2):
    t1 = random.choice(entries1)
    t2 = random.choice(entries2)
    print("Title 1: " + t1["title"])
    print("Title 2: " + t2["title"])
    h1 = half_string(t1["title"], True)
    h2 = half_string(t2["title"], False)
    return h1 + " " + h2


def half_string(content, first_half):
    mylist = shlex.split(content.encode('utf8'), False, False)
    cut = len(mylist) / 2
    half = mylist[0:cut] if first_half else mylist[cut:]
    return ' '.join(half)


jvc_entries = get_entries(jvc_feed_url)
gb_entries = get_entries(gb_feed_url)
print("Final: " + random_title(jvc_entries, gb_entries))


