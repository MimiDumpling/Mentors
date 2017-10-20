"""
You receive a list of strings.
Recursively search for a term in the list.
If you find the the term, return the index
of where it is. If not, return None.
"""

def find_needle(haystack, needle):

    def _find_needle(haystack, needle, n):

        # Base Case
        if n == len(haystack):
            return None

        if haystack[n] == needle:
            print haystack[n]
            return n

        print n
        return _find_needle(haystack, needle, n+1)

    _find_needle(haystack, needle, 0)

print find_needle(["hey", "there", "you"], "there")
