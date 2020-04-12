# Use Zed's puny Python scanner example script, and turn it into a generic
# Scanner class.  It will take an input file, scan it into this list of
# tokens, which will then allow you to pull the tokens out in order.
import re


class Token(object):
    """Class to replace the `tuple` in the example script.  It should be
    able to track the token found, the matched string, the beginning,
    and the end of where it matched in the original string.
    """
    def __init__(self, token, matched_str, start, end):
        self.token = token
        self.matched_str = matched_str
        self.start = start
        self.end = end


class Scanner(object):

    def __init__(self, raw_tokens):
        """Takes a similar list of tuples (w/o the `re.compile`)
        and configures the scanner.  Or list of `Token()` objects
        with their associated string?
        """
        self.raw_tokens = raw_tokens
        self.tokens = []

        # get the regex objects for each of the tokens
        for regex, token in self.raw_tokens:
            pattern = re.compile(regex)
            self.tokens.append((pattern, token))

    def scan(self, string):
        """Takes a string and runs the scan on it, creating a list of tokens
        for later.  You should keep this string around for people to access
        later.
        """
        pass

    def match(self, token_list):
        """Given a list of possible tokens, return the first one that matches
        the first token in the list and removes it.
        """
        # adding code from the example...
        def match(i, line):  # obviously need to change this.
            start = line[i:]
            for regex, token in token_list:
                match = regex.match(start)
                if match:
                    begin, end = match.span()
                    return token, start[:end], end
            return None, start, None

    def peek(self, token_list):
        """Given a list of possible tokens, returns which ones **could**
        work with match but does not remove it from the list.
        """
        pass

    def push(self, token):
        """Push a token back on the token stream so that a later `peek` or
        `match` will return it.
        """
        pass
