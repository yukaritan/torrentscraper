from rssfeedscraper import RSSFeedScraper
from torrentlink import sort_key


def test():
    url = "http://tf.maxters.net/pbay/search/pioneer%20one%20x264-VODO/0/99/0"
    naming_convention = "Pioneer.One.S(?P<season>\d+)E(?P<episode>\d+).720p.x264.VODO"

    feed = RSSFeedScraper(url=url, naming_convention=naming_convention)

    links = feed.get_torrent_links()
    for link in sorted(links, key=sort_key):
        print(link)


if __name__ == '__main__':
    test()