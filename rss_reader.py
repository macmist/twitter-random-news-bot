import feedparser
import random
import shlex
import copy
from rss_urls import *
from articles import *


def pick_randoms(dictionary):
    res = []
    new_dict = copy.deepcopy(dictionary)
    for i in range(0, 2):
        choice = 'mandatory' if 'mandatory' in new_dict else random.choice(list(new_dict))
        res.append(pick_random_helper(new_dict[choice]))
        del new_dict[choice]
    # shuffle so the mandatory does not always take the first position
    random.shuffle(res)
    return res


# determine whether the object is a link or a theme and return one link
def pick_random_helper(item):
    if type(item) is list:
        nested_choice = random.choice(item)
        item.remove(nested_choice)
        return nested_choice
    else:
        return item


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

    if h1[-1].lower() in articles and h2[0].lower() in articles:
        print(h1)
        h1 = h1[:-1]
        print(h1)
    h = h1 + h2
    res = " ".join(h)
    res = res.replace(": : ", ": ")
    return res


def half_string(content, first_half):
    try:
        content = content.decode('utf-8')
    except AttributeError:
        pass
    content = content.replace('« ', '"')
    content = content.replace(' »', '"')
    if ':' in content:
        l = content.rpartition(':')
        return (l[0] + ':').strip().split(' ') if first_half else l[2].strip().split(' ')
    mylist = shlex.split(content, False, False)
    cut = len(mylist) // 2
    half = mylist[0:cut] if first_half else mylist[cut:]
    return half


def randomize():
    urls = pick_randoms(feed_urls)
    entries = []
    for url in urls:
        entries.append(get_entries(url))
    return random_title(entries[0], entries[1])

