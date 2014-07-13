"""
This defines a very simple container class, the TorrenLink.

It's basically just a namedtuple:
https://docs.python.org/3.4/library/collections.html#collections.namedtuple

The date field should either contain the time when the date and time torrent was uploaded (in UTC),
or if the former isn't available, it shoud be set to the time when you first saw the torrent.
"""

from collections import namedtuple
TorrentLink = namedtuple('TorrentLink', ['season', 'episode', 'url', 'date'])


def sort_key(torrentlink: TorrentLink):
    """
    Use with sorted() as the key to sort by, and you'll get the torrent links by
    season, descending; episode, descending; date, ascending.
    In other words, you get the latest episode first.

    links = feed.get_torrent_links()
    for link in sorted(links, key=sort_key):
        print(link)
    """
    return -torrentlink.season, -torrentlink.episode, torrentlink.date
