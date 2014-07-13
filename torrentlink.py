"""
This defines a very simple container class, the TorrenLink.

It's basically just a namedtuple:
https://docs.python.org/3.4/library/collections.html#collections.namedtuple

The date field should either contain the time when the date and time torrent was uploaded (in UTC),
or if the former isn't available, it shoud be set to the time when you first saw the torrent.
"""

from collections import namedtuple
TorrentLink = namedtuple('TorrentLink', ['season', 'episode', 'url', 'date'])
