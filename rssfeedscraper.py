"""This will scrape an RSS feed and return any items matching our naming convention"""
from datetime import datetime

import feedparser
import pytz
from abstorrentscraper import AbsTorrentScraper
from torrentlink import TorrentLink


class RSSFeedScraper(AbsTorrentScraper):
    def get_torrent_links(self) -> [TorrentLink]:
        """This will scrape an RSS feed and return any items matching our naming convention"""

        feed = feedparser.parse(self._url)
        if feed['bozo'] == 1:
            raise Exception(feed['bozo_exception'])

        naming = self.get_naming_convention()

        for item in feed['items']:
            season, episode = self.fallback_series_number, 0
            date = datetime.utcnow()

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

                try:
                    # Add a date if we could find one
                    date = datetime(*item['published_parsed'][:6], tzinfo=pytz.utc)
                except Exception as exception:
                    print(exception)

                # If everything worked out okay, let's "yield" it.
                # See https://wiki.python.org/moin/Generators
                yield TorrentLink(season, episode, item['link'], date)

            except AttributeError as e:
                print("failed to parse", item['title'])
                pass


if __name__ == '__main__':
    help(RSSFeedScraper.get_naming_convention)
    help(RSSFeedScraper.set_naming_convention)
    help(RSSFeedScraper.get_torrent_links)
