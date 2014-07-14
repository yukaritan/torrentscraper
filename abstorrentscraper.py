"""This is an abstract class. Do not instantiate directly."""

from re import compile
from torrentlink import TorrentLink


class AbsTorrentScraper:
    """This is an abstract class. Do not instantiate directly."""

    def __init__(self, url: str, naming_convention: str=None, fallback_series_number=0):
        self._url = url
        self._naming_convention = None
        self.set_naming_convention(naming_convention)
        self._fallback_series_number = fallback_series_number

    @property
    def url(self) -> str:
        """This returns the URL you passed to the constructor"""
        return self._url

    @property
    def fallback_series_number(self) -> int:
        """If a series number can't be found, use this number instead"""
        return self._fallback_series_number

    def get_naming_convention(self):
        """
        This is used to get a naming convention.
        It's useful both to find a specific torrent and,
        to figure out the season and episode.
        """
        return self._naming_convention

    def set_naming_convention(self, value: str) -> None:
        """
        This is used to set a naming convention.
        It's useful both to find a specific torrent and,
        to figure out the season and episode.
        """
        self._naming_convention = compile(value) if value is not None else None

    # This is another way of creating properties.
    # The other way is by "decorating" a function with @property
    # https://docs.python.org/3.4/library/functions.html#property
    naming_convention = property(get_naming_convention, set_naming_convention, doc="Naming convention")

    def get_torrent_links(self) -> [TorrentLink]:
        """
        You should overload this function and have it spit out a list of TorrentLinks:
        return [TorrentLink(i, i, "http://blahblah.com/?number=%d" % i) for i in range(5)]
        """
        raise NotImplementedError("Not implemented. Overload this method.")


if __name__ == '__main__':
    help(AbsTorrentScraper.get_naming_convention)
    help(AbsTorrentScraper.set_naming_convention)
    help(AbsTorrentScraper.get_torrent_links)
