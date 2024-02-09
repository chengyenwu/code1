# 389. Find the difference
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for j in t:
            if j not in s or s.count(j) != t.count(j):
                return j