"""This will scrape an RSS feed and return any items matching our naming convention"""

import feedparser
from abstorrentscraper import AbsTorrentScraper
from torrentlink import TorrentLink


class RSSFeedScraper(AbsTorrentScraper):
    def get_torrent_links(self) -> [TorrentLink]:
        """This will scrape an RSS feed and return any items matching our naming convention"""

        feed = feedparser.parse(self._url)
        naming = self.get_naming_convention()

        for item in feed['items']:
            season, episode = 0, 0

            try:
                # Try to match this entry against the naming convention we defined before
                result = naming.match(item['title']).groupdict()

                try:
                    # If we caught a season number, let's try to convert it to an int
                    season = int(result['season'])
                except (KeyError, ValueError):
                    pass

                try:
                    # If we caught an episode number, let's try to convert it to an int
                    episode = int(result['episode'])
                except (KeyError, ValueError):
                    pass

                # If everything worked out okay, let's "yield" it.
                # See https://wiki.python.org/moin/Generators
                yield TorrentLink(season, episode, item['link'])

            except AttributeError as e:
                print(e)
                pass


if __name__ == '__main__':
    help(RSSFeedScraper.get_naming_convention)
    help(RSSFeedScraper.set_naming_convention)
    help(RSSFeedScraper.get_torrent_links)
