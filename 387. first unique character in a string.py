# 387. First unique character in a string
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        c = Counter(s)
        print(c, type(c))
        for i, letter in enumerate(s):
            if c[letter] == 1:
                return i
        return -1