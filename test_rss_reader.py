from rss_reader import *
from rss_urls import *


def test_url_not_null():
    assert feed_urls is not None


def test_pick_randoms():
    res = pick_randoms(feed_urls)
    assert isinstance(res, list)


def test_randomize():
    r = randomize()
    assert r is not None
    assert isinstance(r, str)
    assert len(r) > 0
