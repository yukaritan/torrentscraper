class Regex(object):
    """Mock class for a regular expression pattern object."""

    def __init__(self, flags, groups, groupindex, pattern):
        """Create a new pattern object.

        :type flags: int
        :type groups: int
        :type groupindex: dict[bytes | unicode, int]
        :type pattern: bytes | unicode
        """
        self.flags = flags
        self.groups = groups
        self.groupindex = groupindex
        self.pattern = pattern

    def search(self, string, pos=0, endpos=-1):
        """Scan through string looking for a match, and return a corresponding
        match instance. Return None if no position in the string matches.

        :type string: T <= bytes | unicode
        :type pos: int
        :type endpos: int
        :rtype: __Match[T] | None
        """
        pass

    def match(self, string, pos=0, endpos=-1):
        """Matches zero | more characters at the beginning of the string.

        :type string: T <= bytes | unicode
        :type pos: int
        :type endpos: int
        :rtype: __Match[T] | None
        """
        pass

    def split(self, string, maxsplit=0):
        """Split string by the occurrences of pattern.

        :type string: T <= bytes | unicode
        :type maxsplit: int
        :rtype: list[T]
        """
        pass

    def findall(self, string, pos=0, endpos=-1):
        """Return a list of all non-overlapping matches of pattern in string.

        :type string: T <= bytes | unicode
        :type pos: int
        :type endpos: int
        :rtype: list[T]
        """
        pass

    def finditer(self, string, pos=0, endpos=-1):
        """Return an iterator over all non-overlapping matches for the
        pattern in string. For each match, the iterator returns a
        match object.

        :type string: T <= bytes | unicode
        :type pos: int
        :type endpos: int
        :rtype: collections.Iterable[__Match[T]]
        """
        pass

    def sub(self, repl, string, count=0):
        """Return the string obtained by replacing the leftmost non-overlapping
        occurrences of pattern in string by the replacement repl.

        :type repl: bytes | unicode | collections.Callable
        :type string: T <= bytes | unicode
        :type count: int
        :rtype: T
        """
        pass

    def subn(self, repl, string, count=0):
        """Return the tuple (new_string, number_of_subs_made) found by replacing
        the leftmost non-overlapping occurrences of pattern with the
        replacement repl.

        :type repl: bytes | unicode | collections.Callable
        :type string: T <= bytes | unicode
        :type count: int
        :rtype: (T, int)
        """
        pass