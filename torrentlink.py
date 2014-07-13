"""
This defines a very simple container class, the TorrenLink.

It's basically just a namedtuple:
https://docs.python.org/3.4/library/collections.html#collections.namedtuple
"""
from collections import namedtuple
TorrentLink = namedtuple('TorrentLink', ['season', 'episode', 'url'])
