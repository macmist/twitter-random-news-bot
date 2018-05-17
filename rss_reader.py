import feedparser
import random
import shlex
from rss_urls import *


def pick_random(array):
    res = []
    for i in range(0, 2):
        choice = random.choice(array)
        array.remove(choice)
        res.append(choice)
        print(i)
    return res


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
    h1 = half_string(t1["title"], True)
    h2 = half_string(t2["title"], False)
    return h1 + " " + h2


def half_string(content, first_half):
    try:
        content = content.decode('utf-8')
    except AttributeError:
        pass
    mylist = shlex.split(content, False, False)
    cut = len(mylist) // 2
    half = mylist[0:cut] if first_half else mylist[cut:]
    return ' '.join(half)


def randomize():
    urls = pick_random(feed_urls)
    entries = []
    print(urls)
    for url in urls:
        entries.append(get_entries(url))
    print(entries)
    return random_title(entries[0], entries[1])