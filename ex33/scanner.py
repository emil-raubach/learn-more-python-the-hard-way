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

    def __init__(self, raw_tokens, code):
        """Takes a similar list of tuples (w/o the `re.compile`)
        and configures the scanner.  Or list of `Token()` objects
        with their associated string?
        """
        self.raw_tokens = raw_tokens
        self.regex_list = self.get_regex(self.raw_tokens)
        self.tokens = self.scan(code)

    def scan(self, code):
        """Takes a string and runs the scan on it, creating a list of tokens
        for later.  You should keep this string around for people to access
        later.
        """
        self.script = []

        for line in code:
            i = 0
            while i < len(line):
                token, string, end = self.match(i, line)
                assert token, "Failed to match line %s" % string
                if token:
                    i += end
                    self.script.append((token, string, i, end))

        return self.script

    def match(self, i, line):
        """Given a list of possible tokens, return the first one that matches
        the first token in the list and removes it.
        """
        start = line[i:]
        for regex, token in self.regex_list:
            match = regex.match(start)
            if match:
                begin, end = match.span()
                return token, start[:end], end
        return None, start, None

    def get_regex(self, raw_tokens):
        # get the regex objects for each of the tokens
        regs = []

        for regex, token in raw_tokens:
            pattern = re.compile(regex)
            regs.append((pattern, token))

        return regs

    def peek(self, tokens):
        """Given a list of possible tokens, returns which ones **could**
        work with match but does not remove it from the list.
        """
        pass

    def push(self, tokens):
        """Push a token back on the token stream so that a later `peek` or
        `match` will return it.
        """
        pass

    def skip(self, tokens):
        pass

    def done(self):
        return len(self.tokens) == 0
